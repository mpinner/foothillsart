from PIL import Image, ImageOps, ImageFont, ImageDraw

# creates juror image without artist name
def createjurorimages(filename, number, showtitle, folder, output_folder):
    # filename='Francis,Kenda_ZigZagJag_Other Media_8x11_$950.jpg'

    # parse attributes from image_filename
    attributes=filename.split('_')

    print(attributes)

    title=attributes[1]
    medium=attributes[2]
    dimension=attributes[3]
    cost=attributes[4].split('.')[0]

    image_filename=folder+"\\" + filename

    img = Image.open(image_filename)
    
    # fix rotate images via ORIENTATION 
    # https://pillow.readthedocs.io/en/latest/reference/ImageOps.html#PIL.ImageOps.exif_transpose
    img = ImageOps.exif_transpose(img)


    aspect_ratio = img.height / img.width
    new_width = 750
    new_height = new_width * aspect_ratio


    img = img.resize((new_width, int(new_height)))


    # add 50 pixel to top
    # with pink background
    border_height=60
    border_color='pink'
    img_with_border = ImageOps.pad(img,size=(img.width,img.height+border_height),color=border_color,centering=(1,1))

    # uncomment to save image for preview
    # img_with_border.save('imaged-with-border.png')

    # build new title 
    drawtext_line1=title.upper() + " #" + str(number)
    drawtext_line2=medium + ", " + dimension + ", " + cost

    font = ImageFont.truetype("arial.ttf", 24, encoding="unic")
    draw = ImageDraw.Draw(img_with_border)
    draw.text((img.width/2, 0), drawtext_line1, font=font, fill='black', anchor="ma")
    draw.text((img.width/2, 30), drawtext_line2, font=font, fill='black', anchor="ma")

    img_with_border.save(output_folder+"\\" + str(number) + "_ " + showtitle + ".jpg" )
