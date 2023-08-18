from PIL import Image
import os

def invert_images(directory, n):
    # Get a list of all image files in the directory
    image_files = [f for f in os.listdir(directory) if f.endswith('.jpg') or f.endswith('.png')]

    # Limit the number of images to process
    #image_files = image_files[:n]
    print("here1")
    print(len(image_files))
    for image_file in image_files:
        print("here")
        # Open the image
        image_path = os.path.join(directory, image_file)
        image = Image.open(image_path)

        # Invert the pixels
        inverted_image = Image.eval(image, lambda x: 255 - x)

        # Save the inverted image
        newdir="no defect inverted"
        inverted_image_path = os.path.join(newdir, 'inverted_' + image_file)
        inverted_image.save(inverted_image_path)

        print(f"Inverted image saved as: {inverted_image_path}")

# Specify the directory and number of images to process
directory = ("no defect check dataset")
num_images = 21

# Call the function to invert the images
invert_images(directory, num_images)
