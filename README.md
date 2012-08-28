Markdown Slideshow
==================

A Sublime Text 2 plugin for slideshow in your web browser from markdown file.  
Create a contents for markdown and then preview the slides in your browser.

### Examples of themes

* [Google I/O 2012](http://ogom.github.com/python-mcider/examples/io2012/slide.html)
* [Google I/O 2011](http://ogom.github.com/python-mcider/examples/io2011/slide.html)


## Installation
### Package Control

The easy to install using the [Package Control](http://wbond.net/sublime_packages/package_control).

1. Press `ctrl+shift+p` (Windows) or `cmd+shift+p` (OS X). then `Package Control: Install Package`.
2. To install at the command of `Markdown Slideshow`.

### Github

Download is available from github, Install the folder of Sublime Text 2 Packages.

    $ git clone git://github.com/ogom/sublimetext-markdown-slideshow.git


## Usage

Let's add key bindings - user.

### Sample Key Bindings

    [
      {
        "keys": ["alt+s"], "command": "markdown_slideshow",
        "args": {"theme": "default"}
      }
    ]

### Google I/O 2012 theme

    [
      {
        "keys": ["alt+s"], "command": "markdown_slideshow",
        "args": {"theme": "io2012"}
      }
    ]

### Google I/O 2011 theme

    [
      {
        "keys": ["alt+s"], "command": "markdown_slideshow",
        "args": {"theme": "io2011"}
      }
    ]


### All options Key Bindings

    [
      {
        "keys": ["alt+s"], "command": "markdown_slideshow",
        "args":
        {
          "themes": "/opt/mcider/themes",
          "theme": "io2012",
          "extensions": ["fenced_code", "tables"],
          "browser": true,
          "presenter": false,
          "clean": false,
          "output_file": "/opt/mcider/tmp/slide.html"
        }
      }
    ]

#### args

* themes        : Path of the custom themes
* theme         : Theme of the slide. (default, io2012, io2011, ...) 
* extensions    : Provided to expand the base syntax. (extra, fenced_code, tables, ...) [See also](http://freewisdom.org/projects/python-markdown/Available_Extensions)
* browser       : View in Web Browser. (boolean, default true)
* presenter     : Presenter mode. Only theme `io2012`. (boolean, default false)
* clean         : Theme was to clean the output. (boolean, default false)
* output_file   : File to output slide.


## How to use

[See also](https://github.com/ogom/python-mcider#how-to-use)


## Examples

[See also](https://github.com/ogom/python-mcider#examples)


## Uses

* [python-mcider](https://github.com/ogom/python-mcider)
* [Python-Markdown](https://github.com/waylan/Python-Markdown)
* [HTML5 slide template for Google I/O 2012](http://code.google.com/p/io-2012-slides/)
* [HTML5 slide template for Google I/O 2011](http://code.google.com/p/html5slides/)


## Licence

* [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
