# -*- coding=utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import pymysql
import re

import time
def get_urls():
    url='http://liaozhai.5000yan.com/'  #获取主页
    res=requests.get(url)
    res.encoding='utf-8'
    html=res.text
    # links=[]
    bf_article=BeautifulSoup(html,'html.parser')  #创建bs4对象
    #获取所有article标签
    bf_htmls=bf_article.find_all('article',class_="block block--inset block--list")

    return bf_htmls #返回html中包含article的列表

        



def get_each_content(bf_link,file):
        link=bf_link['href']  #获取每个故事超链接
        resl=requests.get(link) #获取故事所在网页内容
        resl.encoding='utf-8'
        newHtml=BeautifulSoup(resl.text,'html.parser') #对该网页创建bs4对象
        section=newHtml.select('section')#获取故事所在标签及内容
        head=section[0].header.h2.text #获取故事名
        subhead=section[0].header.p.text #获取故事副标题
        content=section[0].div.text.replace(' ','') #获取故事内容
        file.write('\n\n'+head+subhead+content) #将以上获取内容写入txt文件

def get_content():
    bf_htmls=get_urls() #调用函数，获取article列表
    #打开一个txt文档，不存在的话会自动创建
    with open(r'liaozhai.txt','w',encoding='utf-8') as file: 
        for bf_html in bf_htmls:
            bf_head=bf_html.find('h2',itemprop="headline").text #获取章节序号 ex:卷一
            # print(bf_head)
            file.write('\n'+bf_head+'\n') #写入章节序号
            bf_links=bf_html.find_all('a')  #获取本章节下所有故事链接
            for bf_link  in bf_links:
                get_each_content(bf_link,file)




if __name__=='__main__':
    print('test start,please wait for a while')
    t1=time.time()
    get_content()
    t2=time.time()
    print('总共用时：%ss'%(t2-t1))


