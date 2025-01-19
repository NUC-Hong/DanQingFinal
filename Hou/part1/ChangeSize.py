import time

import cv2
from cv2 import dnn_superres


#
# def show_cv(name, img):
#     cv2.imshow(name, img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
def changeSizeSmall(imgname):


    # img = cv2.imread('dim')
    # img=cv2.resize(img,(295,413), interpolation=cv2.INTER_AREA)
    # show_cv("img",img)
    # resized = cv2.resize(img, (443, 626), interpolation=cv2.INTER_AREA)
    # show_cv("resize",resized)
    sr = dnn_superres.DnnSuperResImpl_create()
    # 读图
    imgFile = "static/image/" + imgname
    img = cv2.imread(imgFile)

    # img = cv2.resize(img, (295, 413), interpolation=cv2.INTER_AREA)
    # show_cv("img", img)
    # 读取模型
    sr.readModel("Models/ESPCN_x4.pb")
    # 设定算法和放大比例
    sr.setModel("espcn", 4)
    # 将图片加载入模型处理，获得超清晰度图片
    print("处理图片中...\n")
    t0 = time.perf_counter()

    upScalePic = sr.upsample(img)

    print("处理图片完成\n")
    # print(time.perf_counter() - t0)

    # 将图片放大
    # justBigPic = cv2.resize(img, (390, 567), interpolation=cv2.INTER_AREA)
    upScalePic = cv2.resize(upScalePic, (0,0), fx=1/7,fy=1/7,interpolation=cv2.INTER_AREA)

    # 输出
    filename = "static/new_image/" + imgname
    # cv2.imwrite("justBigPic.jpg", justBigPic)
    cv2.imwrite(filename, upScalePic)
    # show_cv("just", justBigPic)


    # cv2.imwrite(filename, upScalePic)
    # show_cv("upScale", upScalePic)
    print("输出图片完成\n")


def changeSizeBig(imgname):


    # img = cv2.imread('dim')
    # img=cv2.resize(img,(295,413), interpolation=cv2.INTER_AREA)
    # show_cv("img",img)
    # resized = cv2.resize(img, (443, 626), interpolation=cv2.INTER_AREA)
    # show_cv("resize",resized)
    sr = dnn_superres.DnnSuperResImpl_create()
    # 读图
    imgFile = "static/image/" + imgname
    img = cv2.imread(imgFile)

    # img = cv2.resize(img, (295, 413), interpolation=cv2.INTER_AREA)
    # show_cv("img", img)
    # 读取模型
    sr.readModel("Models/ESPCN_x4.pb")
    # 设定算法和放大比例
    sr.setModel("espcn", 4)
    # 将图片加载入模型处理，获得超清晰度图片
    print("处理图片中...\n")
    t0 = time.perf_counter()

    upScalePic = sr.upsample(img)

    print("处理图片完成\n")
    # print(time.perf_counter() - t0)

    # 将图片放大
    # justBigPic = cv2.resize(img, (390, 567), interpolation=cv2.INTER_AREA)
    upScalePic = cv2.resize(upScalePic, (0,0), fx=1/2,fy=1/2,interpolation=cv2.INTER_AREA)

    # 输出
    filename = "static/new_image/" + imgname
    # cv2.imwrite("justBigPic.jpg", justBigPic)
    cv2.imwrite(filename, upScalePic)
    # show_cv("just", justBigPic)


    # cv2.imwrite(filename, upScalePic)
    # show_cv("upScale", upScalePic)
    print("输出图片完成\n")

