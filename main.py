import csv
import cv2
import shutil
import sys
import os
import zipfile
from PIL import Image, ImageDraw, ImageFont

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <template> <names> <font_size>")
        sys.exit(1)

    template_path = sys.argv[1]
    names_path = sys.argv[2]
    coordinates = get_click_coords(template_path)
    font_size = int(sys.argv[3])

    generate_certificate(template_path, names_path, coordinates, font_size)


# Opens a window to click on the image and get the coordinates
def get_click_coords(image_path):
    print("getting coordinates...")
    coords = {"x": None, "y": None}

    def print_click_coords(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            coords["x"], coords["y"] = x, y
            print(f'x = {x}, y = {y}')
            cv2.destroyAllWindows()

    img = cv2.imread(image_path)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', print_click_coords)

    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:  
            break

        if coords["x"] is not None:
            break

    cv2.destroyAllWindows()
    return coords["x"], coords["y"]



# Generates the certificates and saves them in a zip file
def generate_certificate(template_path, names_path, coordinates, font_size):

    font = ImageFont.truetype("arial.ttf", font_size)

    path = "certificates"
    os.makedirs(path, exist_ok=True)


    with open(names_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            template = Image.open(template_path)
            draw = ImageDraw.Draw(template)
            name = row[0]
            x, y = coordinates

            draw.text((x, y), name, fill="black", font=font)

            certificate_path = f"{path}/{name}.png"
            template.save(certificate_path)
            print(f"Generated certificate for {name}.")


    with zipfile.ZipFile("certificates.zip", "w") as zip_file:
        print("Saving certificates in certificates.zip .....")
        for root, _, files in os.walk("certificates"):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.basename(file_path))

    shutil.rmtree("certificates")
    print("Certificates generated and saved in certificates.zip")

if __name__ == "__main__":
    main()