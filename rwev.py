import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from lxml import html

url_input = input("Input url here:  ")
request_to_url = requests.get(url_input)
tree = html.fromstring(request_to_url.content)
recipe = tree.xpath("//*[@class='text show-more__control']/text()")
str_sent = ''.join(recipe)
# print(str_sent)

word_cloud = WordCloud(width=5000, height=4000, random_state=1, background_color='black', colormap='Pastel1',
                       collocations=False, stopwords=STOPWORDS).generate(str_sent)
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()



