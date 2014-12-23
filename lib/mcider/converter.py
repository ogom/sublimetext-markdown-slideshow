""" mcider - converter
Copyright(c) 2012-2014 ogom

slide maker
"""
import os
import sys
import shutil
from . import util


if util.is_v3():
    from ..markdown import Markdown
else:
    from markdown import Markdown


class Slide():
    """ Create a slide from the content and theme. """

    """ opts
        .themes themes path
        .theme io2012(default) or io2011
        .contents
        .extensions extra fenced_code tables, ...
        .clean (boolean, default False)
    """
    def __init__(self, opts):
        self.options = opts
        if 'themes' not in self.options:
            raise KeyError('themes')
        if 'theme' not in self.options:
            self.options['theme'] = 'io2012'
        if 'contents' not in self.options:
            self.options['contents'] = None
        if 'extensions' not in self.options:
            self.options['extensions'] = []
        if 'clean' not in self.options:
            self.options['clean'] = False

        if self.options['extensions'] is None:
            self.options['extensions'] = []

    def maker(self, output_path=None):
        theme_path = os.path.abspath(os.path.join(self.options['themes'], self.options['theme']))
        template = self._get_template(output_path, theme_path, self.options['clean'])
        slide = self._get_slide(self.options['theme'], self.options['contents'], self.options['extensions'])
        return template.replace('{{ slide }}', slide)

    def _get_template(self, output_path=None, theme_path=None, clean=False):
        """ copy theme assets and read base.html """
        assets = ['css', 'js', 'images']
        for asset in assets:
            src_path = os.path.join(theme_path, asset)
            if os.path.isdir(src_path):
                dst_path = os.path.join(output_path, asset)
                if clean and os.path.isdir(dst_path):
                    shutil.rmtree(dst_path)
                if not os.path.isdir(dst_path):
                    shutil.copytree(src_path, dst_path)
        return util.fs_reader(os.path.join(theme_path, 'base.html'))

    def _get_slide(self, theme=None, contents=None, extensions=[]):
        html = None
        if theme == 'io2011':
            html = self._get_slide_io2011(contents, extensions)
        elif theme == 'io2012':
            html = self._get_slide_io2012(contents, extensions)
        else:
            html = self._get_slide_none(contents, extensions)
        return html

    def _get_slide_none(self, contents=None, extensions=[]):
        """ none style """
        md = Markdown(extensions=extensions)

        # from pages to slides
        pages = md.convert(contents) + '\n'
        slides = pages.split('<hr />\n')

        # from slides to html
        html = '\n'
        for slide in slides:
            html += '<article>\n'
            html += slide
            html += '</article>\n\n'
        return html

    def _get_slide_io2012(self, contents=None, extensions=[]):
        """ io-2012 style """
        md = Markdown(extensions=extensions)
        splits = [
            {'horizon': '----', 'style': 'none'},
            {'horizon': '____', 'style': 'smaller'},
            {'horizon': '****', 'style': 'fill'}
        ]

        styles = []
        for split in splits:
            styles.append(split['style'])
            horizon = '\n' + split['horizon'] + '\n'
            contents = contents.replace(horizon, '\n---\n' + split['style'] + '\n')

        pages = contents.split('\n---\n')

        # from pages to slides
        slides = []
        for page in pages:
            sections = page.split('\n\n', 2)
            slide = {}
            if not sections[0] in styles:
                if len(sections) > 2:
                    sections[1] += '\n\n' + sections[2]
                sections.insert(0, 'none')
            slide['style'] = sections[0]
            if len(sections) > 1:
                slide['hgroup'] = sections[1]
            if len(sections) > 2:
                slide['article'] = sections[2]
            slides.append(slide)

        # from slides to html
        html = '\n'
        for slide in slides:
            html += '<slide>\n'
            if 'hgroup' in slide:
                html += '<hgroup>\n'
                html += md.convert(slide['hgroup']) + '\n'
                html += '</hgroup>\n'
            if 'article' in slide:
                html += '<article class="' + slide['style'] + '">\n'
                html += md.convert(slide['article']) + '\n'
                html += '</article>\n'
            html += '</slide>\n\n'

        # from comment out to presener note
        html = html.replace('\n<!--\n', '\n<aside class="note">\n')
        html = html.replace('\n-->\n', '\n</aside>\n')

        return html

    def _get_slide_io2011(self, contents=None, extensions=[]):
        """ io-2011 style """
        md = Markdown(extensions=extensions)
        splits = [
            {'horizon': '----', 'style': 'none'},
            {'horizon': '____', 'style': 'smaller'},
            {'horizon': '****', 'style': 'fill'}
        ]

        styles = []
        for split in splits:
            styles.append(split['style'])
            horizon = '\n' + split['horizon'] + '\n'
            contents = contents.replace(horizon, '\n---\n' + split['style'] + '\n')

        pages = contents.split('\n---\n')

        # from pages to slides
        slides = []
        for page in pages:
            sections = page.split('\n\n', 1)
            slide = {}
            if not sections[0] in styles:
                if len(sections) > 1:
                    sections[0] += '\n\n' + sections[1]
                sections.insert(0, 'none')
            slide['style'] = sections[0]
            if len(sections) > 1:
                slide['article'] = sections[1]
            slides.append(slide)

        # from slides to html
        html = '\n'
        for slide in slides:
            if 'article' in slide:
                html += '<article class="' + slide['style'] + '">\n'
                html += md.convert(slide['article']) + '\n'
                html += '</article>\n\n'
        return html
