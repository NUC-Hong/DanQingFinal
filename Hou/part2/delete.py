# import os
# rootdir="F:\数据分析\OpenCV+TensorFlow入门人工智能图像处理"
# filelist=os.listdir(rootdir)
# for f in filelist:
#     print(f)

import os
def shanchu1(imagename):
    rootdir="static/image/"
    filelist=os.listdir(rootdir)
    for file in filelist:
        if imagename in file:
            del_file = rootdir + file #当代码和要删除的文件不在同一个文件夹时，必须使用绝对路径
            os.remove(del_file)#删除文件
            print("已经删除：",del_file)

def shanchu2(imagename):
    rootdir="static/new_image/"
    filelist=os.listdir(rootdir)
    for file in filelist:
        if imagename in file:
            del_file = rootdir + file #当代码和要删除的文件不在同一个文件夹时，必须使用绝对路径
            os.remove(del_file)#删除文件
            print("已经删除：",del_file)

def shanchu3(imagename):
    rootdir="static/vedio/"
    filelist=os.listdir(rootdir)
    for file in filelist:
        if imagename in file:
            del_file = rootdir + file #当代码和要删除的文件不在同一个文件夹时，必须使用绝对路径
            os.remove(del_file)#删除文件
            print("已经删除：",del_file)

def shanchu4(imagename):
    rootdir="output/"
    filelist=os.listdir(rootdir)
    for file in filelist:
        if imagename in file:
            del_file = rootdir + file #当代码和要删除的文件不在同一个文件夹时，必须使用绝对路径
            os.remove(del_file)#删除文件
            print("已经删除：",del_file)


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)