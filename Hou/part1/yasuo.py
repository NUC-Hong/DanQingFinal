import os
from venv import logger

import cv2

im_path = "Pictures/old1.png"


def compress_im(im_path):
    """
    图像压缩到5m以内
    :param file_path:
    :return:
    """

    target_m = 5

    imgFile = "static/image/" + im_path
    img = cv2.imread(imgFile)

    # filename = "static/new_image/" + im_path

    # img = cv2.imread(im_path)
    new_im_path = "static/new_image/" + os.path.splitext(im_path)[0] + '.jpg'
    print(new_im_path)
    # new_im_path = filename
    quality = 95
    while quality > 10:
        cv2.imwrite(new_im_path, img, [cv2.IMWRITE_JPEG_QUALITY, quality])

        file_size = os.stat(new_im_path).st_size / 1000 / 1000
        logger.info('compress img {} to {} M'.format(im_path, str(file_size)))
        if file_size <= target_m:
            break
        quality -= 10 if file_size >= 6.5 else 5  # 图像大小大于6.5M时以-10衰减，否则以5衰减
    # file = open(new_im_path, 'rb')
    # os.system('rm {}'.format(new_im_path))



    # cv2.imwrite(filename,img)
    print("yasuook")

# compress_im("1655364815126.png")

# import cv2
# img=cv2.imread("pictures/mengna.jpg")
# cv2.imshow("yuan",img)
#
# resized = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)
# cv2.imshow("bian",resized)
# cv2.waitKey(0)
