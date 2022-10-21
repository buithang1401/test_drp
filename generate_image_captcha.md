# Generate image captcha in Python

```
from captcha.image import ImageCaptcha
# Specify the image size
image = ImageCaptcha( width = 300, height = 100)
# Specify the Text for captcha
captcha_text = input("Enter Captcha text: ")
# generate the image of the given text
data = image.generate(captcha_text)
# clcoding.com
# write the iamge omn the given file and save it
image.writr(captcha_text,'E:\CAPTCHA1.png')
from PIL import Image
Image.open('E:\CAPTCHA1.png')
```
