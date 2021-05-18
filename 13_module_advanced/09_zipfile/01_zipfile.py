import zipfile

# 创建压缩包
f = zipfile.ZipFile("abc.zip", mode="w")
f.write("x1.txt")
f.write("x2.txt")
f.close()

# 如何进行解压缩
f = zipfile.ZipFile("abc.zip", mode="r")
# 直接全部解压缩
f.extractall("zip_dir/abc")

# 一个个取
for name in f.namelist():
    f.extract(name, "zip_dir/hehe")
