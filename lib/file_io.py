def write_file(file_name, file_content):
   path = str(file_name) + ".txt"
   file =  open(path, mode="w" ,encoding="utf-8")
   file.write(file_content)

def append_file(file_name, append_content):
     path = str(file_name) + ".txt"
     file = open(path,mode="a",encoding="utf-8")
     file.write(append_content)
    

def read_file(file_name):
    path = str(file_name) + ".txt"
    file = open(path, mode="r", encoding="utf-8")
    return file.read()
    pass
