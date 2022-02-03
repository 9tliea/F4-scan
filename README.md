# F4-scan
一款子域名爆破,信息收集,融合了fofa,zoomeye,C段扫描的红队工具,帮助您加大对暴露面资产的披露发现,是挖洞必备神器

安装:
1.https://github.com/9tliea/F4-scan.git(克隆文件)

2.安装模块:pip3 install request

3.运行程序:python3 main.py

4.打开main.py进行配置
  配置分两部分:
  (1).main.py第13行,更改存放字典的地址,具体添加子域名请参照data.txt一行一个
  (2).main.py第27行更改输出文件,要用双斜杠哦
