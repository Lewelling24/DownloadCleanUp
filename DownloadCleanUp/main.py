import os # writing for windows

downloads_path = ''
text_file_path = ''
image_file_path = ''
audio_file_path = ''
video_file_path = ''
executable_file_path = ''

text_extensions = [".docx", ".txt", ".pdf", ".doc"]

image_extensions = [".jpg", ".jpeg", ".png", ".gif"]

audio_extensions = [".mp3", ".wav", ".mp4"]

video_extensions = [".mov", ".avi", ".flv", ".wmv"]

executable_extensions = [".exe", ".jar", ".zip"]

compressed_extensions = [".zip", ".rar", ".tar", ".gz"]


contents = os.listdir(downloads_path)

for item in contents:
    for i in text_extensions:
        if(item.endswith(i)):
            os.remove(downloads_path + '/' + item)