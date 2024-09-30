# from bs4 import BeautifulSoup 
# import requests

# def apstrada_lapu(url):
#     r = requests.get(url)
#     html = r.text
#     soup = BeautifulSoup(html, "html.parser")
#     return soup

# html = apstrada_lapu("https://www.liepajniekiem.lv")
# print(html.head.title.text)

# tags = html.find_all('h2')
# for tag in tags:
#     print(tag.text)

# from bs4 import BeautifulSoup
# import requests
# def apstrada_lapu(url):
#     r = requests.get(url)
#     html = r.text
#     soup = BeautifulSoup(html, 'html.parser')
#     return soup
# html = apstrada_lapu("https://www.tvnet.lv")
# print(html.head.title.text) 

# tags = html.find_all('h2')
# for tag in tags:
#         print(tag.text)

from bs4 import BeautifulSoup
import requests

def apstrada_lapu(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

soup = apstrada_lapu("https://www.tvnet.lv")
print(soup.head.title.text)

tags = soup.find_all('h2')
for tag in tags:
    print(tag.text)
