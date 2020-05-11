from PIL import Image
import base64

def saveToPNG(dat):

    dat = dat.strip('data:image/png;base64')
    dat = dat.strip(',')

    dat = base64.b64decode(dat)
    
    with open("image.png", "wb") as f:
        f.write(dat)

    image = Image.open('image.png').convert("L")
    new_image = image.resize((28, 28))
    new_image.save('image2.png')
