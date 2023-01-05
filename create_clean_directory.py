import os, shutil


def removeAndCreate(clean_folder):     
    # delete and recreate output folder 
    if os.path.exists(clean_folder):
        print("output folder exists, DELETING: '" + clean_folder)
        shutil.rmtree(clean_folder)	
    os.mkdir(clean_folder)