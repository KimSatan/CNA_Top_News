import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, InlineQueryHandler

token = 'TOKEN'
chatid = 'CHATID'


URL = 'https://www.channelnewsasia.com/news/singapore'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div', class_ = 'u-grid is-separated-by-line')
news_elems = results.find_all('div', class_ = 'grid__col-4')

top_news = []

for news_elem in news_elems:

    link = 'https://www.channelnewsasia.com/' + news_elem.find('a')['href']
    top_news.append(link)

requests.get('https://api.telegram.org/bot{}/sendMessage?chat_id=-{}&text=Top+news+from+CNA!'.format(token, chatid))

for index, news in enumerate(top_news):

    if index != len(top_news) - 1:
        base_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id=-{}&text={}'.format(token, chatid, news)
        requests.get(base_url)