import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()

url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的

def saveFile(data):
    save_path = 'D:\temp.out'
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()

queue.append(url)
cnt = 0

while queue:
  url = queue.popleft()  # 队首元素出队
  visited |= {url}  # 标记为已访问

  print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
  cnt += 1
  urlop = urllib.request.urlopen(url, timeout = 2)
  if 'html' not in urlop.getheader('Content-Type'):
    continue

  # 避免程序异常中止, 用try..catch处理异常
  try:
    data = urlop.read().decode('utf-8')
  except:
    continue

  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  linkre = re.compile('href="(.+?)"')
  for x in linkre.findall(data):
    if 'http' in x and x not in visited:
      queue.append(x)
      print('加入队列 --->  ' + x)

  saveFile(data)