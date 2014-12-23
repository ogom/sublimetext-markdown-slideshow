import sublime
import sublime_plugin
import os
import sys
import tempfile
import webbrowser


def is_v3():
    return sys.version_info >= (3, 0)


if is_v3():
    from .lib.mcider import converter
    from .lib.mcider import util

else:
    from lib.mcider import converter
    from lib.mcider import util


class MarkdownSlideshowCommand(sublime_plugin.TextCommand):
    """ slideshow in your web browser from file contents """

    def run(self, edit):
        settings = sublime.load_settings('MarkdownSlideshow.sublime-settings')
        themes = settings.get('themes', None)
        theme = settings.get('theme', 'io2012')
        extensions = settings.get('extensions', [])
        output_file = settings.get('output_file', None)
        clean = settings.get('clean', False)
        browser = settings.get('browser', True)
        presenter = settings.get('presenter', False)

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
            pkg_path = os.path.abspath(os.path.dirname(__file__))
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
            url = 'file://' + output_file
            if slide.options['theme'] == 'io2012':
                url += '?presentme='
                url += 'true' if presenter else 'false'
            webbrowser.open_new_tab(url)
