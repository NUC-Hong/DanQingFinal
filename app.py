from flask import Flask, request, json

import Repair1
import FaceChange
# import Repair1
import colorize
from ChangeSize import changeSizeSmall, changeSizeBig
from DrawImg import simple_multimodal_conversation_call
from VideoChangeFace import changeFunc
import delete
from PaddleGAN import paddleFunc
from expand.kuotu import kuotu
from expand.tiqukuotu import check_task_status_expand
from imgCreatVedio.creatVedio import AiCreatVedio
from imgCreatVedio.tiquVedio import tiquVedio
from oldCrackPepair.CrackPepair import CreatCrackPepair
from oldCrackPepair.tiquCrackPepair import getJpghd_url
from poster.Poster import Poster
from poster.tiquPoster import check_task_status_poster
# from chip.test111 import chinaPaint
# from clear import inference_video
# from clear import upcunet_v3
from shangchuan import upload, uploadMore, uploadVedio, uploadStyle, uploadOld
from style_transfer.baidu_style_transfer.transfer import trans
from textToImg import toImg
from xiazai import getname, xiazai, xiazaiVedio, getnameCompress
from yasuo import compress_im

app = Flask(__name__)


# 图片压缩
@app.route('/compress', methods=['POST'])
def compress():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        compress_im(name)
        name = getnameCompress(name)
        back = upload(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


# 图片尺寸变换
@app.route('/changeSize', methods=['POST'])
def SizeSmall():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        changeSizeSmall(name)

        back = upload(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


@app.route('/big', methods=['POST'])
def SizeBig():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        changeSizeBig(name)

        back = upload(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


# # 图像清晰化
# @app.route('/clear', methods=['POST'])
# def Clear():
#     if request.method == 'POST':
#         data = json.loads(request.get_data('x'))
#         x = data['x']
#
#         name = getname(x)
#         xiazai(x)
#         upcunet_v3.clear__(name)
#
#         back = upload(name)
#         delete.shanchu1(name)
#         delete.shanchu2(name)
#     return back

# # 视频清晰化
# @app.route('/videoClear', methods=['POST'])  # TO DO
# def videoClear():
#     if request.method == 'POST':
#         data1 = json.loads(request.get_data('x'))
#         x = data1['x']
#         vedioname = getname(x)
#         xiazaiVedio(x)
#         inference_video.clearV(vedioname)
#         back = uploadVedio(vedioname)
#         delete.shanchu3(vedioname)
#         delete.shanchu4(vedioname)
#     return back

# 图片上色
@app.route('/colorize', methods=['POST'])
def colorizethings():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        colorize.colorful(name)
        back = upload(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


# # 图片AI创作 水墨画风格
@app.route('/style', methods=['POST'])
def styleChange():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        trans(name)
        # paddleFunc.shuimoStlye(name)
        # back = uploadMore(name)
        # chinaPaint(name)
        back = upload(name)
        # name = name.split('.')[0]
        # name = "dataset1_" + name + "_fake.png"
        # delete.shanchu1(name)
        # delete.shanchu2(name)
        # name = "dataset1_" + name + "_real.png"
        delete.shanchu1(name)
        delete.shanchu2(name)
        # delete.shanchu1(name)
        # delete.shanchu2(name)
    return back


@app.route('/TextToImg', methods=['POST'])
def TextToImg():
    if request.method == 'POST':
        text = json.loads(request.get_data('text'))
        text = text['text']
        print(text)
        back = toImg(text)
    return back

# 图片生成诗
@app.route('/ImgToText', methods=['POST'])
def ImgToText():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']
        back = simple_multimodal_conversation_call(x)

    return back

# 图片动漫化
@app.route('/cartoon', methods=['POST'])
def turnToCar():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        paddleFunc.turnToCartoon(name)
        back = upload(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


# 图片多种风格转换
@app.route('/moreStar', methods=['POST'])
def moreStar():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        paddleFunc.starStlye(name)
        back = uploadMore(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


@app.route('/moreOcean', methods=['POST'])
def moreOcean():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        paddleFunc.oceanStlye(name)
        back = uploadMore(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


@app.route('/moreLight', methods=['POST'])
def moreLight():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        paddleFunc.lightStlye(name)
        back = uploadMore(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


@app.route('/moreCirc', methods=['POST'])
def moreCirc():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        paddleFunc.circStlye(name)
        back = uploadMore(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


# 黑白视频上色
@app.route('/videoRepair', methods=['POST'])  # TO DO
def videoRepair():
    if request.method == 'POST':
        data1 = json.loads(request.get_data('x'))
        x = data1['x']
        vedioname = getname(x)
        xiazaiVedio(x)
        paddleFunc.repairV(vedioname)
        # while(os.path.exists("output/result.mp4")):
        back = uploadVedio(vedioname)
        delete.shanchu3(vedioname)
        # delete.shanchu4(vedioname)
        delete.del_file("output")
    return back


# 图像动起来

@app.route('/motion', methods=['POST'])
def motionThings():
    if request.method == 'POST':
        data1 = json.loads(request.get_data('x'))
        data2 = json.loads(request.get_data('y'))
        x = data1['x']
        y = data2['y']

        vedioname = getname(x)
        picturename = getname(y)
        xiazaiVedio(x)
        xiazai(y)
        paddleFunc.motionPerson(picturename, vedioname)
        # while(os.path.exists("output/result.mp4")):

        back = uploadVedio(vedioname)
        delete.shanchu1(picturename)
        delete.shanchu1(picturename)
        delete.shanchu1(vedioname)
        delete.shanchu1(vedioname)
    return back


# 视频换脸
@app.route('/faceVideo', methods=['POST'])  # TO DO
def faceChangeV():
    if request.method == 'POST':
        data1 = json.loads(request.get_data('x'))
        data2 = json.loads(request.get_data('y'))
        x = data1['x']
        y = data2['y']

        vedioname = getname(x)
        picturename = getname(y)
        xiazaiVedio(x)
        xiazai(y)
        changeFunc.changeVideo(vedioname, picturename)
        # name=vedioname.split('.')[0]
        back = uploadVedio(vedioname)
        delete.shanchu1(picturename)
        delete.shanchu1(picturename)
        delete.shanchu1(vedioname)
        delete.shanchu1(vedioname)
        # delete.del_file("E:/guhua/hou/part2/finalGuHuaChuLi/output")
    return back


@app.route('/faceChange', methods=['POST'])
def faceChange():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        FaceChange.faceChange(name, "libai.jpeg")
        back = upload(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back


@app.route('/repair1', methods=['POST'])
def repair1():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        Repair1.repairV(name)
        back = upload(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back

# AI扩图
@app.route('/kuotu', methods=['POST'])
def Expand():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        name = data['x']
        print(name)
        task_id = kuotu(name)
        back = check_task_status_expand(task_id)
        print(back)
    return back

# 国风海报生成
@app.route('/Poster', methods=['POST'])
def CreatPoster():
    if request.method == 'POST':
        data = json.loads(request.get_data())
        print(data)
        text1 = data['text1']
        text2 = data['text2']
        text3 = data['text3']
        text4 = data['text4']
        text5 = data['text5']
        print(text1,text2,text3,text4,text5)
        task_id = Poster(text1,text2,text3,text4,text5)
        print(task_id)
        back=check_task_status_poster(task_id)
        print(back)
    return back

# 图生视频
@app.route('/ImgCreatVedio', methods=['POST'])
def ImgCreatVedio():
    if request.method == 'POST':
        data = json.loads(request.get_data())
        name = data['x']
        text = data['y']
        print(name)
        print(text)
        id=AiCreatVedio(name,text)
        print(id)
        back=tiquVedio(id)
    return back

# 裂痕修复
@app.route('/OldCrackRepair', methods=['POST'])
def OldCrackRepair():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        name = data['x']
        print(name)
        pid = CreatCrackPepair(name)
        back = getJpghd_url(pid)
    return back

if __name__ == '__finalGuHua__':
    app.run()
