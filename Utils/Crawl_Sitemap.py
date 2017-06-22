#!user/bin/env python
# -*- coding: utf-8 -*-
' utils : 网站地图爬虫 '
import re
from Download import download
def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)<loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)

if __name__ == '__main__':
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')