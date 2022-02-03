#开发者:9tlie
#github:https://github.com/9tliea
#开发时间:2022年2月
import requests
import time
t=0.85
website=input("输入url:")
time.sleep(t)
print("人类的伟大是勇气的伟大,人类的赞歌是勇气的赞歌!")
time.sleep(t)
print("我将带着"+website+"远航,喝杯茶放松一下吧,结果马上就好")
time.sleep(t)
with open("C:/Users/9t/Desktop/F4-scan/data.txt", "r") as f: #字典地址(单斜杠更改)
    data = f.readlines()
    #print(data)
    s=[x.strip() for x in data if x.strip()!='']
    #print(s)
    for subline in s:
        new_shuline='http://'+subline+'.'+website
        #print(new_shuline)
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        try:
          r=requests.get(url=new_shuline,timeout=0.5,headers=headers)
          url_code = r.status_code
          url_code == 200
          print("[*]"+new_shuline+",访问成功")
          with open('C:\\Users\\9t\Desktop\\F4-scan\\a.txt','a',encoding='utf-8') as f: #输出结果存放地址和文件名(更改时要双斜杠)
            f.write(new_shuline)
            f.write('\n')
            f.close()
        except:
          print("[*]失败")

print("跑完啦,结果已生成!")          
        




    