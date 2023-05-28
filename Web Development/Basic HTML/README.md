# [Basic HTML](https://www.youtube.com/playlist?list=PL4cUxeGkcC9ibZ2TSBaGGNrgh4ZgYE6Cc)
- [Final Project](/Web%20Development/Basic%20HTML/final_project)

## Overview
- HTML is a Markup Language, not a programming language
- HTML uses tags (e.g \<p> \</p>) to mark content up
- The browser uses these tags to interpret how content should be structured
- Tags may contain attributes (e.g. \<span id="content-1"> \</span>), which adds extra information to individual tags
- We can nest tags (e.g. \<p> This is \<bold> bold \</bold> \</p>)
- Some tags are block-level elements (i.e. they start in a new line) and order are inline elements (i.e. )
- Some tags are self-contained (e.g. \<img>) and some are not (e.g. \<div> \</div>)

## Important Tags
- \<div> content \</div> : division
    - block-level
    - divides content into different sections
    - by itself, there's no visual different on the webpage. 
    - by using ids and classes, can be very useful to style things with CSS

- \<p> content \</p>: paragraph
    - block-level
    - used to introduce a paragraph

- \<h1> Header \</h1>: header
    - block-level
    - introduces a header. h1 is the biggest, and it gets smaller as you increase the number after 'h'. h6 is the smallest header.

- \<img src="">: image
    - block-level
    - adds an image to the webpage. The location of the image will be in the 'src' property

- \<a href=""> content \</a>: anchor
    - inline
    - used to turn 'content' into a link to (1) internal page, (2) external page, (3) file, (4) other elements in the same page
    - you can use attribute target="_black" to open the link in a new page

- \<ul> 
    - \<li> item 1 \</li>
    - \<li> item 2 \</li>
- \</ul> : unordered lists
    - block-level
    - lists items inside \<li> \</li> without numbering them

- \<ol> 
    - \<li> item 1 \</li>
    - \<li> item 2 \</li>
- \</ol> : ordered lists
    - block-level
    - lists items inside \<li> \</li> and adds the number of each item

- \<dl> 
    - \<dt> term 1 \</dt>
    - \<dd> definition 1 \</dd>
    - \<dt> term 2 \</dt>
    - \<dd> definition 2 \</dd>
- \</dl> : definition list
    - block-level
    - lists terms inside \<dt> and, below, their definitions \<dd>

- \<hr> : horizontal rule
    - adds a horizontal line

- \<br> : break
    - adds a line break

## CSS
Used to add style to your raw HTML content (e.g. make a sentence red)
There are 3 ways to modify the style of HTML element:
- 1. By using the "style" property inside an HTML tag
- - not ideal, because if you have 100 HTML elements that you want in a different color, you need to add these attributes one by one

- 2. By defining the styles between \<style> \</style> tags
- - not ideal, because if you have 5 pages with shared styles, you will need to add these \<style> \</style> tags to each one

- 3. By linking a CSS file to your HTML code inside the \<head> \</head> tag
- - good, because it keeps your styling decision separate to your content structure. Also, you can affect multiple elements and pages at the same time

## Javscript
Used to add functionalities (e.g. when you click a button, show this hidden text)
There are 3 ways to add Javscript to your HTML code:
- 1. By using inline properties (e.g. \<p onclick="console.log(hi)> Click Me \</p>)
- - not ideal, because it's harder to debug and it's not scalable

- 2. By using \<script> \</script> tags:
- - it should usually be at the bottom of the HTML page, because it will wait for the content to be loaded before running the code
- - not ideal, because if multiple pages use the same script, you will have to copy and paste, and debug them separately

- 3. By using external files \<script src=""> \</script>
- - it should usually be at the bottom of the HTML page, because it will wait for the content to be loaded before running the code
- - good, because it separates the script from the HTML structure, making it easier to debug

## Important Properties
- id: used to uniquely identify elements
- classes: can be used multiple times in the HTML. useful for treating similar content simmilarly (style, actions). One element may have different classes

## Pro-Tips
- Indentation is not functionally necessary, but it should be done to increase readability
- Although you can style your page with CSS, you should still use proper tags (e.g. \<h1>), because search engine crawlers use this information to rank your website
- When a style property is not explicit via CSS, the browsers will use their default styling options for each tag (e.g. \<h1>). They don't change much 
