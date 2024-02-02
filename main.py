import csv
import shutil
import sys
import os
import zipfile
from PIL import Image, ImageDraw, ImageFont

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <template> <names> <coordinates>")
        sys.exit(1)

    template_path = sys.argv[1]
    names_path = sys.argv[2]
    coordinates = tuple(map(int, sys.argv[3].split(",")))

    generate_certificate(template_path, names_path, coordinates)

def generate_certificate(template_path, names_path, coordinates):
    # Load the template image
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

    # Load the font
    font = ImageFont.truetype("arial.ttf", 24)
    
    # Create a directory to save the certificates
    path = "certificates"
    os.makedirs(path, exist_ok=True)


    # Open the names CSV file
    with open(names_path, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Generate certificates for each name
        for row in reader:
            name = row[0]
            x, y = coordinates

            # Draw the name on the template
            draw.text((x, y), name, fill="black", font=font)

            # Save the certificate
            certificate_path = f"{path}/{name}.png"
            template.save(certificate_path)
            
    # Create a zip file of all the certificates
    with zipfile.ZipFile("certificates.zip", "w") as zip_file:
        for root, _, files in os.walk("certificates"):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.basename(file_path))

    # Remove the certificates directory
    shutil.rmtree("certificates")
    print("Certificates generated and saved in certificates.zip")

if __name__ == "__main__":
    main()