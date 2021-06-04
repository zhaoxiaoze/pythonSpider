import requests
from bs4 import BeautifulSoup

#find_all 里面的方法函数
def way(tag):
    return tag.has_attr('href') and not tag.has_attr('class')
def way_detail(tag):
    return not tag.has_attr('class') and tag.name=='p'

#获取翻页
def get_Out(url,page_url):
    respon = requests.get(url)
    soup = BeautifulSoup(respon.text,'html.parser')
    pages = soup.find_all(way)
    for page in pages:
        if page.name == u'a':
            # print(page['href'])
            page_url.append(url+page['href'])
        
#获取详细页
def get_In(url,pageurl,name_list,detail_list):
    respon = requests.get(url)
    soup = BeautifulSoup(respon.text,'html.parser')
    #解析电影名称
    names = soup.find_all('h2',{'class':'m-b-sm'})
    for name in names:
        name_list.append(name.string)
    #解析电影名称对应的地址
    url_details = soup.find_all('a',{'class':'name'})
    for url_detail in url_details:
        detail_list.append(url+url_detail['href'])

#获取电影简介
def get_Content(name_list,detail_list,dict_list):
    count = 0
    for url in detail_list:
        respon = requests.get(url)
        soup = BeautifulSoup(respon.text,'html.parser')
        details = soup.find_all(way_detail) 
        for detail in details:
            if detail.string != None:
                dict_list.update({name_list[count]:detail.string})
                count = count + 1


if __name__=='__main__':
    url = 'https://ssr1.scrape.center'
    page_url = []
    name_list = []
    detail_list = []
    dict_list = {}
    get_Out(url,page_url)
    for pageurl in page_url:
        get_In(url,pageurl,name_list,detail_list)
    get_Content(name_list,detail_list,dict_list)
   

  