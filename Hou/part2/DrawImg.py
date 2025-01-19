
from http import HTTPStatus
import dashscope


def simple_multimodal_conversation_call(img):
    dashscope.api_key = 'sk-1def98b08c3d4fc8938f4184bc648c4f'
    messages = [
        {
            "role": "user",
            "content": [
                {"image": img},
                {"text": "根据这个图片生成一首中国古诗，要求对仗工整"}
            ]
        }
    ]
    response = dashscope.MultiModalConversation.call(
        model='qwen-vl-plus',
                                                     # model=dashscope.MultiModalConversation.Models.qwen_vl_chat_v1,
                                                     messages=messages)
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.

    text = response.output.choices[0].message.content[0]['text']
    # text = response.output.choices[0].message.content
    return text