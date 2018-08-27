from PIL import Image

# Add commands to import modules here.
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(file_name): #(Shawn_Mendes)
    im = Image.open(file_name, mode='r') #(filename, mode='r')
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show(title=None)

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.

def save_img(img, file_name): #(img, file_name)
    img.save(file_name) #(filename, format=None)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.

def obamicon(img):
    pass #replace this line with the correct command(s). Remember to return your image.
