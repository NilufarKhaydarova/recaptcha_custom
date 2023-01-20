import random
import string
from captcha.image import ImageCaptcha
from decouple import config
from sqlalchemy import create_engine

password = config('PASSWORD')

# Create image captcha with distortion and extra noise
image = ImageCaptcha(fonts=['arial.ttf'], width=300, height=100,
                     noise_func=lambda x, y, z: (x*y*random.randint(0, z),
                                               x*y*random.randint(0, z)))

# Generate random string for captcha
captcha_text = ''.join(random.choices(string.digits, k=6))

# Generate image from captcha text
captcha = image.generate(captcha_text)

# Draw random lines over the image
for i in range(random.randint(5,10)):
    line_start = (random.randint(0,image.width), random.randint(0,image.height))
    line_end = (random.randint(0,image.width), random.randint(0,image.height))
    image.draw_line(line_start, line_end)

#Randomly change position of some numbers
captcha_text_list = list(captcha_text)
random.shuffle(captcha_text_list)
captcha_text = ''.join(captcha_text_list)

# Save image to file
image.write(captcha_text, 'captcha.png')



# Insert image and its answer into the database
with engine.connect() as con:
    con.execute("INSERT INTO captchas (answer, image) VALUES (%s, %s)", (captcha_text, 'captcha.png'))
