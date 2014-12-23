---
layout: default
title:  Documentation
---

## Getting Started

### Write in markdown

Write the text in Markdown.

```Markdown
# Title

Content

<!--
  Note
-->

----

Next content

____

## String of small content

Content
```

to HTML

```HTML
<slide>
  <hgroup>
    <h1>Title</h1>
  </hgroup>
  <article class="none">
    <p>Content</p>
    <aside class="note">
      Note
    </aside>
  </article>
</slide>

<slide>
  <hgroup>
    <p>Next content</p>
  </hgroup>
</slide>

<slide>
  <hgroup>
    <h2>String of small content</h2>
  </hgroup>
  <article class="smaller">
    <p>Content</p>
  </article>
</slide>
```

### Slideshow in browser

Use `alt + p` then presentation begins on Web browser.

## Guide

### Markdown

Convenient syntax to slide in the presentation.

#### Resize of Image

Set the attributes of the width and height in `<img>` tag.
 `100px` is the width of the image.

```Markdown
![original](https://octodex.github.com/images/original.png){:width="100px"}
```

to HTML

```HTML
<p><img alt="original" src="https://octodex.github.com/images/original.png" width="100px" /></p>
```

![original](https://octodex.github.com/images/original.png){:width="100px"}

#### Position change of image

Use the style sheet in the style attribute.
Centering the position of the image.

```Markdown
![repo](https://octodex.github.com/images/repo.png){:width="100px" style="display:block;margin-left:auto;margin-right:auto;"}
```

to HTML

```HTML
<p><img alt="repo" src="https://octodex.github.com/images/repo.png" style="display:block;margin-left:auto;margin-right:auto;" width="100px" /></p>
```

![repo](https://octodex.github.com/images/repo.png){:width="100px" style="display:block;margin-left:auto;margin-right:auto;"}

#### Link added to the image

I include to `[]()` `![]()`. `[![]()]()` is the state of the union.
Specify to `100px` in the left margin of the `<a>` tag.

```Markdown
[![benevocats](https://octodex.github.com/images/benevocats.png){:width="100px"}](https://octodex.github.com){:style="margin-left:100px;"}
```

to HTML

```HTML
<p><a href="https://octodex.github.com" style="margin-left:100px;">
<img alt="benevocats" src="https://octodex.github.com/images/benevocats.png" width="100px" /></a></p>
```

[![benevocats](https://octodex.github.com/images/benevocats.png){:width="100px"}](https://octodex.github.com){:style="margin-left:100px;"}

#### Style sheet for icon fonts

Use the style sheet with the class attribute.
Disable and underscores link in the black color of `<a>` tag.

```Markdown
<link rel="stylesheet" href="http://octicons.github.com/components/octicons/octicons/octicons.css">
[ ](){:class="mega-octicon octicon-mark-github" style="color:black;text-decoration:none;border-bottom:none"}
```

to HTML

```HTML
<p><link rel="stylesheet" href="http://octicons.github.com/components/octicons/octicons/octicons.css">
<a class="mega-octicon octicon-mark-github" href="" style="color:black;text-decoration:none;border-bottom:none"> </a></p>
```

<link rel="stylesheet" href="http://octicons.github.com/components/octicons/octicons/octicons.css">
[ ](){:class="mega-octicon octicon-mark-github" style="color:black;text-decoration:none;border-bottom:none"}

#### String with no display

Use HTML comments.
HTML does not change.

```Markdown
<!-- I ❤ CATS -->
```

to HTML

```HTML
<!-- I ❤ CATS -->
```
