import os
import shutil

#zmienne
folders_list = ["Obrazy", 
    "Wideo", 
    "Dokumenty", 
    "Muzyka", 
    "Archiwa", 
    "Nieznane",
]
polish_signs = ["ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź", "ż", ]
main_path = r"C:\Users\Lukasz\Desktop\Bałagan"
all_file_extensions = {
    "Obrazy": ["jpeg", "png", "jpg", "svg", "bmp"],
    "Wideo": ["avi", "mp4", "mov", "mkv"],
    "Dokumenty": ["doc", "docx", "txt", "pdf", "xlsx", "pptx"],
    "Muzyka": ["mp3", "ogg", "wav", "amr"],
    "Testy": ["mp5", "kabom", "gzm"],
    "Archiwa": ["zip", "gz", "tar"],
} 

#funkcje
def list_of_files(main_path):
    allfiles = []
    items = os.listdir(main_path)
    
    for item in items:
        temp_path = os.path.join(main_path, item)
        if os.path.isdir(temp_path):
            allfiles.extend(list_of_files(temp_path))
        else:
            allfiles.append(temp_path)

    return allfiles

def move_files(all_files):
    try:
        for file in all_files:
            found_extension = False
            for extension_type, extension_lists in all_file_extensions.items():
                for extension in extension_lists:
                    if file.lower().endswith(extension):
                        destination_path = os.path.join(main_path, extension_type)
                        if not os.path.exists(destination_path):
                            os.makedirs(destination_path)
                        shutil.move(file, destination_path)
                        found_extension = True
                        break
                if found_extension:
                    break
            if not found_extension:
                destination_path = os.path.join(main_path, "Nieznane")
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                shutil.move(file, destination_path)
    except shutil.Error as e:
        print(f"Plik {file.split("\\")[-1]} istnieje już w katalogu {destination_path}.")

def removing(main_path):
    all_object = os.listdir(main_path)
    all_folders = []
    for item in all_object:
        item_path = os.path.join(main_path, item)
        if os.path.isdir(item_path):
            all_folders.append(item_path)
            removing(item_path)
    for folder in all_folders:
        if not os.listdir(folder):
            os.rmdir(folder)
            print(f"usunięto pusty folder: {folder}")

def rename(main_path):
    ren_file = []
    ren_files = os.listdir(main_path)
    for file in ren_files:
        temp_path = os.path.join(main_path, file)
        print(f"ren: {temp_path}")
        if os.path.isdir(temp_path):
            rename(temp_path)
        else:
            shortname = os.path.basename(file)
            new_shortname = shortname
            
            for letters in polish_signs:
                new_shortname = new_shortname.replace(letters, "_")
            if new_shortname == shortname:
                continue
            else:
                full_shortname = os.path.join(main_path, shortname)
                full_new_shortname = os.path.join(main_path, new_shortname)
                os.rename(full_shortname, full_new_shortname)
    return ren_file
    
#wywoływanie funkcji
all_files = list_of_files(main_path)
move_files(all_files)
removing(main_path)
rename(main_path)