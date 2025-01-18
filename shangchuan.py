# 上传文件
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


def upload(imgname):
    imgFile = "static/new_image/" + imgname
    # imgFile = imgname
    secret_id = 'AKIDJZqCUfheTBlDXficObcYM2iT8xrkeSC0'  # 替换为用户的 secretId
    secret_key = 'vmYCnUA6AEKYknnr8Jc6jM1b9gKvQzT0'  # 替换为用户的 secretKey
    region = 'ap-shanghai'  # 替换为用户的 Region

    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
    client = CosS3Client(config)

    response = client.upload_file(
        Bucket='guhua-buc-1324634892',
        LocalFilePath=imgFile,  # 本地文件的路径
        Key=imgname,  # 上传到桶之后的文件名
    )
    # 生成URL
    url = client.get_object_url(
        Bucket='guhua-buc-1324634892',
        Key=imgname
    )
    print(url)
    return url

def uploadOld(imgname):
    imgFile = "static/new_image/final_output/" + imgname
    # imgFile = imgname
    secret_id = 'AKIDJZqCUfheTBlDXficObcYM2iT8xrkeSC0'  # 替换为用户的 secretId
    secret_key = 'vmYCnUA6AEKYknnr8Jc6jM1b9gKvQzT0'  # 替换为用户的 secretKey
    region = 'ap-shanghai'  # 替换为用户的 Region

    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
    client = CosS3Client(config)

    response = client.upload_file(
        Bucket='guhua-buc-1324634892',
        LocalFilePath=imgFile,  # 本地文件的路径
        Key=imgname,  # 上传到桶之后的文件名
    )
    # 生成URL
    url = client.get_object_url(
        Bucket='guhua-buc-1324634892',
        Key=imgname
    )
    print(url)
    return url


def uploadStyle(imgname):
    imgname=imgname.split('.')[0]
    imgFile = "static/new_image/" +"dataset1_"+  imgname+"_fake.png"
    # imgFile = imgname
    secret_id = 'AKIDJZqCUfheTBlDXficObcYM2iT8xrkeSC0'  # 替换为用户的 secretId
    secret_key = 'vmYCnUA6AEKYknnr8Jc6jM1b9gKvQzT0'  # 替换为用户的 secretKey
    region = 'ap-shanghai'  # 替换为用户的 Region

    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
    client = CosS3Client(config)

    response = client.upload_file(
        Bucket='guhua-buc-1324634892',
        LocalFilePath=imgFile,  # 本地文件的路径
        Key=imgname,  # 上传到桶之后的文件名
    )
    # 生成URL
    url = client.get_object_url(
        Bucket='guhua-buc-1324634892',
        Key=imgname
    )
    print(url)
    return url

def uploadMore(imgname):
    imgFile = "static/new_image/LapStyle/" + imgname
    # imgFile = imgname
    secret_id = 'AKIDJZqCUfheTBlDXficObcYM2iT8xrkeSC0'  # 替换为用户的 secretId
    secret_key = 'vmYCnUA6AEKYknnr8Jc6jM1b9gKvQzT0'  # 替换为用户的 secretKey
    region = 'ap-shanghai'  # 替换为用户的 Region

    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
    client = CosS3Client(config)

    response = client.upload_file(
        Bucket='guhua-buc-1324634892',
        LocalFilePath=imgFile,  # 本地文件的路径
        Key=imgname,  # 上传到桶之后的文件名
    )
    # 生成URL
    url = client.get_object_url(
        Bucket='guhua-buc-1324634892',
        Key=imgname
    )
    print(url)
    return url

def uploadVedio(imgname):
    imgFile = "output/"+imgname
    # imgFile = imgname
    secret_id = 'AKIDJZqCUfheTBlDXficObcYM2iT8xrkeSC0'  # 替换为用户的 secretId
    secret_key = 'vmYCnUA6AEKYknnr8Jc6jM1b9gKvQzT0'  # 替换为用户的 secretKey
    region = 'ap-shanghai'  # 替换为用户的 Region

    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
    client = CosS3Client(config)

    response = client.upload_file(
        Bucket='guhua-buc-1324634892',
        LocalFilePath=imgFile,  # 本地文件的路径
        Key=imgname,  # 上传到桶之后的文件名
    )
    # 生成URL
    url = client.get_object_url(
        Bucket='guhua-buc-1324634892',
        Key=imgname
    )
    print(url)
    return url
    # # imgFile = imgname
    # headers = {'Authorization': 'Hlk5YkdwRWJzvlQhCt5My7mgJxKVUOBn'}
    # files = {'smfile': open(imgFile, 'rb')}
    # url = 'https://sm.ms/api/v2/upload'
    # res = requests.post(url, files=files, headers=headers).json()
    #
    # back_url = res['data']['url']
    # print("成功将图片上传")
    # # print(back_url)
    # return back_url


