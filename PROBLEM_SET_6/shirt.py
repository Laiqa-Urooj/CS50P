import os
import sys
from PIL import Image, ImageOps

def main() :
    if len(sys.argv) >3 :
        sys.exit("Too many arguments")
    elif len(sys.argv) <3 :
        sys.exit("Too few arguments")

    img1 = sys.argv[1]
    img2 = sys.argv[2]
    validate(img1,img2)
    
    try :
        shirt = Image.open("shirt.png")
        photo = Image.open(img1)
    except FileNotFoundError :
        sys.exit("Input does not exist")
        
    photo = ImageOps.fit(photo,shirt.size)
    photo.paste(shirt,shirt)
    photo.save(img2)    
    
def validate(img1,img2) :
    valid_extensions = (".jpg", ".jpeg", ".png")
    if not img1.lower().endswith(valid_extensions):
        sys.exit("Invalid input")

    if not img2.lower().endswith(valid_extensions):
        sys.exit("Invalid output")
        
    if os.path.splitext(img1)[1].lower() != os.path.splitext(img2)[1].lower():
        sys.exit("Input and output have different extensions")

    if not os.path.exists(img1):
        sys.exit("Input does not exist")
        
        
if __name__ == "__main__":
    main()