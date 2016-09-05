import sys
import os
import subprocess
from os.path import join, getsize

import pdb, logging

logging.basicConfig(level=logging.ERROR,
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

cwd = str(os.getcwd())
lsResults = os.listdir(cwd)

isMkdocsInstalled = (
    subprocess.check_output(['mkdocs', '--version'])[0:15] == 'mkdocs, version')

if ('mkdocs.yml' in lsResults) and ('docs' in lsResults) and isMkdocsInstalled:
    print('all dependencies present. Initiate build...')
    subprocess.call('mkdocs build --clean', shell=True)
    print('mkdocs build successful. Initiate tagmanager injection...')
    siteDirectory = cwd + "/site"
    htmlFileFullnames = []

    for root, subDirectories, files in os.walk(siteDirectory):
        for filename in os.listdir(root):
            if filename.endswith('.html'):
                htmlFileFullnames.append(root + '/' + filename)
                print root + '/' + filename + ' found!'

    for htmlFilefullname in htmlFileFullnames:
        print 'accessing' + htmlFilefullname + '...'
        htmlLines = open(htmlFilefullname, 'r').readlines()
        for index, line in enumerate(htmlLines):

            # TODO: Find header and insert tagmanager script right underneath it.

            # Identify top index page item in TOC.
            if '<a class="" href=".."></a>\n' in line:
                # TODO: Unnecessary item in TOC, remove element.
                print line

            # TODO: Identify EN items in JA pages in TOC and remove element.

            # TODO: Identify JA items in EN pages in TOC and remove element.

            # TODO: Change all filenames to unicode.
            pdb.set_trace()

    pdb.set_trace()

else:
    logging.error( """ dependencies missing.
                       Make sure that:
                       - mkdocs is installed.
                       - this script runs in /source
                       - a mkdocs.yml file and a docs/ directory is present. """ )
    # TODO: Make errors specific, eg unique messages by missing dependency.
