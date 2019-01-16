from urllib.request import urlopen
from bs4 import BeautifulSoup

class Scraper():
    __url  = ''
    __data = ''

    def __init__(self, url):
        self.__url = url

    def get_page_data(self):
        self.__data = urlopen(self.__url)
        
    def get_links(self):
        soup = BeautifulSoup(self.__data.read(), 'html.parser')
        questions = soup.find(id="questions")
        
        with open("stack_links.html", 'w') as fileobj: 
            for count, link in enumerate(questions.find_all("h3")):          
                url = ' <a href="https://stackoverflow.com{}" target="_blank">{}</a></br></br>'.format(link.find("a")["href"], link.text)
                fileobj.write(str(count+1))
                fileobj.write(url)
                

url = 'https://stackoverflow.com/questions/tagged/django'
sobj = Scraper(url)
sobj.get_page_data()
sobj.get_links()
