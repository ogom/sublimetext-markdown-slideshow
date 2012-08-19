import sublime
import sublime_plugin
import os
import sys
import tempfile
import webbrowser

pkg_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(pkg_path, 'lib'))

import mcider.converter as converter
import mcider.util as util

class MarkdownSlideshowCommand(sublime_plugin.TextCommand):
    """ slideshow in your web browser from file contents """

    def run(self, edit, themes=None, theme='default', extensions=[], clean=False, output_file=None, browser=True, save=None, path=None):
        """ TODO: save and path of the variable to be removed. """

        # slide options
        opts = {
            'themes': themes,
            'theme': theme,
            'contents': self.view.substr(sublime.Region(0, self.view.size())),
            'extensions': extensions,
            'clean': clean
        }

        # custom themes or default themes
        if opts['themes'] is None or not os.path.isdir(opts['themes']):
            opts['themes'] = os.path.join(pkg_path, 'themes')

        # path of the output file
        if output_file is None:
            output_path = None
        else:
            output_path = os.path.abspath(os.path.dirname(output_file))
            if not os.path.isdir(output_path):
                output_path = None

        if output_path is None:
            output_path = tempfile.mkdtemp()
            output_file = os.path.join(output_path, 'slide.html')
        
        # slide maker
        slide = converter.Slide(opts)
        html = slide.maker(output_path)
        util.fs_writer(output_file, html)

        if browser:
            webbrowser.open_new_tab('file://' + output_file)
        