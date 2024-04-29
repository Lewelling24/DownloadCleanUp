import os # writing for windows

#add your file paths here
downloads_path = ''
text_file_path = ''
image_file_path = ''
audio_file_path = ''
video_file_path = ''
executable_file_path = ''

#extensions for various file types
text_extensions = [".docx", ".txt", ".pdf", ".doc"]

image_extensions = [".jpg", ".jpeg", ".png", ".gif"]

audio_extensions = [".mp3", ".wav", ".mp4"]

video_extensions = [".mov", ".avi", ".flv", ".wmv"]

executable_extensions = [".exe", ".jar", ".zip"]

compressed_extensions = [".zip", ".rar", ".tar", ".gz"]

# open the downloads folder
contents = os.listdir(downloads_path)

# deleting compressed files
for item in contents:
    for i in text_extensions:
        if(item.endswith(i)):
            os.remove(downloads_path + '/' + item)

    for i in image_extensions:
        if(item.endswith(i)):
            os.remove(downloads_path + '/' + item)

    for i in audio_extensions:
        if(item.endswith(i)):
            os.remove(downloads_path + '/' + item)

    for i in video_extensions:
        if(item.endswith(i)):
            os.remove(downloads_path + '/' + item)

    for i in executable_extensions:
        if(item.endswith(i)):
            os.remove(downloads_path + '/' + item)
    
    for i in compressed_extensions:
        if(item.endswith(i)):
            os.remove(downloads_path + '/' + item)