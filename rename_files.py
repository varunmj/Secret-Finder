import os
def rename_files():
    file_list=os.listdir("C:\Users\intel\Desktop\prank python\prank1")
    print(file_list)
    saved_path=os.getcwd()
    print("current working directory is "+saved_path)
    os.chdir("C:\Users\intel\Desktop\prank python\prank1")
    for file_name in file_list:
        print("old name- "+ file_name)
        print("New name- "+ file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)     

rename_files()
