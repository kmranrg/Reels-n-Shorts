from rembg import remove
from PIL import Image
import numpy as np

def remove_background_new(image_path):
    try:
        # taking the source image
        source = Image.open(image_path)

        # Convert the input image to a numpy array
        input_array = np.array(source)

        # Apply background removal using rembg
        output_array = remove(input_array)

        # Create a PIL Image from the output array
        output_image = Image.fromarray(output_array)

        output_path = image_path.split('.')[0] + "_without_bg.png"
        output_image.save(output_path)
        print(f"Background removed successfully from {image_path}.")
    except Exception as e:
        print(f"Failed to remove background in {image_path}.")
        print("Error:",e)
    return

remove_background_new("01.jpg")
remove_background_new("02.jpg")
remove_background_new("03.jpg")
remove_background_new("04.jpg")