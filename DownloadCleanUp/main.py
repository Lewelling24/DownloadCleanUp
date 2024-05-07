import os # writing for windows
import shutil # using to move files

#add your file paths here
downloads_path = ''
text_file_path = ''
image_file_path = ''
audio_file_path = ''
video_file_path = ''

#extensions for various file types
text_extensions = [".docx", ".txt", ".pdf", ".doc", ".xlsx"]

image_extensions = [".jpg", ".jpeg", ".png", ".gif"]

audio_extensions = [".mp3", ".wav", ".mp4"]

video_extensions = [".mov", ".avi", ".flv", ".wmv"]

executable_extensions = [".exe", ".jar", ".zip"]

compressed_extensions = [".zip", ".rar", ".tar", ".gz", ".iso"]

# open the downloads folder
contents = os.listdir(downloads_path)


def file_removal(contents):
    for item in contents:
        for i in text_extensions:
            if(item.endswith(i)):
                shutil.move(downloads_path + '/' + item, text_file_path + '/' + item)

        for i in image_extensions:
            if(item.endswith(i)):
                shutil.move(downloads_path + '/' + item, image_file_path + '/' + item)

        for i in audio_extensions:
            if(item.endswith(i)):
                shutil.move(downloads_path + '/' + item, audio_file_path + '/' + item)

        for i in video_extensions:
            if(item.endswith(i)):
                shutil.move(downloads_path + '/' + item, video_file_path + '/' + item)

        # deleting executable files. i.e. installers
        for i in executable_extensions:
            if(item.endswith(i)):
                os.remove(downloads_path + '/' + item)
        
        # deleting compressed files
        for i in compressed_extensions:
            if(item.endswith(i)):
                os.remove(downloads_path + '/' + item)

file_removal(contents)