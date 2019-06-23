import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
'''
ua = UserAgent()

print("chrome-->" + UserAgent().chrome)#(ua.random)
print("random1-->" + ua.random)
print("random2-->" + ua.random)
print("random3-->" + ua.random)
'''

'''
url = "http://baidu.com"
headers = {"User-Agent":ua.random}#User-Agent大小写敏感

response = requests.get(url = url, headers = headers)
response.raise_for_status()

print(response.text)#响应体内容
print(response.status_code)#响应状态信息
print(response.headers)#响应头信息
'''

#获取网页内容
def getHTMLText(url,headers):
    try:        
        response = requests.get(url = url, headers = headers)
        response.raise_for_status#如果状态不是200(正常状态)，引发HTTPError异常
        response.encoding = response.apparent_encoding#获取目标页面的字符集编码并赋值，这样输出text便无乱码
        return response.text
    except:
        return("ERROR")


if __name__ == "__main__":

    ua = UserAgent()

    url = "http://baidu.com"
    headers = {"user-agent":ua.random}

    htmltest = getHTMLText(url,headers)

    #beautifulsoup4
    bs = BeautifulSoup(htmltest, "html.parser")






    print(url + "的网页内容：\r\n\r\n" + htmltest)

