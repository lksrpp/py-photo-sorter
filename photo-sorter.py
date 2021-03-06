# 
# Photo Sorter
#


#
# Imports
#

import os
import shutil
import exifread #https://pypi.org/project/ExifRead/
from datetime import datetime


#
# Functions
#

def get_exif_create_date(file_path):
    photo = open(file_path, 'rb')
    exif_data = exifread.process_file(photo, stop_tag="EXIF DateTimeOriginal", details=False)
    photo.close()
    creation_date = exif_data['EXIF DateTimeOriginal']
    return creation_date

def get_file_mod_date(file_path):
    return datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y:%m:%d %H:%M:%S")

def get_creation_year_month(timestamp):
    creation_date = datetime.strptime(str(timestamp), "%Y:%m:%d %H:%M:%S")
    creation_year = creation_date.strftime("%Y")
    creation_month = creation_date.strftime("%m")
    return creation_year, creation_month

def create_structure_copy_file(source_filepath, target_subdirectory):
    os.makedirs(target_subdirectory, exist_ok=True)
    shutil.copy(source_filepath, target_subdirectory)
    print("copied", source_filepath, "to", target_subdirectory)


#
# Main
# 

if __name__ == "__main__":
    
    # specify source directory (folder with unsorted photos)
    source_directory = os.path.join("..", "py-photo-sorter-test", "photo-target")

    # specify target directory (default: create a new folder "photos_sorted" inside source directory)
    target_directory = os.path.join(source_directory, "photos_sorted")

    # iterate over all files in source_directory and sort photo and movie files
    with os.scandir(source_directory) as dir:
        for entry in dir:
            if entry.is_file() and entry.name.endswith(("HEIC", "JPEG", "jpeg", "JPG", "jpg")):
                
                try:
                    creation_year, creation_month = get_creation_year_month(get_exif_create_date(entry.path))
                except KeyError:
                    print("Warning: no exif data, use modification date for file", entry.path)
                    creation_year, creation_month = get_creation_year_month(get_file_mod_date(entry.path))

                create_structure_copy_file(entry.path, os.path.join(target_directory, creation_year, creation_month))

            elif entry.is_file() and entry.name.endswith(("MOV", "mov", "mp4")):

                creation_year, creation_month = get_creation_year_month(get_file_mod_date(entry.path))
                create_structure_copy_file(entry.path, os.path.join(target_directory, creation_year, creation_month))

            else:
                continue
