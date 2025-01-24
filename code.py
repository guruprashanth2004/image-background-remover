from rembg import remove
from PIL import Image

# Path to the input image
input_path = 'path/to/your/image.jpg' 

# Path to save the output image
output_path = 'path/to/save/output.png'

# Open the image
input_image = Image.open(input_path)

# Remove the background
output_image = remove(input_image)

# Save the output image
output_image.save(output_path)