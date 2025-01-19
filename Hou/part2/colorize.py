import base64
import requests


def colorful(img):
    # r = requests.post(//deepai要花钱
    #     "https://api.deepai.org/api/colorizer",
    #     files={
    #         'image': open('static/image/' + img, 'rb'),
    #     },
    #     headers={'api-key': '431809a6-e7a6-4acc-a347-bc219866db85'}
    # )
    # print(r.json())
    # print(r.json()['output_url'])

    # import urllib.request
    #
    # # 网络上图片的地址
    # img_src = r.json()['output_url']
    #
    # # 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
    # urllib.request.urlretrieve(img_src, 'static/new_image/' + img)


    # 百度上色接口
    request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/colourize"
    f = open('static/image/' + img, 'rb')
    img1 = base64.b64encode(f.read())
    params = {"image": img1}
    access_token = '24.29023e37773ac45763a0df21d80e4393.2592000.1733033694.282335-56658288'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())

    # 从响应中提取Base64编码的图片数据
    base64_image_data = response.json()['image']

    # 解码Base64数据为二进制数据
    binary_image_data = base64.b64decode(base64_image_data)

    # 指定要保存的文件名和路径
    output_file_path = 'static/new_image/' + img  # 或者根据图片类型使用其他扩展名，如.png

    # 将二进制数据写入文件
    with open(output_file_path, 'wb') as file:
        file.write(binary_image_data)

    print(f"图片已成功保存到 {output_file_path}")



