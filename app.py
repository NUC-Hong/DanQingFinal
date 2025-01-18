import json

from flask import Flask, json, request

import delete
from ChangeSize import changeSizeSmall, changeSizeBig
from clear import upcunet_v3, inference_video
from xiazai import getname, xiazai, getnameCompress, xiazaiVedio
from yasuo import compress_im
from shangchuan import upload, uploadOld, uploadMore, uploadVedio

app = Flask(__name__)

# 功能1：图片压缩

# @app.route('/part1/compress', methods=['POST'])
# def compress():
#     if request.method == 'POST':
#         data = json.loads(request.get_data('x'))
#         x = data['x']
#
#         name = getname(x)
#         xiazai(x)
#         compress_im(name)
#         name = getnameCompress(name)
#         back = upload(name)
#         delete.shanchu1(name)
#         delete.shanchu2(name)
#     return back
#
# #功能2：图片尺寸变换
#
# @app.route('/changeSize', methods=['POST'])
# def SizeSmall():
#     if request.method == 'POST':
#         data = json.loads(request.get_data('x'))
#         x = data['x']
#
#         name = getname(x)
#         xiazai(x)
#         changeSizeSmall(name)
#
#         back = upload(name)
#         delete.shanchu1(name)
#         delete.shanchu2(name)
#     return back
#
#
# @app.route('/big', methods=['POST'])
# def SizeBig():
#     if request.method == 'POST':
#         data = json.loads(request.get_data('x'))
#         x = data['x']
#
#         name = getname(x)
#         xiazai(x)
#         changeSizeBig(name)
#
#         back = upload(name)
#         delete.shanchu1(name)
#         delete.shanchu2(name)
#     return back
#
# 功能3：图像清晰化

@app.route('/part1/clear', methods=['POST'])
def Clear():
    if request.method == 'POST':
        data = json.loads(request.get_data('x'))
        x = data['x']

        name = getname(x)
        xiazai(x)
        upcunet_v3.clear__(name)

        back = upload(name)
        delete.shanchu1(name)
        delete.shanchu2(name)
    return back

#
# 功能9：视频清晰化

@app.route('/part1/videoClear', methods=['POST'])  # TO DO
def videoClear():
    if request.method == 'POST':
        data1 = json.loads(request.get_data('x'))
        x = data1['x']
        vedioname = getname(x)
        xiazaiVedio(x)
        inference_video.clearV(vedioname)
        back = uploadVedio(vedioname)
        delete.shanchu3(vedioname)
        delete.shanchu4(vedioname)
        print(back)
    return back

if __name__ == '__guHuaOne__':
    app.run()
