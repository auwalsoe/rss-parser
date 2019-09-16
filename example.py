from rss_parser.rss_parser import rss_parser 

if __name__ == "__main__":
    test = rss_parser("https://news.ycombinator.com/rss")
    test.prettyPrint()
    test.toHtml("test")
