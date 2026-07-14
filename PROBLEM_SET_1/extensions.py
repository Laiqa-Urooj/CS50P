#Main function to take user's greeting 
def main() :
    file_name=input("File name : ")
    file_media_type(file_name)

#Function to calculate appropriate compensation for user's greeting
def file_media_type(file_name) :
    name=file_name.lower().strip()
    if name.endswith(".gif") :
        print("image/gif")
    elif name.endswith(".jpg") :
        print("image/jpg")
    elif name.endswith(".jpeg") :
        print("image/jpeg")
    elif name.endswith(".png") :
        print("image/png")
    elif name.endswith(".pdf") :
        print("application/pdf")
    elif name.endswith(".txt") :
        print("text/plain")
    elif name.endswith(".zip"):
        print("application/zip")
    else :
        print("application/octet-stream")

main()