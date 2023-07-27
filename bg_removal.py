#python code to remove the background of the image
#install necessary modules, read the image, process it and svae in the path.


from PIL import Image
from rembg import remove

input_image = Image.open('/home/reshma/Desktop/bird.jpg')
output = remove(input_image)

output.save('/home/reshma/Desktop/bird_out.png')
