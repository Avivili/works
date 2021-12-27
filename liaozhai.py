# -*- coding=utf-8 -*-
import os.path

from bs4 import BeautifulSoup
import requests
import sys
import time
from tqdm import tqdm



def get_urls(filename):

    url = 'http://liaozhai.5000yan.com/'  # 获取主页
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = res.text

    bf_article = BeautifulSoup(html, 'html.parser')  # 创建bs4对象

    bf_links = bf_article.select('article>div>a')   #获取所有文章链接列表
    total_pro = tqdm(total=len(bf_links))  #获取进度条

    for bf_html in bf_links:
        s_url = bf_html['href']
        s_res = requests.get(s_url)
        s_res.encoding = 'utf-8'
        s_soup = BeautifulSoup(s_res.text, 'html.parser')  #创建每篇文章的bs4对象

        headline = s_soup.select('header>h2')[0].text
        title = s_soup.select('header>p')[0].text
        context = s_soup.select('.grap')[0].text.replace('\xa0', '')

        with open(filename, 'a', encoding='utf-8', errors='ignore') as f:
            f.write('\n' + headline + title + context)
        time.sleep(0.1)
        total_pro.update(1) #update进度条
    total_pro.close()  #关闭进度条更新

def main():
    t1 = time.time()
    filename=input('enter txt filename to save the crawling content:')
    if os.path.exists(filename):
        filename=input('file exists,please use another filename:')
    if not  filename.endswith('.txt'):
        filename=input('please use .txt file,enter name again:')
    print('crawling begins....')
    get_urls(filename)
    t2 = time.time()
    print('totally used {:.2f}s'.format(t2 - t1)) #计算爬取文件所用时长
    input('press any key to exit...')

if __name__ == "__main__":
    main()


