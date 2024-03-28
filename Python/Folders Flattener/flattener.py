import os
import shutil

RESTRICTED_AREAS = [r"C:\Users\Adam\Desktop", r"C:\Users\Adam\Desktop\Scripts\Python-Scripts\Flatten Folders"]

def flatten_directory(source_dir, target_dir):    
    for root, dirs, files in os.walk(source_dir, topdown=False): 
        if os.getcwd() in RESTRICTED_AREAS:
            print(f"'ERROR: {os.getcwd()}' is a restricted area! Aborting program.")
            return
            
        for file in files:
            # Don't touch raw files in root directory (for copy files purposes)
            if(root == "./" or root == target_dir):
                continue
            file_path = os.path.join(root, file)
            print(f"root = {root}\nfile = {file}\nfile_path = {file_path}\n--------\n")

            target_file_path = os.path.join(target_dir, file)
            
            # If a file with the same name already exists in the target directory, rename it
            count = 0
            while os.path.exists(target_file_path):
                count += 1
                base_name, extension = os.path.splitext(file)
                new_file_name = f"{base_name} - Copy ({count}){extension}"
                target_file_path = os.path.join(target_dir, new_file_name)

            shutil.move(file_path, target_file_path)

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            
            try:
                os.rmdir(dir_path)
            except OSError:
                pass

def run():
    source_directory = "./"  # Change this to your source directory
    target_directory = "./loot"  # Change this to your target directory

    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)

    flatten_directory(source_directory, target_directory)

run()
