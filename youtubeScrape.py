#! python3
# youtubeScrape.py - Scrapes video titles from youtube trending feed

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import sys

options = Options()
options.headless = True
url = webdriver.Firefox(options=options, executable_path=r'C:\Utilities\geckodriver.exe')
url.get('https://www.youtube.com/feed/trending')

element = url.find_elements(By.XPATH, "//a[@id='video-title']")
viewEle = url.find_elements(By.XPATH, "//span[@class='style-scope ytd-video-meta-block']")

t = []
v = []

for title in element:
    t.append(title.text)

for view in viewEle:
    v.append(view.text)

url.close()
vfin = v[0::2]   # Creates new list from v starting at index 0 and stepping over twice

for i in range(len(t)):
    print('Video Title: %s - Views: %s' % (t[i], vfin[i]))

ex = input('When you are done type exit.\n')
if ex == 'exit':
    sys.exit()
