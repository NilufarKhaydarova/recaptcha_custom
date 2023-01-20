from PIL import Image, ImageFont, ImageDraw
import requests
import io

# Load font from URI
roboto_url = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Black.ttf?raw=true'
neuton_url = 'https://github.com/googlefonts/neuton/blob/main/fonts/ttf/Neuton-Black.ttf?raw=true'
pacifico = 'https://'

roboto = requests.get(roboto_url, allow_redirects=True)
arial = requests.get(arial_url, allow_redirects=True)
font = ImageFont.truetype(io.BytesIO(arial.content), size=24)

# Create image
img = Image.new('RGB', (200, 200), color = (73, 109, 137))
d = ImageDraw.Draw(img)

# Draw text
d.text((10,10), "Hello World", font=font, fill=(255,255,0))

# Save image
img.save("example.png")
