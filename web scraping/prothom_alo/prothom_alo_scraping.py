"""
__author__     = "Md. Ashikun Nabi"
__maintainer__ = "Md. Ashikun Nabi"
__email__      = "ashikunnabituhin@gmail.com"
__status__     = "Education"

"""

import requests
from bs4 import BeautifulSoup


url  = "https://www.prothomalo.com"
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

# Full page download
with open('FirstPage.html', 'w', encoding='UTF-8') as fp:
    fp.write(soup.prettify())

print("====================================================")
print("====================All Links=======================")
print("====================================================")

with open('prothomalo.html', 'w', encoding='UTF-8') as file:
    link_count = 1
    for link in soup.find_all("a"):
        if (len(link.text)) < 1:
            if str(link.get("href")).startswith("/"):
                link = ' <a href="{}{}" target="_blank">No title</a>'.format(url, link.get("href"))
            else:
                link = ' <a href="{}" target="_blank">No Title</a>'.format(link.get("href"))
        else:
            if str(link.get("href")).startswith('/'):
                link = ' <a href="{}{}" target="_blank">{}</a>'.format(url, link.get("href"), link.text)
            else:
                link = ' <a href="{}" target="_blank">{}</a>'.format(link.get("href"), link.text)
                                                                       
        file.write(str(link_count))
        file.write(link)
        file.write("<br>")
        link_count = link_count + 1
        
    print("====================================================")
    print("====================All Image=======================")
    print("====================================================")

    image_count = 1
    for image in soup.find_all("img"):
        if str(image.get("src")).startswith("https:"):
            link = ' <img src="{}"> </br>{}'.format(image['src'], image.get('alt'))
        else:            
            link = ' <img src="https:{}"> </br>{}'.format(image.get("src"), image.get('alt'))

        file.write(str(image_count))
        file.write(link)
        file.write("<br>")
        image_count = image_count + 1
