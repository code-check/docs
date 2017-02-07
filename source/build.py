import os
import subprocess
from os.path import join, getsize
from lib import googleTagManager
from lib import postMkdocs

import logging, pdb


# ============================================================================


logging.basicConfig(filename='log.log',
                    level=logging.DEBUG,
                    format='%(levelname)s: %(message)s [%(asctime)s]',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

cwd = str(os.getcwd())
lsResults = os.listdir(cwd)

isMkdocsInstalled = (
    subprocess.check_output(['mkdocs', '--version'])[0:15] == b'mkdocs, version')

googleTagManagerScriptLines = googleTagManager.scriptLines


# ============================================================================


if ('mkdocs.yml' in lsResults) and ('docs' in lsResults) and isMkdocsInstalled:
    print('All dependencies present. Initiate mkdocs build...')
    subprocess.call('mkdocs build --clean', shell=True)
    print('Mkdocs build successful.')

    print('Finding html files...')
    siteDirectory = cwd + "/site"
    htmlFileFullPaths = set([])
    for directoryPath, subDirectories, filenames in os.walk(siteDirectory):
        for filename in filenames:
            if filename.endswith('.html'):
                htmlFileFullPaths.add(directoryPath + '/' + filename)
                logging.debug(directoryPath + '/' + filename + ' found!')

    print('Parsing/modding html files...')
    for htmlFileFullPath in htmlFileFullPaths:
        logging.debug('Parsing and marking ' + htmlFileFullPath)
        readHtmlFile = open(htmlFileFullPath, 'r')
        htmlString = readHtmlFile.read()
        readHtmlFile.close()

        parser = postMkdocs.PostMkdocsParser(htmlFileFullPath)
        parser.feed(htmlString)

        if parser.markers:
            logging.debug('Modifying html...')
            htmlLines = htmlString.splitlines()

            # rearrange markers to start modifying from the end of each file.
            # this prevents `position`s from becoming outdated.
            markersList = []
            for marker in parser.markers:
                markersList.append(marker)
            markersList.sort(reverse=True)

            for marker in markersList:
                position = marker[1]

                if marker[0] == 'pruneDirectory':
                    logging.warning('illegal directory "source" detected! Avoiding...')
                    # TODO: avoiding code here?
                    continue

                if marker[0] == 'injectTagManager':
                    logging.debug('injecting tag manager at row '+str(position))
                    htmlLines.insert(position, googleTagManagerScriptLines)
                    position += 1

                if marker[0] == 'prune':
                    logging.debug('pop! goes ' + htmlLines[position-1])
                    htmlLines.pop(position-1)

            htmlNewString = '\n'.join(htmlLines)
            open(htmlFileFullPath, 'w').write(htmlNewString)

    print('Modding complete. Migrating files to repo top directory...')


    print('Your dirty job is complete, boss! :sunglasses:')

else:
    logging.error(""" dependencies missing.
                      Make sure that:
                      - mkdocs is installed.
                      - this script runs in /source
                      - a mkdocs.yml file and a docs/ directory is present. """)
    # TODO: Make errors specific, eg unique messages by missing dependency.
