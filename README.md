# Codecheck Documentation & Website

Welcome to Codecheck's Documentation Repo!  
We use [Mkdocs](http://www.mkdocs.org/) to build the site using only Markdown,
and we host it by pushing the built HTML pages to [GitHub Pages](http://pages.github.com/).  

This page is live [here](http://code-check.github.io/docs).
If you just want to view our documentation, I recommend the live page.

## Get Started

If you want to work on the site, you will want to install and run a local dev copy of it.

 1. **Install all dependencies.**
 2. `git clone` the contents of this repo.
 3. `cd [directory of clone]/source && mkdocs serve`
 6. Access http://localhost:8000/
 7. Yatta, you're finished!

## Dependencies

 * [Python & Pip](https://www.python.org/downloads/)
 * Mkdocs (`pip install mkdocs`)

## Instructions

- All of the source files are located in `/source`.  
- You can `mkdocs serve` to work on the site.  
- When you want to generate the static pages:
 - First, go to `/source` and `mkdocs build`.
 - The static pages will be generated into `/source/site`.
 - Move all the files in `/source/site` to the top. Remove any old files.
