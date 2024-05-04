from bs4 import BeautifulSoup

soup = BeautifulSoup(open('result.html'),"html.parser")
titleArr = soup.select('.u')
#标题
if titleArr:
    headerTitle = titleArr[0].get_text()
else:
    headerTitle = 'Default Header Title'
formatText = headerTitle + '\n'

#新闻
newsStr = ""
newsElement = soup.select('.news-wrap > .line')
for div in newsElement:
	news = div.get_text() + '\n'
	newsStr += news
formatText += newsStr + '\n'

#历史上的今天
historyTitleArr = soup.select('.u')
if len(historyTitleArr) > 1:
    historyTitle = historyTitleArr[1].get_text()
else:
    historyTitle = 'Default History Title'
formatText += historyTitle + '\n'

historyArr = soup.select('.history-wrap > .line a')
index = 0
history = ''

for a in historyArr:
    index += 1
    history += str(index) + '. ' + a.get_text() + '\n'

formatText = formatText + history + '\n'

#时间进度条
progressArr = soup.select('.progress-bar')
if progressArr:
    progress = '时间进度条: ' + progressArr[0].get_text()
else:
    progress = '时间进度条: N/A'
progress_text = soup.select('.line')[-1].get_text()
formatText += progress + '\n'
formatText += progress_text + '\n'
filename = 'result.txt'
with open (filename,'w') as file:
    file.write(formatText)   






