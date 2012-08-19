Markdown Slideshow
==================

A Sublime Text 2 plugin for slideshow in your web browser from markdown file.  
Create a contents for markdown and then preview the slides in your browser.

#### Examples of themes

* [Google I/O 2012](http://ogom.github.com/sublimetext-markdown-slideshow/examples/io2012/slide.html)
* [Google I/O 2011](http://ogom.github.com/sublimetext-markdown-slideshow/examples/io2011/slide.html)

---

### Installation
#### Package Control

The easy to install using the [Package Control](http://wbond.net/sublime_packages/package_control).

1. Press `ctrl+shift+p` (Windows) or `cmd+shift+p` (OS X). then `Package Control: Install Package`.
2. To install at the command of `Markdown Slideshow`.

---

#### Github

Download is available from github, Install the folder of Sublime Text 2 Packages.

    $ git clone git://github.com/ogom/sublimetext-markdown-slideshow.git

___

### Usage
#### Sample Key Bindings

Let's add key bindings - user.

    [
      {
        "keys": ["alt+s"], "command": "markdown_slideshow",
        "args": {"theme": "default"}
      }
    ]

##### args
* theme         : Theme of the slide. (default, io2012, io2011, ...) 
* extensions    : Provided to expand the base syntax. (extra, fenced_code, tables, ...)
* clean         : Theme was to clean the output. (boolean, default False)
* output_file   : File to output slide.
* browser       : View in Web Browser. (boolean, default True)
* themes        : Path of the custom themes

---

### How to use
#### Output Hints

Separates the slide is `---` or `___` or `***` be returned to hr tab at markdown.  
io2012 or io2011 of the theme to change the class of article in the horizon. 

     horizon |  article class
    -------- | --------------
      ---    |  none
      ___    |  smaller
      ***    |  fill

---

### Examples

#### Theme of io2012

Markdown the original

```markdown
I/O 2012 slide example
======================

---

### Simple slide with header and text
Here is the text of hgroup.

This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  

There is more text just underneath.

___

### Simple slide with header and text (small font)
Here is the text of hgroup.

This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  

There is more text just underneath.

***

### Image filling the slide (with optional header)
Here is the text of hgroup.

![syaraku](images/syaraku_eye.jpg)

There is more text just underneath.
```

The converted html

```html
<slide>
  <hgroup>
    <h1>
      I/O 2012 slide example
    </h1>
  </hgroup>
</slide>

<slide>
  <hgroup>
    <h3>
      Simple slide with header and text
    </h3>
    <p>
      Here is the text of hgroup.
    </p>
  </hgroup>
  <article class="none">
    <p>
      This is a slide with just text. This is a slide with just text.<br />
      This is a slide with just text. This is a slide with just text.<br />
      This is a slide with just text. This is a slide with just text.<br />
    </p>
    <p>
      There is more text just underneath.
    </p>
  </article>
</slide>

<slide>
  <hgroup>
    <h3>
      Simple slide with header and text (small font)
    </h3>
    <p>
      Here is the text of hgroup.
    </p>
  </hgroup>
  <article class="smaller">
    <p>
      This is a slide with just text. This is a slide with just text.<br />
      This is a slide with just text. This is a slide with just text.<br />
      This is a slide with just text. This is a slide with just text.<br />
    </p>
    <p>
      There is more text just underneath.
    </p>
  </article>
</slide>

<slide>
  <hgroup>
    <h3>
      Image filling the slide (with optional header)
    </h3>
    <p>
      Here is the text of hgroup.
    </p>
  </hgroup>
  <article class="fill">
    <p>
      <img alt="syaraku" src="images/syaraku_eye.jpg" />
    </p>
    <p>
      There is more text just underneath.
    </p>
  </article>
</slide>
```


#### Theme of io2011

Markdown the original

```markdown
I/O 2011 slide example
======================

---

### Simple slide with header and text

This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  

There is more text just underneath.

___

### Simple slide with header and text (small font)

This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  
This is a slide with just text. This is a slide with just text.  

There is more text just underneath.

***

### Image filling the slide (with optional header)

![syaraku](images/syaraku_eye.jpg)

There is more text just underneath.
```

The converted html

```html
<article class="none">
  <h1>
    I/O 2011 slide example
  </h1>
</article>

<article class="none">
  <h3>
    Simple slide with header and text
  </h3>
  <p>
    This is a slide with just text. This is a slide with just text.<br />
    This is a slide with just text. This is a slide with just text.<br />
    This is a slide with just text. This is a slide with just text.<br />
  </p>
  <p>
    There is more text just underneath.
  </p>
</article>

<article class="smaller">
  <h3>
    Simple slide with header and text (small font)
  </h3>
  <p>
    This is a slide with just text. This is a slide with just text.<br />
    This is a slide with just text. This is a slide with just text.<br />
    This is a slide with just text. This is a slide with just text.<br />
  </p>
  <p>
    There is more text just underneath.
  </p>
</article>

<article class="fill">
  <h3>
    Image filling the slide (with optional header)
  </h3>
  <p>
    <img alt="syaraku" src="images/syaraku_eye.jpg" />
  </p>
  <p>
    There is more text just underneath.
  </p>
</article>
```
---

### Uses

* [python-mcider](https://github.com/ogom/python-mcider)
* [Python-Markdown](https://github.com/waylan/Python-Markdown)
* [HTML5 slide template for Google I/O 2012](http://code.google.com/p/io-2012-slides/)
* [HTML5 slide template for Google I/O 2011](http://code.google.com/p/html5slides/)

---

### Licence

* [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
