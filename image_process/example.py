from PIL import Image
from StringIO import StringIO

image = open('./cat.jpg').read()
image = Image.open(StringIO(str(image)))
print image.mode