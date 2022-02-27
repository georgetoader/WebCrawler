from SiteCrawler import SiteCrawler

def main():
    crawler = SiteCrawler("https://www.hotnews.ro")

    # Get ALL urls and print them
    for url in crawler.crawl(SiteCrawler.Mode.ALL):
        print("Found: " + url)

if __name__ == '__main__':
    main()