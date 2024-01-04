import pytube

v_list = [
"'https://youtu.be/B9iQHLLdkUY?feature=shared'",
]

import os
download_location = os.getcwd()

# download_location = r'C:\Users\my039\OneDrive\桌面\python\影音爬蟲'
for video_url in v_list :
    yt = pytube.YouTube(video_url)
    print('開始下載')
    print(type(yt.streams.filter(res="720p")))
    stream = yt.streams.filter(res="720p").first()
    print(stream)
    stream.download(download_location)
    print('下載完成!!')
