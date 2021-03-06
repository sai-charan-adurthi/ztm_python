import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    """[summary]

    Args:
        hnlist ([type]): [description]
    """
    return sorted(hnlist, key= lambda key: key['votes'], reverse=True)

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        
        if len(vote):
            points=int(vote[0].getText().replace(' points', ''))
            hn.append({'title': title, 'link': href, 'votes': points})
    
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))