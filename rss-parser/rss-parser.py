import urllib.request
import xml.etree.ElementTree as ET

class rss_parser():
    
    def __init__(self,rss_url):
        self.webUrl  = urllib.request.urlopen(rss_url)
        self.data = self.webUrl.read().decode("iso-8859-1")
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
            feed_item['post_title'] = self.checkIfNone(element.find('title'))
            feed_item['post_link'] = self.checkIfNone(element.find('link'))
            feed_item['post_comments'] = self.checkIfNone(element.find('comments'))
            feed_item['post_pubDate'] = self.checkIfNone(element.find('pubDate'))
            feed_item['post_guid'] = self.checkIfNone(element.find('guid'))
            feed_item['post_description'] = self.checkIfNone(element.find('description'))
            self.feed_items.append(feed_item)
    def checkIfNone(self, element_test):
        
        if type(element_test) == type(None) or type(element_test.text) == type(None):
            print("empty")
            return "empty".encode("iso-8859-1")
        else:
            return element_test.text.encode("iso-8859-1")
    def prettyPrint(self):
        for post in self.feed_items:
            print("-----------------------------------------")
            print("Title: " + str(post['post_title']))
            print("Published: " + str(post['post_pubDate']))
            print("Link: " + str(post['post_link'])
            print("guid: " + str(post['post_guid']))
            print(' ')
            print(str(post['post_description']))
            print((post['post_comments']))
            print(' ')
            print(' ')

