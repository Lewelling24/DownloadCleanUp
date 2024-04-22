import os # writing for windows as that is what I have

path = 'your path here'


document_extensions = [".docx", ".txt", ".pdf"]

contents = os.listdir(path)

for item in contents:
    if(item.endswith(document_extensions[2])):
        print(item)