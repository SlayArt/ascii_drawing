from PIL import Image

def drawing_in_file(charactere):
    with open("ascii_color_drawing.txt", "a+") as file:
        file.write(charactere)

def ask_user():
    image_user = input("what is the link to the image you wanna transform ? ")
    img = Image.open(image_user)
    return img.convert('RGB')

def size_image(image):
    width, height = image.size
    aspect_ratio = width / height
    new_width = 150
    new_height = int(new_width / aspect_ratio)

    resized_img = image.resize((new_width, new_height), Image.LANCZOS)

    return resized_img

def traitement(image, width, height):
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            avg = (r + g + b)/3

            if avg > 0 and avg < 55:
                drawing_in_file("$")
            elif avg > 200 and avg < 255:
                drawing_in_file("|")
        drawing_in_file(" END OF A LINE ... end of a line ...\n") 

def main():
    print("STARTING... ")
    image = ask_user()
    print("IN WORKING... ")
    resized_img = size_image(image)
    traitement(resized_img, resized_img.width, resized_img.height)
    print("WORK END... PROCESS OCCURE WITH NO ISSUE... ")

main()
