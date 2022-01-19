import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")

# we can select the scores for each news article by selecting the 'score' class (. means class)
print(soup.select(".score"))

# we can also get the links to each news article using the titlelink class
print(soup.select(".titlelink")[0])

# so we can get the news articles and their votes
links = soup.select(".titlelink")
scores = soup.select(".score")

# then subreference the scores to get the value
print(scores[0].get("id"))

# however, new articles won't have votes, so the links and scores will have different array lengths
# instead, we can reference the 'subtext' field of links and then the score element from that in our function
scores = soup.select(".subtext")


def sort_stores_by_votes(hnlist):
    # return a sorted dictionary list
    return sorted(hnlist, key=lambda k: k['score'], reverse=True)


def create_custom_hacker_news(links, scores, cutoff=99):
    hn = []
    for idx, item in enumerate(links):
        # get the titles of each news article
        title = links[idx].getText()
        # get all the links, or default to None if broken
        href = links[idx].get('href', None)
        # get the score from our subtext field
        vote = scores[idx].select(".score")
        # if a score exists (ie length is not none)
        if len(vote):
            # convert to int, removing the word 'points'
            score = int(vote[0].getText().replace(" points", ""))
            if score > cutoff:
                # append as dictionary
                hn.append({'title': title, 'link': href, 'score': score})
    return sort_stores_by_votes(hn)


# return the article titles and links where the score is over 100
pprint.pprint(create_custom_hacker_news(links, scores))


# then extend this to cover more than just the first page
response = requests.get("https://news.ycombinator.com/news")
response2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(response.text, "html.parser")
soup2 = BeautifulSoup(response2.text, "html.parser")

links = soup.select(".titlelink")
scores = soup.select(".subtext")
links2 = soup2.select(".titlelink")
scores2 = soup2.select(".subtext")

links = links + links2
scores = scores + scores2

pprint.pprint(create_custom_hacker_news(links, scores))

# if in future want to explore larger web scraping projects, could look at scrapy (https://scrapy.org)
# scrapy is a framework rather than just a module, designed for large scale web scraping
