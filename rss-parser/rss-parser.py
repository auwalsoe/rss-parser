import urllib.request
import xml.etree.ElementTree as ET


#print ("result code: " + str(webUrl.getcode()))
#data = webUrl.read()


class rss_parser():
    
    def __init__(self,rss_url):
        self.webUrl  = urllib.request.urlopen(rss_url)
        self.data = self.webUrl.read()
        self.root = ET.fromstring(self.data)
        self.feed_items = []
        self.get_version(self.root)
        self.getParams(self.root)
    def get_version(self,rss_root):
        self.rss_version = rss_root.attrib
    def getParams(self,rss_root):
        for child in rss_root:
            self.blog_title = self.checkIfNone(child.find('title'))
            self.blog_link = self.checkIfNone(child.find('link'))
            self.blog_description = self.checkIfNone(child.find('description'))
            self.blog_lastBuildDate = self.checkIfNone(child.find('lastBuildDate'))
            self.blog_language = self.checkIfNone(child.find('language'))
            self.blog_generator = self.checkIfNone(child.find('generator'))


        for element in child.iter('item'):
            feed_item = {}
            feed_item['post_title'] = str(self.checkIfNone(element.find('title')).encode("utf-8"))
            feed_item['post_link'] = self.checkIfNone(element.find('link'))
            feed_item['post_comments'] = self.checkIfNone(element.find('comments'))
            feed_item['post_pubDate'] = self.checkIfNone(element.find('pubDate'))
            feed_item['post_guid'] = self.checkIfNone(element.find('guid'))
            #tmp = self.checkIfNone(element.find('description'))
            #print(type((tmp).encode('utf-8').strip()))
            #print(repr(tmp.encode('utf-8').strip().decode("utf-8")))
            #feed_item['post_description'] = str(self.checkIfNone(element.find('description')).encode("utf-8"))
            self.feed_items.append(feed_item)
    def checkIfNone(self, element_test):
        if element_test is None:
            return "empty"
        else:
            return element_test.text
    def prettyPrint(self):
        for post in self.feed_items:
            print("-----------------------------------------")
            print("Title: " + post['post_title'])
            print("Published: " + post['post_pubDate'])
            print("Link: " + post['post_link'])
            print("guid: " + post['post_guid'])
            print(' ')
            #print(post['post_description'])
            print(post['post_comments'])
            print(' ')
            print(' ')
if __name__ =='__main__':
    #test = rss_parser('https://blog.acolyer.org/feed/')
    test = rss_parser('https://www.nrk.no/ostafjells/buskerud/toppsaker.rss')
    print(test.rss_version)
    test.prettyPrint()
