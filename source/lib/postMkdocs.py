from html.parser import HTMLParser

class PostMkdocsParser(HTMLParser):

    def __init__(self, htmlFileFullPath):
        self.reset()
        self.convert_charrefs = True
        self.markers          = set([])
        self.targetIsFullHTML = False
        self.targetFullPath   = htmlFileFullPath
        self.pruneLangs       = set([])
        if '/en/' in self.targetFullPath:
            self.pruneLangs.add('ja')
        if '/ja/' in self.targetFullPath:
            self.pruneLangs.add('en')
        if self.targetFullPath.split('/')[-2] == 'source':
            self.markers.add(('pruneDirectory', ''))

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

        if self.isPruneEmptyElement(tag, attrs):
            # mark for removal: unelegant blank TOC item.
            self.markers.add(('prune', position))

        if self.isPruneReleaseNotesElement(tag, attrs):
            self.markers.add(('prune', position))

        for attr in attrs:
            if self.isPruneLangElement(tag, attr):
                # mark for removal: TOC items of the other language.
                self.markers.add(('prune', position))

                # retroactively prevent removal of main links from
                #  top level page to each language's index page.
                if self.isExceptionTopIndex(attr):
                    self.markers.remove(('prune', position))

    def handle_data(self, data):
        position = self.getpos()[0]
        if self.isStartPruneReleaseNotesData(data):
            self.markers.add(('startPrune', position+1))
        # if self.isPruneReleaseNotesData(self, data):
        #     self.markers.add(('prune', position))


    def handle_endtag(self, tag):
        if self.isEndPruneReleaseNotesData(tag):
            for i in self.markers:
                if i[0] == 'startPrune':
                    removeLoc = i[1]
            self.markers.remove(('startPrune', removeLoc))

    def isPruneEmptyElement(self, tag, attrs):
        return (
            tag == 'a' and (('href', '..') in attrs) and
                           (('class', '') in attrs)
        )

    def isPruneReleaseNotesElement(self, tag, attrs):
        href = False
        classIsToctreeL4 = False
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    href = True
                if attr == ('class', 'toctree-l4'):
                    classIsToctreeL4 = True
        for i in self.markers:
            if i[0] == 'startPrune' and href and classIsToctreeL4 and (i[1] < self.getpos()[0]):
                return True


        # return hrefStartsWithV and classIsToctreeL4

    def isPruneLangElement(self, tag, attr):
        return ((
            'ja' in self.pruneLangs and tag == 'a' and attr[0] == 'href' and
            ('../ja/' in attr[1] or attr[1].startswith('ja/'))
        ) or (
            'en' in self.pruneLangs and tag == 'a' and attr[0] == 'href' and
            ('../en/' in attr[1] or attr[1].startswith('en/'))
        ))

    def isStartPruneReleaseNotesData(self, data):
        return data == u'過去のリリース'

    def isEndPruneReleaseNotesData(self, tag):
        for i in self.markers:
            if i[0] == 'startPrune' and tag == 'ul' and (i[1] < self.getpos()[0]):
                return True

    def isExceptionTopIndex(self, attr):
        return (
            not('/en/' in self.targetFullPath or '/ja/' in self.targetFullPath) and
            self.targetFullPath.endswith('/index.html') and
            (attr[1] == 'en/' or attr[1] == 'ja/')
        )
