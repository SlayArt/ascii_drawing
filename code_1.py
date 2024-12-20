from PIL import Image
import numpy as np

def ask_user():
    image_user = input("what is the link to the image you wanna transform ? ")
    img = Image.open(image_user)
    return img.convert('RGB')

def size_image(image):
    return image.size

def traitement(image, width, height, tableau):
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            avg = (r + g + b)/3

            if avg > 0 and avg < 55:
                tableau[x][y] = "$"
            elif avg > 200 and avg < 255:
                tableau[x][y] = "|"
    
    return tableau

def np_tab(image):
    height, width = size_image(image)
    tableau = np.full((height, width), "", dtype = str)
    return tableau

def main():
    image = ask_user()
    tab = np_tab(image)
    size = size_image(image)
    new_tab = traitement(image, size[0], size[1], tab)
    print(new_tab)

main()