import os # to be able to access our directories
import shutil # for moving files around (needed to organize our desktop)

extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".blend": "Blender",
    ".blend1": "Blender Backups",
    ".mp3": "Music"
}

def main():
    directory_path = input("Enter directory path to sort: ")

    # check if path exists first:
    path_is_directory = os.path.isdir(directory_path)

    if path_is_directory:
        organize_desktop(directory_path)
    else:
        print("Path provided is not a directory. Unable to organize.")

def organize_desktop(path):
    for filename in os.listdir(path):
        print(filename)

main()