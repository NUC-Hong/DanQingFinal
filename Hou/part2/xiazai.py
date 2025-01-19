import requests



def getname(url):
    name = url.split('/')[-1]
    print("成功获取名字")
    return name

def getnameCompress(url):
    name = url.split('.')[0]
    print("成功获取名字")
    return name+".jpg"

def getnameStyle(url):
    name = url.split('/')[-1].split('.')[0]
    print("成功获取名字")
    return "dataset1_"+ name +"_fake.png"

def xiazai(url):
    # url = 'https://636c-cloud1-0gjs3867092b42e0-1312009154.tcb.qcloud.la/game/1654601366242.png'
    # name =url.split('/')[-1]
    # print(name)
    name = getname(url)
    image = requests.get(url)
    # 在目标路径创建相应文件
    f = open('static/image/' + name, 'wb')
    # 将下载到的图片数据写入文件
    f.write(image.content)
    f.close()
    print("下载完成")

def xiazaiVedio(url):
    # url = 'https://636c-cloud1-0gjs3867092b42e0-1312009154.tcb.qcloud.la/game/1654601366242.png'
    # name =url.split('/')[-1]
    # print(name)
    name = getname(url)
    image = requests.get(url)
    # 在目标路径创建相应文件
    f = open('static/vedio/' + name, 'wb')
    # 将下载到的图片数据写入文件
    f.write(image.content)
    f.close()
    print("下载完成")




