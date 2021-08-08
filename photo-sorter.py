# 
# Photo Sorter
#

#Imports
import os
import exifread #https://pypi.org/project/ExifRead/


def get_create_date(file_path):
    photo = open(file_path, 'rb')
    exif_data = exifread.process_file(photo, stop_tag="EXIF DateTimeOriginal", details=False)
    creation_Date = exif_data['EXIF DateTimeOriginal']
    photo.close()
    return creation_Date


if __name__ == "__main__":
    
    # TODO set absolute path
    target_directory = os.path.join("..", "py-photo-sorter-test", "photo-target")

    # iterate over all files in target_directory
    with os.scandir(target_directory) as dir:
        for entry in dir:
            if entry.is_file() and entry.name.endswith(("HEIC", "JPEG", "jpeg", "JPG", "jpg")):
                # TODO add code for images without exif data
                # TODO add code for .mov files that don't have exif dates but need to be in the same folder (check modified date)
                
                print ("\n" + entry.path)
                
                creation_date = get_create_date(entry.path)
                print(creation_date)

            else:
                continue