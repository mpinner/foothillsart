import os
import pandas as pd
from csv import writer
import locale


import create_clean_directory
import fetch_images
import createwebsiteimages

INPUT_CSV_FILE = "C:\\Users\\rjp\\dev-foothills\\load_artshow.csv"

IMAGE_DIR="C:\\Users\\rjp\\dev-foothills\\LOADED_ARTSHOW_IMAGES"
OUTPUT_DIR="C:\\Users\\rjp\\dev-foothills\\LOADED_ARTSHOW_WEB_OUTPUT"
OUTPUT_CSV=os.path.join(OUTPUT_DIR, "artshow_printout.csv")

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

fields = [
    "Name (First)",
    "Name (Last)",
    "Phone",
    "Art Title #1",
    "Art Work Style #1",
    "Quoted Value of Artwork Entry #1",
    "Art Work Size #1",
    "Artwork Upload Entry #1",
    "Art Title #2",
    "Art Work Style #2",
    "Quoted Value of Artwork Entry #2",
    "Art Work Size #2",
    "Artwork Upload Entry #2",
    "Art Title #3",
    "Art Work Style #3",
    "Quoted Value of Artwork Entry #3",
    "Art Work Size #3",
    "Artwork Upload Entry #3",
    "Art Title #4",
    "Art Work Style #4",
    "Quoted Value of Artwork Entry #4",
    "Art Work Size #4",
    "Artwork Upload Entry #4"
    
    ]

artshow = pd.read_csv(INPUT_CSV_FILE, usecols=fields)

create_clean_directory.removeAndCreate(IMAGE_DIR)
create_clean_directory.removeAndCreate(OUTPUT_DIR)

def isValid(entry):
    return not pd.isna(entry["Name (First)"])

def formatArtist(entry):
    return str(entry["Name (First)"]) + " " + str(entry["Name (Last)"])

def addPrintoutRow(artist, title, medium, dimensions, price, phonenumber):
    with open(OUTPUT_CSV, "a", newline="") as file:
        writer(file).writerow([artist, title, medium, price, dimensions, phonenumber])
        file.close()

def loadArtwork(entry, submissionNum):
    artist = formatArtist(entry)
    titleKey = "Art Title #" + str(submissionNum)
    if titleKey in entry.keys():
        title = entry[titleKey]
        print(artist, titleKey, title)
        if not pd.isna(title):
            phonenumber = entry["Phone"]
            if pd.isna(phonenumber):
                phonenumber = ""
            filename = artist + "_" + "".join(x for x in title.title() if x.isalnum()) + ".jpg"
            medium = entry["Art Work Style #" + str(submissionNum)]
            price = entry["Quoted Value of Artwork Entry #" + str(submissionNum)]
            if isinstance(price, int) or isinstance(price, float):
                price = locale.currency(price, grouping=True, symbol=True)
            if "$" not in price:
                price = "$" + price
            dimensions = entry["Art Work Size #" + str(submissionNum)]
            url = entry["Artwork Upload Entry #" + str(submissionNum)]
            
            if not pd.isna(title):
                addPrintoutRow(
                    artist=artist, 
                    title=title, 
                    medium=medium, 
                    dimensions=dimensions, 
                    price=price, 
                    phonenumber=phonenumber)
                if not pd.isna(url):
                    fetch_images.saveimage(url, filename, IMAGE_DIR)
                    createwebsiteimages.createwebsiteimages(
                        filename, 
                        artist=artist,
                        title=title,
                        medium=medium,
                        dimension=dimensions,
                        cost=price,
                        number=0,
                        folder=IMAGE_DIR,
                        output_folder=OUTPUT_DIR)



for index, entry in artshow.iterrows():
    if isValid(entry):
        artist = formatArtist(entry)
        print(artist)
        for submissionNum in range(1, 5):
            loadArtwork(entry, submissionNum)

    


