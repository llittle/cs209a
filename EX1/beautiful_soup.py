'''
Going through the Quick Start guide of the Beautiful Soup
documentation foud here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print('whole html doc is')
print(soup.prettify())
print('Title is: ')
print(soup.title)
print('Title name is: ')
print(soup.title.name)
print('Title string is: ')
print(soup.title.string)
print('Find all "a" is: ')
print(soup.find_all('a'))
