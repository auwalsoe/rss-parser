import urllib.request
import xml.etree.ElementTree as ET

webUrl  = urllib.request.urlopen('https://blog.acolyer.org/feed/')
print ("result code: " + str(webUrl.getcode()))
data = webUrl.read()

root = ET.fromstring(data)

for child in root:
    blog_title = child.find('title').text
    blog_link = child.find('link').text
    blog_description = child.find('description').text
    blog_lastBuildDate = child.find('lastBuildDate').text
    blog_language = child.find('language').text
    blog_generator = child.find('generator').text

    
    for element in child.iter('item'):
        post_title = element.find('title').text
        post_link = element.find('link').text
        post_comments = element.find('comments').text
        post_pubDate = element.find('pubDate').text
        post_guid = element.find('guid').text
        post_description = element.find('description').text.encode('utf-8').strip()
