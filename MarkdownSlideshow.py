import sublime
import sublime_plugin
import sys
import os
import tempfile
import webbrowser
import shutil

# add local libs
if os.path.join(sublime.packages_path(), 'Markdown Slideshow', 'lib') not in sys.path:
    sys.path.append(os.path.join(sublime.packages_path(), 'Markdown Slideshow', 'lib'))

from markdown import markdown


class MarkdownSlideshowCommand(sublime_plugin.TextCommand):
    """ slideshow in your web browser from file contents """

    path_theme = None

    def read_file(self, file):
        if not os.path.isfile(file):
            raise Exception(file + " file not found!")

        return open(file, 'r').read().decode('utf-8')

    def get_template(self, theme='default'):
        self.path_theme = os.path.join(sublime.packages_path(), 'Markdown Slideshow', 'themes', theme)
        base = self.read_file(os.path.join(self.path_theme, 'base.html'))
        css = self.read_file(os.path.join(self.path_theme, 'css', 'styles.css'))
        js = self.read_file(os.path.join(self.path_theme, 'js', 'slides.js'))

        return base.replace("{{ style }}", '\n' + css).replace("{{ script }}", '\n' + js)

    def get_slideshow(self, contents, template):
        html = markdown(contents, ['fenced_code', 'tables']) + '\n'
        article = '\n'

        pages = html.split('<hr />\n')
        for page in pages:
            article += '<article>\n' + page + '</article>\n\n'

        return template.replace("{{ article }}", article)

    def copy_images(self, dest):
        images_dir = os.path.join(self.path_theme, "images")
        if (os.path.isdir(images_dir)):
            shutil.copytree(images_dir, os.path.join(dest, "images"))

    def run(self, edit, theme='default', save=True, path=None):
        contents = self.view.substr(sublime.Region(0, self.view.size()))
        template = self.get_template(theme)
        html = self.get_slideshow(contents, template)

        if save:
            if not path is None and not os.path.isdir(path):
                path = None

            tempDir = tempfile.mkdtemp(dir=path)
            temp = open(os.path.join(tempDir, "slide.html"), "w")
            temp.write(html.encode('utf-8'))
            temp.close()
            self.copy_images(tempDir)

            webbrowser.open_new_tab(temp.name)
        else:
            view = self.view.window().new_file()
            edit = view.begin_edit()
            view.insert(edit, 0, html)
            view.end_edit(edit)
