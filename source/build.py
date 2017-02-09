import os
import subprocess
from os.path import join
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
postMkdocsParser = postMkdocs.htmlParser

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
                htmlFileFullPaths.add(join(directoryPath, filename))
                logging.debug(directoryPath + '/' + filename + ' found!')

            if filename.endswith('.md'):
                print('ruh oh!')
            if filename.endswith('.gitignore'):
                print('ruh oh!2')

            if directoryPath.endswith('.git') or directoryPath.endswith('source'):
                print('hrmmmmmmmm not good!')
                logging.warning(
                    'illegal directory {dir} detected, skipping!'.format(
                        dir=directoryPath
                ))
                os.replace( directoryPath,
                            directoryPath+'.skipped')
            if '.git' in subDirectories or 'source' in subDirectories:
                print('hrmmmmmmmm not good!')
                logging.warning(
                    'illegal directory {dirs} detected, skipping!'.format(
                        dirs=subDirectories
                ))
                pdb.set_trace()
    print('Parsing/modding html files...')
    for htmlFileFullPath in htmlFileFullPaths:
        logging.debug('Parsing and marking ' + htmlFileFullPath)
        readHtmlFile = open(htmlFileFullPath, 'r')
        htmlString = readHtmlFile.read()
        readHtmlFile.close()

        parser = postMkdocsParser(htmlFileFullPath)
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

                if marker[0] == 'skipDirectory':
                    logging.warning(
                        'illegal directory {dir} detected, skipping!'.format(
                            dir=marker[1]
                        )
                    )
                    dir, filename = os.path.split(htmlFileFullPath)
                    os.replace(dir, dir + '.skipped')
                    htmlFileFullPath = join(dir + '.skipped', filename)
                    break

                if marker[0] == 'skipFile':
                    print('whoop whoop!')
                    logging.warning(
                        'illegal file {filename} detected, skipping!'.format(
                            filename=marker[1]
                        )
                    )
                    os.replace(htmlFileFullPath, htmlFileFullPath + '.skipped')
                    htmlFileFullPath += '.skipped'
                    break

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
