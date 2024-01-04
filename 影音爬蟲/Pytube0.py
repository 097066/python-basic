# import pytube
#
# video_url = r"https://youtu.be/B9iQHLLdkUY?feature=shared"
# yt = pytube.YouTube(video_url)
# video_list = yt.streams
# print(video_list)

import os
# path = r'C:\Users\my039\OneDrive\桌面\python\2023-12-18turtleHomeWork四周跑的正方形-Ronnie.py'
# print(os.path.basename(path))   # 2023-12-18turtleHomeWork四周跑的正方形-Ronnie.py
# print(os.path.dirname(path))    # C:\Users\my039\OneDrive\桌面\python
# print(os.path.isfile(path))     # True
# print(os.path.isdir(path))      # False
# print(os.path.join('content','drive','test.txt'))   # content/drive/test.txt

start_path = r'C:\Users\my039\OneDrive\桌面\python'

for root, dirs, files in os.walk(start_path):
    for file in files:
        if file.endswith(   ('中華民國國旗.webp')   ) :
            print(os.path.join(root, file))
            os.system(r"copy 中華民國國旗.webp C:\Users\my039\OneDrive\桌面")  # 複製至 demo 資料夾裡 ( Windows 使用 copy )
