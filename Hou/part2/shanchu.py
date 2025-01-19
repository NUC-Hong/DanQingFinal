import os


def delete(imagename):
    rootdir = "static/image/"

    # 清理imagename，避免包含的特殊字符影响路径构造
    cleaned_imagename = imagename.strip().replace('/', '').replace('\\', '')

    # 构建绝对路径，使用os.path.join确保跨平台兼容性
    filelist = [os.path.join(rootdir, f) for f in os.listdir(rootdir) if os.path.isfile(os.path.join(rootdir, f))]

    for filepath in filelist:
        # 检查文件名是否包含清理后的imagename
        if cleaned_imagename in os.path.basename(filepath):
            try:
                os.remove(filepath)
                print("已经删除：", filepath)
            except FileNotFoundError:
                print(f"文件未找到，无法删除：{filepath}")
            except Exception as e:
                print(f"删除文件时发生错误：{e}")