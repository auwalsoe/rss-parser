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
        self.getParams(self.root)
    def getParams(self,rss_root):
        for child in rss_root:
            self.blog_title = child.find('title').text
            self.blog_link = child.find('link').text
            self.blog_description = child.find('description').text
            self.blog_lastBuildDate = child.find('lastBuildDate').text
            self.blog_language = child.find('language').text
            self.blog_generator = child.find('generator').text


        for element in child.iter('item'):
            feed_item = {}
            feed_item['post_title'] = element.find('title').text
            feed_item['post_link'] = element.find('link').text
            feed_item['post_comments'] = element.find('comments').text
            feed_item['post_pubDate'] = element.find('pubDate').text
            feed_item['post_guid'] = element.find('guid').text
            feed_item['post_description'] = element.find('description').text.encode('utf-8').strip()
            self.feed_items.append(feed_item)
    def prettyPrint(self):
        for post in self.feed_items:
            print("-----------------------------------------")
            print("Title: " + post['post_title'])
            print("Published: " + post['post_pubDate'])
            print("Link: " + post['post_link'])
            print("guid: " + post['post_guid'])
            print(' ')
            print(post['post_description'])
            print(post['post_comments'])
            print(' ')
            print(' ')
if __name__ =='__main__':
    test = rss_parser('https://blog.acolyer.org/feed/')
    test.prettyPrint()