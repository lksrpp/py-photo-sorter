# Summary: py-photo-sorter
This repository features a small python script to sort photos and videos based on their creation date in a year-month folder structure.

# Background & use case
I created this script to quickly create a new year-month strucutre for a large amount of photos and some video files located in one common folder. The new structure is ideal to store photos and videos on your Synology NAS, eg, at the DS Photos application directory.

# Usage
1. Clone this repository to a local directory
2. Install dependency package [exifread](https://pypi.org/project/ExifRead/) to your (virtual) environment (eg, pip install exifread)
3. Specify the absolute path to the source directory (line 53), that includes the photos & videos you would like to sort
    * The script only works with photos with ending "HEIC", "JPEG", "jpeg", "JPG", or "jpg", and videos with ending "MOV", "mov", or "mp4".
    * You can change the file types in case you want to consider additional files.
    * Subfolders are ignored.
4. Specify the target directory (line 56), where the sorted images should be copied to. As per default, a new directory "photo_sorted" is created within the source directory.
5. Run the script
    * For photos, the script tries to derive the creation date based on exif data. In case the exif data is not set, the fallback option is the modified date.
    * For videos, the script derives the creation date based on the modified date of the file
