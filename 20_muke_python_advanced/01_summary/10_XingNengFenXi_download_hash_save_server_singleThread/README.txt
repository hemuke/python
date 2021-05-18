1）下载模块 IO密集模块
2）哈希模块 CPU密集模块
3）存储模块 IO密集模块
4）调度模块

调度模块 控制 上面三个模块

pip3 freeze > requirements.txt
如果安装报错 找不到 Error file
vim requirements.txt
:%s#@ file:///.*/work##g

pip3 install -r ./requirements.txt


这3个模块是有依赖关系的 各个模块是串行的
改造
模块内并行
