# from moviepy.editor import VideoFileClip, AudioFileClip, afx
#
#
# # 比较快的合并视频和音频方式
# def merge(myMp4, myMp3, resultPath):
#     video = VideoFileClip(myMp4)
#     audio = AudioFileClip(myMp3)
#     video_merge = video.set_audio(audio)
#     video_merge.write_videofile(resultPath)
#     # os.remove('{title}.mp4')
#
#
# def divide():
#     video = VideoFileClip("E:/guhua/hou/part2/finalGuHuaChuLi/static/vedio/2.mp4")
#     audio = video.audio
#     audio.write_audiofile("2.mp3")
#
#
# merge("E:/guhua/hou/part2/finalGuHuaChuLi/output/2.mp4", "E:/guhua/hou/part2/finalGuHuaChuLi/static/vedio/2.mp4",
#       "E:/guhua/hou/part2/finalGuHuaChuLi")
import moviepy.editor as mp
import os
from moviepy import *
import ffmpeg
from moviepy.editor import *


# 分离视频中的音频
def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    return my_clip


# 比较快的合并视频和音频方式
def merge(myMp4, myMp3, resultPath):
    video = VideoFileClip(myMp4)
    audio = AudioFileClip(myMp3)
    video_merge = video.set_audio(audio)
    video_merge.write_videofile(resultPath)
    # os.remove('{title}.mp4')


# 比较慢的合并方式
def merge1(myMp4, myMp3, resultPath):
    audio = ffmpeg.input(myMp3)
    video = ffmpeg.input(myMp4)
    print("合并视音频")
    out = ffmpeg.output(video, audio, resultPath)
    out.run()
    # os.remove('{title}.mp3')
    print("完成")


def mergeVoiceAndVideo(bathPath,videoName,resultPath):
    # 分离音频
    file_path = bathPath + videoName
    resultMusic = "1.mp3"
    my_clip = extract_audio(file_path)
    my_clip.audio.write_audiofile(resultMusic)
    # 合并视频
    myMp4 = resultPath+videoName
    myMp3 = resultMusic
    resultPath = resultPath + "result.mp4"
    print(resultPath)
    merge(myMp4, myMp3, resultPath)
    # merge1(myMp4,myMp3)
# video = VideoFileClip("E:/guhua/hou/part2/finalGuHuaChuLi/output/2.mp4")

# resultMusic = "1.mp3"
# my_clip = extract_audio("E:/guhua/hou/part2/finalGuHuaChuLi/static/vedio/2.mp4")
# my_clip.audio.write_audiofile(resultMusic)