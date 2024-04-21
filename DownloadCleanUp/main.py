import os # writing for windows as that is what I have

path = 'Your path here'


document_extensions = [".docx", ".txt", ".pdf"]

contents = os.listdir(path)

for item in contents:
    print(item)