from bs4 import BeautifulSoup

soup = BeautifulSoup(open('result.html'),"html.parser")

try:
    headerTitle = soup.select('.u')[0].get_text()
except IndexError:
    headerTitle = None
formatText = (headerTitle or '') + '\n'

newsStr = ""
newsElement = soup.select('.news-wrap > .line')
for div in newsElement:
    news = div.get_text() + '\n'
    newsStr += news
formatText += newsStr + '\n'

try:
    historyTitle = soup.select('.u')[1].get_text()
except IndexError:
    historyTitle = None
formatText += (historyTitle or '') + '\n'

index = 0
history = ''
for a in soup.select('.history-wrap > .line a'):
    index += 1
    history += str(index) + '. ' + a.get_text() + '\n'
formatText += history + '\n'

try:
    progress = '时间进度条: ' + soup.select('.progress-bar')[0].get_text()
except IndexError:
    progress = None
formatText += (progress or '') + '\n'

try:
    progress_text = soup.select('.line')[-1].get_text()
except IndexError:
    progress_text = None
formatText += (progress_text or '') + '\n'

filename = 'result.txt'
with open(filename, 'w') as file:
    file.write(formatText)
