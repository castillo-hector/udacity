import os

def rename_files():
    os.chdir(r"H:\project\study\udacity\00 2 Secret Message\prank\prank")
    file_list = os.listdir(r"H:\project\study\udacity\00 2 Secret Message\prank\prank")
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")
        os.rename(file_name, new_name)

rename_files()
    
