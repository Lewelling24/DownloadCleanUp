import os # writing for windows

path = ''


text_extensions = [".docx", ".txt", ".pdf", ".doc"]

image_extensions = [".jpg", ".jpeg", ".png", ".gif"]

audio_extensions = [".mp3", ".wav", ".mp4"]

video_extensions = [".mov", ".avi", ".flv", ".wmv"]

executable_extensions = [".exe", ".jar", ".zip"]

compressed_extensions = [".zip", ".rar", ".tar", ".gz"]


contents = os.listdir(path)

for item in contents:
    for i in text_extensions:
        if(item.endswith(i)):
            os.remove(path + '/' + item)