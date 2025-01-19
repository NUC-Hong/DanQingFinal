from http import HTTPStatus
from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath
import requests
from dashscope import ImageSynthesis
import dashscope

from xiazai import xiazai


def toImg(text):
    dashscope.api_key = 'sk-1def98b08c3d4fc8938f4184bc648c4f'
    prompt = "根据这首古诗生成一幅中国水墨画：" + text
    rsp = ImageSynthesis.call(model=ImageSynthesis.Models.wanx_v1,
                              prompt=prompt,
                              n=1,
                              size='1024*1024')
    if rsp.status_code == HTTPStatus.OK:
        if rsp.output.results and 'url' in rsp.output.results[0]:
            print(rsp.output.results[0]['url'])
            return rsp.output.results[0]['url']
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))