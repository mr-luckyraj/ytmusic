import time
start_time = time.time()
from pytube import YouTube
url = "https://youtu.be/qqsgGapGP84?si=nWdyuu94tTH_c_ng"

from pytube import YouTube

def download_audio_from_custom_server(yt_url, proxies={"https://piped.video/"}):
    yt = YouTube(yt_url)
    stream = yt.streams.filter(only_audio=True).get_by_itag(itag=251)
    print(stream)

# Usage example:
download_audio_from_custom_server(url)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")