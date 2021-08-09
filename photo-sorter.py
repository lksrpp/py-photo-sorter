# 
# Photo Sorter
#

# TODO Documentation
# only analyzes photos on the highest level, without subfolders
# .mov files with the same name will be copies in alignment with corresponding images(some iphone "live" images are backed up with image and video separately)
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

def get_create_date(file_path):
    photo = open(file_path, 'rb')
    exif_data = exifread.process_file(photo, stop_tag="EXIF DateTimeOriginal", details=False)
    creation_date = exif_data['EXIF DateTimeOriginal']
    photo.close()
    return creation_date

#
# Main
# 

if __name__ == "__main__":
    
    # TODO set absolute path
    source_directory = os.path.join("..", "py-photo-sorter-test", "photo-target")
    target_directory = os.path.join(source_directory, "photos_sorted")

    # iterate over all files in target_directory
    with os.scandir(source_directory) as dir:
        for entry in dir:
            if entry.is_file() and entry.name.endswith(("HEIC", "JPEG", "jpeg", "JPG", "jpg")):
                # TODO add code for images without exif data
                # TODO add code for .mov files that don't have exif dates but need to be in the same folder (check modified date)
                
                print("\n")
                print(entry.path)

                # extract creation year and month
                creation_date = datetime.strptime(str(get_create_date(entry.path)), '%Y:%m:%d %H:%M:%S')
                creation_year = creation_date.strftime("%Y")
                creation_month = creation_date.strftime("%m")

                print("creation date: ", creation_year, "-", creation_month)

                # create corresponding folder structure
                target_subdirectory = os.path.join(target_directory, creation_year, creation_month)
                os.makedirs(target_subdirectory, exist_ok=True)
                shutil.copy(entry.path, target_subdirectory)

                print("copied to ", target_subdirectory)

            else:
                continue