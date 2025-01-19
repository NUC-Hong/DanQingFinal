import requests

import simplejson

import json

import base64

# wtt
# 79FjHAC_u44cwyxZYlMUS6u_WdUPEzhd
# d95EKjbhAHPATbXUJc3n3Rh5fvfhZiwO

# LfiyiJZle2jGn8z2RS_ghtwR7791wOKo
# sK8Tf_FtDezfkCHrnf99Cf-Y_7eq4Xlw
# 第一步，获取人脸关键点，代码如下说述：

def find_face(imgpath):
    print("finding")

    http_url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'

    data = {"api_key": '79FjHAC_u44cwyxZYlMUS6u_WdUPEzhd',

            "api_secret": 'd95EKjbhAHPATbXUJc3n3Rh5fvfhZiwO', "image_url": imgpath, "return_landmark": 1}

    files = {"image_file": open(imgpath, "rb")}

    response = requests.post(http_url, data=data, files=files)

    req_con = response.content.decode('utf-8')
    print(req_con)

    req_dict = json.JSONDecoder().decode(req_con)

    this_json = simplejson.dumps(req_dict)
    print(this_json)

    this_json2 = simplejson.loads(this_json)

    faces = this_json2['faces']

    list0 = faces[0]

    rectangle = list0['face_rectangle']

    # print(rectangle)

    return rectangle


# 第二步，换脸，其中图片的大小应不超过2M，代码如下所述：

# number表示换脸的相似度

def merge_face(image_url_1, image_url_2, image_url, number):
    ff1 = find_face(image_url_1)

    ff2 = find_face(image_url_2)

    rectangle1 = str(str(ff1['top']) + "," + str(ff1['left']) + "," + str(ff1['width']) + "," + str(ff1['height']))

    rectangle2 = str(ff2['top']) + "," + str(ff2['left']) + "," + str(ff2['width']) + "," + str(ff2['height'])

    url_add = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface"

    f1 = open(image_url_1, 'rb')

    f1_64 = base64.b64encode(f1.read())

    f1.close()

    f2 = open(image_url_2, 'rb')

    f2_64 = base64.b64encode(f2.read())

    f2.close()

    data = {"api_key": '79FjHAC_u44cwyxZYlMUS6u_WdUPEzhd', "api_secret": 'd95EKjbhAHPATbXUJc3n3Rh5fvfhZiwO',

            "template_base64": f1_64, "template_rectangle": rectangle1,

            "merge_base64": f2_64, "merge_rectangle": rectangle2, "merge_rate": number}

    response = requests.post(url_add, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = json.JSONDecoder().decode(req_con)

    result = req_dict['result']

    imgdata = base64.b64decode(result)

    file = open(image_url, 'wb')

    file.write(imgdata)

    file.close()


# image1 = r"E:\PythonThing\Project\project1\FaceDetec\huat.jpg"
#
# image2 = r"E:\PythonThing\Project\project1\FaceDetec\mayun2.jpg"
#
# image = r"E:\PythonThing\Project\project1\FaceDetec\merge.jpg"
# def test():
#     image1 = r"E:\PythonThing\Project\project1\FaceDetec\jjm.jpg"
#
#     image2 = r"E:\PythonThing\Project\project1\FaceDetec\mama.jpg"
#
#     image = r"E:\PythonThing\Project\project1\FaceDetec\merge.jpg"
#
#     merge_face(image2, image1, image, 90)


# if __name__ == "__main__":
#     test()
def faceChange(img1, img2):
    image1 = r"static/image/" + img1

    image2 = r"pictures/" + img2

    image = r"static/new_image/" + img1

    merge_face(image2, image1, image, 90)


# faceChange(".jpg", "E:/PythonThing/flaskProject1(1)/mengna.jpg")
