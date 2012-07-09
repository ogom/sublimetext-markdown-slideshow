import sublime, sublime_plugin
import os
import tempfile
import markdown
import webbrowser

class MarkdownSlideshowCommand(sublime_plugin.TextCommand):
  """ slideshow in your web browser from file contents """

  def read_file(self, file):
    if not os.path.isfile(file):
      raise Exception(file + " file not found!")

    return open(file, 'r').read().decode('utf-8')

  def get_template(self, theme='default'):
    path = os.path.join(sublime.packages_path(), 'Markdown Slideshow', 'themes', theme)
    base = self.read_file(os.path.join(path, 'base.html'))
    css = self.read_file(os.path.join(path, 'css','styles.css'))
    js = self.read_file(os.path.join(path, 'js', 'slides.js'))

    return base.replace("{{ style }}", '\n' + css).replace("{{ script }}", '\n' + js)

  def get_slideshow(self, contents, template):
    html = markdown.markdown(contents) + '\n'
    article = '\n'

    pages = html.split('<hr />\n')
    for page in pages:
      article += '<article>\n' + page + '</article>\n\n'   

    return template.replace("{{ article }}", article)

  def run(self, edit, theme='default', save=True, path=None):
    contents = self.view.substr(sublime.Region(0, self.view.size()))
    template = self.get_template(theme)
    html = self.get_slideshow(contents, template)

    if save:
      if not path is None and not os.path.isdir(path):
        path=None
      
      temp = tempfile.NamedTemporaryFile(suffix=".html", dir=path, delete=False)
      temp.write(html.encode('utf-8'))
      temp.close()

      webbrowser.open_new_tab(temp.name)
    else:
      view = self.view.window().new_file()
      edit = view.begin_edit()
      view.insert(edit, 0, html)
      view.end_edit(edit)

