import os


# 15. Display Current Directory
# def current_directory():
#     print("\n15. Current Directory")
#     print(os.getcwd())


# 16. List Files
# def list_files():
#     print("\n16. Files and Folders")

#     files = os.listdir()

#     for file in files:
#         print(file)


# # 17. Create a Folder
def create_folder():
    print("\n17. Create Folder")

    folder = "student_data"

    if not os.path.exists(folder):
        os.mkdir(folder)
        print("Folder created successfully.")
    else:
        print("Folder already exists.")