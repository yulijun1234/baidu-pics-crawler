import requests
import time
import re

headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'img2.imgtn.bdimg.com',
'If-Modified-Since':'Thu, 01 Jan 1970 00:00:00 GMT',
'If-None-Match':'7deb005eb9d3f5f0312c43186a7b3dae',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',}

def save_pic(url):
    for i in range(10):
        try:
            pic = requests.get(url,headers=headers)
            break
        except:
            if i==9:
                print "request failed, skip"
                return 0
            print 'request again'
            continue
    name = str(time.time()).replace('.','_')
    filepath ='plants/'+name+'.jpg'
    file = open(filepath,'wb')
    file.write(pic.content)
    file.close()
    print 'save '+name+' pic'


def main():
    links = []
    for i in range(5):
        #request_url = 'http://image.baidu.com/search/index?tn=baiduimage&word=%E6%9C%88%E5%AD%A3%E5%9B%BE%E7%89%87&pn='+str(30*(i+1))+'&rn=30'
        request_url = 'http://image.baidu.com/search/index?tn=baiduimage&word=紫甘蓝&pn='+str(30*(i+1))+'&rn=30'
        a= requests.get(request_url)
        res=re.compile('middleURL":"(.+?).jpg"').findall(a.content)
        if res:
            for link in res:
                link_full = link+'.jpg"'
                print link_full
                save_pic(link_full)
if __name__=='__main__':
    main()