import io
import os
from gtts import gTTS


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
        
 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\spap9\OneDrive\Documents\SteelHacks\AudibleImage.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'idiotest.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

f = open("Text.txt", "x")

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
    f.write(text.description)
    if '.' in text.description:
        break