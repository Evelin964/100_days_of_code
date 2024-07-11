from bs4 import BeautifulSoup
import requests 

url = 'https://news.ycombinator.com/news'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')

athing_class = soup.find_all( class_='athing',id=True)
subtext_class = soup.find_all( class_='score')

athing_items = [(item.get('id'), 
                 item.find('span', class_='titleline').find('a').get('href'), 
                 item.find('span', class_='titleline').find('a').text) 
                for item in soup.find_all('tr', class_='athing')]

subtext_class_scores = [(item.get('id'), item.text) for item in subtext_class]

subtext_class_scores = [(item.get('id').replace('score_', ''), item.text) for item in subtext_class]
max_values  = []
max_values = [int(subtext_class_scores[1].replace(' points', '')) for subtext_class_scores in subtext_class_scores]
subtext_class_scores = [(subtext_class_scores[0], int(subtext_class_scores[1].replace(' points', ''))) for subtext_class_scores in subtext_class_scores]

max_nr = max(max_values)
index_max = max_values.index(max_nr)
max_id=subtext_class_scores[index_max][0]

for i in range(0, len(athing_items)):
    if athing_items[i][0] == max_id:
        print(athing_items[i][0])
        print(athing_items[i][1])
        print(athing_items[i][2])
        print(subtext_class_scores[index_max][1])


