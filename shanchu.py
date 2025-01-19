import os




def delete(imagename):

    # rootdir="static/image/"
    rootdir="static/image/"

    filelist = os.listdir(rootdir)
    for file in filelist:
        if imagename in file:
            del_file = rootdir + file #当代码和要删除的文件不在同一个文件夹时，必须使用绝对路径
            os.remove(del_file)#删除文件
            print("已经删除：",del_file)

