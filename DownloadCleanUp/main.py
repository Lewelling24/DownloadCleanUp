import os # writing for windows

path = 'Youre path here'


document_extensions = [".docx", ".txt", ".pdf"]

contents = os.listdir(path)

for item in contents:
    for i in document_extensions:
        if(item.endswith(i)):
            print(item)