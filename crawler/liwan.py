#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request
import re
import pypandoc

if __name__ == '__main__':
    # Set total page number manually
    for page_num in range(7):
        page_url = 'http://www.sdsgwy.com/zhenti/list-liwan-{}.html'.format(page_num + 1)
        
        with urllib.request.urlopen(page_url) as response:
            soup = BeautifulSoup(response.read(), from_encoding = 'gb18030', features="lxml")

        articles = soup.find_all('a')
        for article in articles:
            if '事业' in article.text and '荔湾' in article.text:
                if 'article' in article.get('href'):
                    with urllib.request.urlopen(article.get('href')) as response:
                        soup_child = BeautifulSoup(response.read(), from_encoding = 'gb18030', features = "lxml")
                    filename = '{}.html'.format(article.text)
                    with open(filename, 'w') as f:
                        f.write(re.match(r'^(.+?)<p.*$', str(soup_child.find('div', id = 'mainNewsContent')), re.DOTALL).group(1) + '</div>')
                    pypandoc.convert_file(filename, 'docx', outputfile = "{}.docx".format(article.text))
                    contents = soup_child.find('div', id = 'mainNewsContent')