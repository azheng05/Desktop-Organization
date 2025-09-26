import os # to be able to access our directories
import shutil # for moving files around (needed to organize our desktop)

# modify as necessary for different scenarios!
extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".blend": "Blender",
    ".blend1": "Blender Backups",
    ".mp3": "Music",
    ".c": "C Programs",
    ".pdf": "PDFs"
}

def main():
    directory_path = input("Enter directory path to sort: ")

    # check if path exists first:
    path_is_directory = os.path.isdir(directory_path)

    if path_is_directory:
        organize_desktop(directory_path)
    else:
        print("Path provided is not a directory. Unable to organize.")

def organize_desktop(directory_path):

    for filename in os.listdir(directory_path):
        
        original_file_path = os.path.join(directory_path, filename)
        if not os.path.isfile(original_file_path):
            print(f"Skip {filename}. This is a folder.")

        # the extension of the file
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:

            # from the file's extension, get the corresponding folder name
            folder_name = extensions[extension]
            
            folder_path = os.path.join(directory_path, folder_name)
            # only creates the folder if it doesn't exist yet
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            # move the file into the new folder
            shutil.move(original_file_path, destination_path)
        else:
            print(f"Skip {filename}. It has an unknown extension.")
main()