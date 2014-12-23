Markdown Slideshow
==================

Markdown converter for slideshow.

* A Sublime Text 2/3 plugin for slideshow in your web browser from markdown file.
* Create a contents for markdown and then preview the slides in your browser.

## Installation
### Package Control

The easy to install using the [Package Control](http://wbond.net/sublime_packages/package_control).

1. Press `ctrl+shift+p` (Windows) or `cmd+shift+p` (OS X). then `Package Control: Install Package`.
2. To install at the command of `Markdown Slideshow`.

### Github

Download is available from github, Install the folder of Sublime Text 2/3 Packages.

```
$ git clone git://github.com/ogom/sublimetext-markdown-slideshow.git
```

## Usage

### Default Settings

```
{
  // Path of the custom themes
  "themes": null,

  // Theme of the slide. (io2012, io2011, ...)
  "theme" : "io2012",

  // Provided to expand the base syntax. (extra, fenced_code, tables, ...)
  "extensions": [],

  // Theme was to clean the output.
  "clean" : false,

  // File to output slide.
  "output_file": null,

  // View in Web Browser.
  "browser": true,

  // Presenter mode. Only theme io2012.
  "presenter": false
}
```

### Key Bindings

```
[
  {
    "keys": ["alt+s"], "command": "markdown_slideshow"
  }
]
```

## Examples

* [Google I/O 2012](http://ogom.github.com/python-mcider/examples/io2012/slide.html)
* [Google I/O 2011](http://ogom.github.com/python-mcider/examples/io2011/slide.html)

## Uses

* [python-mcider](https://github.com/ogom/python-mcider)

## Licence

* MIT
