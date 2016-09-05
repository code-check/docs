import os
import subprocess
from os.path import join, getsize
from HTMLParser import HTMLParser

import pdb, logging


logging.basicConfig(level=logging.DEBUG,
                    filename='logs.log',
                    filemode='w')

googleTagManagerContainerId = 'GTM-MNRH4J'

googleTagManagerScript = """
<!-- Google Tag Manager -->
  <noscript>
    <iframe src="//www.googletagmanager.com/ns.html?id={containerId}"
    height="0" width="0" style="display:none;visibility:hidden"></iframe>
  </noscript>
  <script>
    (function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','{containerId}');
  </script>
<!-- End Google Tag Manager -->
""".format(containerId = googleTagManagerContainerId)

# create a subclass and override the handler methods
class PostMkdocsParser(HTMLParser):

    targetIsFullHTML = False
    targetLang = ''
    results = set([])

    def __kill__(self):
        self.targetIsFullHTML = False
        self.targetLang = ''
        self.results = ''
        self.results = set([])

    def handle_decl(self, data):
        if data == "DOCTYPE html":
            self.targetIsFullHTML = True

    def handle_starttag(self, tag, attrs):
        for attr in attrs:

            # TODO: Find header and insert tagmanager script right underneath it.

            if self.targetIsFullHTML and tag == 'body':
                self.results.add(('injectTagManager', self.getpos()))

            if ( (tag == 'a' and attr == ('href', '..')) or
                 (self.targetLang == 'en' and tag == 'a' and
                  attr[0] == 'href' and ('../ja/' in attr[1])) or
                 (self.targetLang == 'jp' and tag == 'a' and
                  attr[0] == 'href' and ('../en/' in attr[1]))
               ):
                    #redundant top level index TOC item.
                    self.results.add(('kill', self.getpos()))

cwd = str(os.getcwd())
lsResults = os.listdir(cwd)

isMkdocsInstalled = (
    subprocess.check_output(['mkdocs', '--version'])[0:15] == 'mkdocs, version')

if ('mkdocs.yml' in lsResults) and ('docs' in lsResults) and isMkdocsInstalled:
    print('all dependencies present. Initiate build...')
    subprocess.call('mkdocs build --clean', shell=True)
    print('mkdocs build successful. Initiate tagmanager injection...')
    siteDirectory = cwd + "/site"
    htmlFileFullPaths = set([])

    for root, subDirectories, files in os.walk(siteDirectory):
        for filename in os.listdir(root):
            if filename.endswith('.html'):
                htmlFileFullPaths.add(root + '/' + filename)
                logging.debug(root + '/' + filename + ' found!')

    allResults = []

    for htmlFileFullPath in htmlFileFullPaths:
        print 'accessing ' + htmlFileFullPath + '...'
        htmlFile = open(htmlFileFullPath, 'r')
        htmlString = htmlFile.read()
        parser = PostMkdocsParser()

        if '/en/' in htmlFileFullPath:
            parser.targetLang = 'en'
        if '/ja/' in htmlFileFullPath:
            parser.targetLang = 'ja'
        parser.feed(htmlString)
        if parser.results:
            allResults.append((htmlFileFullPath, parser.results))
            pdb.set_trace()
        print 'htmlFileFullPath is: ' + htmlFileFullPath

        htmlFile.close()
        parser.__kill__()
        parser.reset()
        # TODO: Identify EN items in JA pages in TOC and remove element.
        # TODO: Identify JA items in EN pages in TOC and remove element.
        # TODO: Change all filenames to unicode.
    pdb.set_trace()

    # for results in allResults:

else:
    logging.error( """ dependencies missing.
                       Make sure that:
                       - mkdocs is installed.
                       - this script runs in /source
                       - a mkdocs.yml file and a docs/ directory is present. """ )
    # TODO: Make errors specific, eg unique messages by missing dependency.
