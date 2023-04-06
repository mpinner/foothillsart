import os, shutil
import createwebsiteimages

filename='Francis Kenda_ZigZagJag_Other Media_$950_8x11.jpg'
folder="C:\\Users\\rjp\\dev-foothills\\PhotosNov2022CleanedUp"
output_folder="C:\\Users\\rjp\\dev-foothills\\OUTPUT"

# delete and recreate output folder 
if os.path.exists(output_folder):
    print("output folder exists, DELETING: '" + output_folder)
    shutil.rmtree(output_folder)	
os.mkdir(output_folder)

createwebsiteimages.createwebsiteimages(filename, folder, output_folder)

