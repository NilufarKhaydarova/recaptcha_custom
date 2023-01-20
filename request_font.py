import requests
import io
from PIL import Image, ImageDraw, ImageFont

# URLs for the TTF fonts you want to download
font_urls = {
    'Arial': 'https://www.fonts.com/font/monotype/arial/regular',
    'Roboto': 'https://www.fonts.com/font/google/roboto/regular',
    'Pacifico': 'https://www.fonts.com/font/vernon-adams/pacifico/regular'
}

# Download the TTF fonts
fonts = {}
for font_name, url in font_urls.items():
    response = requests.get(url)
    fonts[font_name] = io.BytesIO(response.content)

# Create an image and draw on it
img = Image.new('RGB', (200, 200), color = (73, 109, 137))
d = ImageDraw.Draw(img)

# Use the Arial font to draw text on the image
font = ImageFont.truetype(fonts['Arial'], size=24)
d.text((10,10), "Hello World", font=font, fill=(255,255,0))

# Use the Roboto font to draw text on the image
font = ImageFont.truetype(fonts['Roboto'], size=24)
d.text((10,50), "Hello World", font=font, fill=(255,255,0))

# Use the Pacifico font to draw text on the image
font = ImageFont.truetype(fonts['Pacifico'], size=24)
d.text((10,90), "Hello World", font=font, fill=(255,255,0))

# Save the image
img.save("example.png")



