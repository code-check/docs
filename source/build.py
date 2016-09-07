import os
import subprocess
from os.path import join, getsize
from HTMLParser import HTMLParser

import pdb, logging


# ============================================================================


logging.basicConfig( filename='log.log',
                     level=logging.DEBUG,
                     format='%(levelname)s: %(message)s [%(asctime)s]',
                     datefmt='%m/%d/%Y %I:%M:%S %p' )

cwd = str(os.getcwd())
lsResults = os.listdir(cwd)

isMkdocsInstalled = (
    subprocess.check_output(['mkdocs', '--version'])[0:15] == 'mkdocs, version')

googleTagManagerContainerId = 'GTM-MNRH4J'

googleTagManagerScriptLines = """
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
# """.format(containerId = googleTagManagerContainerId).splitlines()


# ============================================================================


class PostMkdocsParser(HTMLParser):

    def __init__(self, htmlFileFullPath):
        self.reset()
        self.markers          = set([])
        self.targetIsFullHTML = False
        self.targetFullPath   = htmlFileFullPath
        self.pruneLangs    = set([])
        if '/en/' in self.targetFullPath:
            self.pruneLangs.add('ja')
        if '/ja/' in self.targetFullPath:
            self.pruneLangs.add('en')

    def handle_decl(self, data):
        if data == "DOCTYPE html":
            self.targetIsFullHTML = True

            if not ('/en/' in self.targetFullPath or '/ja/' in self.targetFullPath):
                self.pruneLangs.add('en')
                self.pruneLangs.add('ja')

    def handle_starttag(self, tag, attrs):
        position = self.getpos()[0]
        if self.targetIsFullHTML and tag == 'body':
            # mark for injection of Google Tag Manager Script.
            self.markers.add(('injectTagManager', position))

        if ( tag == 'a' and (('href', '..') in attrs) and
                            (('class', '') in attrs)
           ):
                #mark for removal: unelegant blank TOC item.
                self.markers.add(('prune', position))

        for attr in attrs:
            if ((
                'ja' in self.pruneLangs and
                tag == 'a' and
                attr[0] == 'href' and
                ('../ja/' in attr[1] or attr[1].startswith('ja/'))
            ) or (
                'en' in self.pruneLangs and
                tag == 'a' and
                attr[0] == 'href' and
                ('../en/' in attr[1] or attr[1].startswith('en/'))
            )):
                #mark for removal: TOC items of the other language.
                self.markers.add(('prune', position))

                # retroactively prevent removal of main links from top level page to
                # each language's index page.
                if (
                    not('/en/' in self.targetFullPath or '/ja/' in self.targetFullPath) and
                    self.targetFullPath.endswith('/index.html') and
                    (attr[1] == 'en/' or attr[1] == 'ja/')
                ):
                    self.markers.remove(('prune', position))


# ============================================================================


if ('mkdocs.yml' in lsResults) and ('docs' in lsResults) and isMkdocsInstalled:
    print('All dependencies present. Initiate build...')
    subprocess.call('mkdocs build --clean', shell=True)
    print('Mkdocs build successful.')
    siteDirectory = cwd + "/site"
    htmlFileFullPaths = set([])

    print('Crawling html files...')
    for root, subDirectories, files in os.walk(siteDirectory):
        for filename in os.listdir(root):
            if filename.endswith('.html'):
                htmlFileFullPaths.add(root + '/' + filename)
                logging.debug(root + '/' + filename + ' found!')

    for htmlFileFullPath in htmlFileFullPaths:
        logging.debug('Parsing and marking ' + htmlFileFullPath)
        readHtmlFile = open(htmlFileFullPath, 'r')
        htmlString = readHtmlFile.read()
        parser = PostMkdocsParser(htmlFileFullPath)
        parser.feed(htmlString)

        readHtmlFile.close()

        if parser.markers:
            logging.debug('Modifying html...')
            htmlLines = htmlString.splitlines()

            markersList = []
            for marker in parser.markers:
                markersList.append(marker)
            # rearrange markers to start modifications from the end of each file.
            # this prevents `position`s from becoming outdated.
            markersList.sort(reverse=True)

            for marker in markersList:
                position = marker[1]

                if marker[0] == 'injectTagManager':
                    logging.debug('injecting tag manager at row ' + str(position))
                    htmlLines.insert(position, googleTagManagerScriptLines)
                    position += 1
                    # for line in googleTagManagerScriptLines:
                    #     htmlLines.insert(position, line)
                    #     position += 1

                if marker[0] == 'prune':
                    logging.debug('pop! goes ' + htmlLines[position-1])
                    htmlLines.pop(position-1)

            htmlNewString = '\n'.join(htmlLines)

            open(htmlFileFullPath, 'w').write(htmlNewString)
    print('Your dirty job is complete, boss! :sunglasses:')

else:
    logging.error( """ dependencies missing.
                       Make sure that:
                       - mkdocs is installed.
                       - this script runs in /source
                       - a mkdocs.yml file and a docs/ directory is present. """ )
    # TODO: Make errors specific, eg unique messages by missing dependency.
