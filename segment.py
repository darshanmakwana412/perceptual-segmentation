from PIL import Image
import numpy as np

image_path = "battleship.jpg"
image = np.array(Image.open(image_path))
image = np.mean(image, 2, dtype=np.uint8)

width = image.shape[0]
height = image.shape[1]

image = np.resize(image, width*height)
print(image.shape)

# segmentation = Image.fromarray(image, "L")
# segmentation.save("segmentation.png")