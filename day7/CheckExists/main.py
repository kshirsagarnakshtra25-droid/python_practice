import file_module

print("\n===== 18. Check File/Folder =====")

filename = input("Enter file/folder name: ")

if file_module.check_exists(filename):
    print("File/Folder exists.")
else:
    print("File/Folder does not exist.")