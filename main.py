from PIL import Image
from rembg import remove

input_patch='teste.jpg'
output_patch='resultado.png'
input=Image.open(input_patch)
output=remove(input)
output.save(output_patch)
