import os, shutil
import createjurorimages
import createwebsiteimages

#########
# Variables to change file titles and paths

# used to name juror files, file name for every photo with numbers, only for juror file
show_title = "foothills October2023"

# source input folder for input files, remember to use double slash
# if set wrong will geyt a 'FileNotFoundError' below
folder="C:\\Users\\rjp\\dev-foothills\\INPUTPhotosCleanedUp"

# has numbers and full titles
output_folder="C:\\Users\\rjp\\dev-foothills\\OUTPUT"
# has numbers as title, and in file name
output_juror_folder="C:\\Users\\rjp\\dev-foothills\\OUTPUT_JUROR"

##########
##
# Code starts here to 
# - create output folders
# - loop through files 
# - create web and juror resized images

files = os.listdir(folder)
 
# prints all files
files = [f for f in files if os.path.isfile(folder+'/'+f)] #Filtering only the files.
print(*files, sep="\n")

def removeAndCreate(clean_folder):     
    # delete and recreate output folder 
    if os.path.exists(clean_folder):
        print("output folder exists, DELETING: '" + clean_folder)
        shutil.rmtree(clean_folder)	
    os.mkdir(clean_folder)

# do folder creations
removeAndCreate(output_folder)
removeAndCreate(output_juror_folder)

#start index for filenaming and juror titles
number=0

# loop through all files in source folder 
for filename in files:
    number=number+1

    # do image creation in output folders
    createwebsiteimages.createwebsiteimages(filename, str(number).zfill(3), folder, output_folder)
    createjurorimages.createjurorimages(filename, str(number).zfill(3), show_title, folder, output_juror_folder)

