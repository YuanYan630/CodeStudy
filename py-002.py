#https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/515/515-bigskin-1.jpg

import os
import requests
from fake_useragent import UserAgent

#获取网页内容(json形式列表)
def getHTMLList(url,headers):
    try:        
        response = requests.get(url = url, headers = headers)
        response.raise_for_status#如果状态不是200(正常状态)，引发HTTPError异常
        response.encoding = response.apparent_encoding#获取目标页面的字符集编码并赋值，这样输出text便无乱码
        return response.json()
    except:
        return("ERROR")


if __name__ == "__main__":

    ua = UserAgent(verify_ssl=False)

    url = 'http://pvp.qq.com/web201605/js/herolist.json'
    headers = {"user-agent":ua.random}

    hero_list = getHTMLList(url,headers)

    # 提取英雄名字和数字
    hero_name=list(map(lambda x:x['cname'], hero_list)) 

    hero_number=list(map(lambda x:x['ename'], hero_list))

    #英雄皮肤的固定前缀
    h_l='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'


    num = 0
    # 逐一遍历英雄
    for i in hero_number:        
    # 逐一遍历皮肤，此处假定一个英雄最多有15个皮肤
        for sk_num in range(15):
            hsl = h_l + str(i)+'/'+str(i)+'-bigskin-'+str(sk_num)+'.jpg'

            hl = requests.get(hsl)

    # 将图片保存下来，并以"英雄名称_皮肤序号"方式命名
            with open(hero_name[num] + str(sk_num) + '.jpg', 'wb') as f:
            #f.write(@"C:\Users\vicky\Desktop\mobile legend"+ hl.content)
                f.write(hl.content)
    #1.增加文件大小判断，若文件大小为0，不保存
    #2.修改保存路径
    #3.支持保存并提示：暂时一次性保存并提示，后续修改成分段保存+提示
        num += 1

    print("ok")