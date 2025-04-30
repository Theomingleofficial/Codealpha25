import os
import shutil

# Define categories and their file extensions
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Others': []
}

def get_category(file_extension):
    for category, extensions in FILE_TYPES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Others'

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path!")
        return

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            category = get_category(ext)
            category_path = os.path.join(folder_path, category)

            if not os.path.exists(category_path):
                os.makedirs(category_path)

            shutil.move(item_path, os.path.join(category_path, item))
            print(f"Moved: {item} --> {category}/")

    print("File organization complete.")

if __name__ == "__main__":
    target_folder = input("Enter the full path to the folder you want to organize: ").strip()
    organize_folder(target_folder)
