import random
from decouple import config
import string
from captcha.image import ImageCaptcha
from sqlalchemy import create_engine


# Create image captcha with distortion and extra noise
image = ImageCaptcha(fonts=['Arial.ttf'], width=300, height=100)



# Generate random string for captcha
captcha_text = ''.join(random.choices(string.digits, k=6))

#draw lines over numbers
for i in range(0, 6):
    line_start = (random.randint(0, 300), random.randint(0, 100))
    line_end = (random.randint(0, 300), random.randint(0, 100))
    image.draw_line(line_start, line_end)


# Generate image from captcha text
captcha = image.generate(captcha_text)

# Save image to file
image.write(captcha_text, 'captcha.png')

# Connect to Postgres database
engine = create_engine('postgresql://username:password@host:port/database')

# Insert image and its answer into the database
with engine.connect() as con:
    con.execute("INSERT INTO captchas (answer, image) VALUES (%s, %s)", (captcha_text, 'captcha.png'))
