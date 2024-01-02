# import requests
# import re
# from pytube import YouTube

# YOUTUBE_STREAM_AUDIO = '140'  # Modify the value to download a different stream
# DOWNLOAD_DIR = 'E:\\vishal\\All Courses\\sql\\ORM'

# playlist_url = 'https://youtube.com/playlist?list=PLdLYbRBk3sGmWHmS4fYTucOImkssv8K3R&si=emEMgvBXFjHbWtb2'

# # Fetching HTML content of the playlist
# response = requests.get(playlist_url)
# html_content = response.text

# # Extracting video IDs from the HTML source
# video_ids = re.findall(r'watch\?v=([a-zA-Z0-9_-]{11})', html_content)

# YOUTUBE_STREAM_VIDEO = '22'

# # Download audio tracks using video IDs
# for video_id in video_ids:
#     yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
#     video_stream = yt.streams.get_by_itag(YOUTUBE_STREAM_VIDEO)
#     if video_stream:
#         print(f"Downloading: {yt.title}...")
#         video_stream.download(output_path=DOWNLOAD_DIR)
#     else:
#         print(f"No suitable video stream found for: {yt.title}")



from pytube import Playlist, YouTube


DOWNLOAD_DIR = 'E:\\vishal\\All Courses\\sql\\ORM'

playlist_url = 'https://youtube.com/playlist?list=PLdLYbRBk3sGmWHmS4fYTucOImkssv8K3R&si=emEMgvBXFjHbWtb2'

playlist = Playlist(playlist_url)

video_urls = playlist.video_urls

for video_url in video_urls:
    yt = YouTube(video_url)
    video_stream = yt.streams.filter(res="720p", file_extension="mp4").first()
    if video_stream:
        print(f"Downloading: {yt.title}...")
        video_stream.download(output_path=DOWNLOAD_DIR)
    else:
        print(f"No suitable video stream found for: {yt.title}")


