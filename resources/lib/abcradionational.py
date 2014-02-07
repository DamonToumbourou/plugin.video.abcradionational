import requests
from BeautifulSoup import BeautifulSoup
import re

ABC_URL= "http://abc.net.au/radionational/rntv"

def get_podcasts():
    """
    returns playable podcasts links from ABC website
    """
    url = ABC_URL
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    
    urls = soup.findAll('a' , 'external')
    titles = soup.findAll('h3', 'title')
    thumbs = soup.findAll('img')
    
    thumb_sec = thumbs[1:36]
    thumb_out = []
    for thumb in thumb_sec:
        thumb_out.append(thumb['src'])
    print len(thumb_out)

    title_out = []
    for title in titles:
        title_out.append(re.sub('&#039;', "'",title.text))
    print len(title_out)

    path = []
    for u in urls:
        if 'youtube' in str(u):
            path.append(u['href'])

    path_out = []
    for i in path:
        path_out.append(i[-11:])
    
    output = []
    for x in range(len(path_out)):
        items = {
            'title': title_out[x],
            'thumb': thumb_out[x],
            'url': path_out[x],
        } 
        output.append(items)

    return output

print get_podcasts()


