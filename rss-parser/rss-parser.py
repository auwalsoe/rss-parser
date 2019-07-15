import urllib.request
import xml.etree.ElementTree as ET
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://blog.acolyer.org/feed/')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()

root = ET.fromstring(data)

for child in root:
    blog_title = child.find('title').text
    blog_link = child.find('link').text
    blog_description = child.find('description').text
    blog_lastBuildDate = child.find('lastBuildDate').text
    blog_language = child.find('language').text
    blog_generator = child.find('generator').text
    # print(link)
    # print(description)
    # print(lastBuildDate)
    # print(language)
    
    for element in child.iter('item'):
        post_title = element.find('title').text
        post_link = element.find('link').text
        post_comments = element.find('comments').text
        post_pubDate = element.find('pubDate').text
        post_guid = element.find('guid').text
        post_description = element.find('description').text.encode('utf-8').strip()
        print(post_title)
        print(post_link)
        print(post_comments)
        print(post_pubDate)
        print(post_guid)
        print(post_description)
        print(" ")
        #print(element.tag,element.attrib,element.text)
        
        #print(title)
        #for element2 in element:
        #    print(element2.tag, element2.attrib, element2.text)
        #    print(" ")