from PIL import Image, ImageEnhance, ImageFilter
import os

#img1 = Image.open('sudhir.jpg')
#img1.save('sudhir.pdf')
#img1.show()

#max_size=(250,250)
#img1.thumbnail(max_size)
#img1.show()

#for item in os.listdir():
#    if item.endswith('.jpg'):
#        img1 = Image.open(item)
#        filename,extention = os.path.splitext(item)
#        img1.save(f'{filename}.pdf')

# ------------------ Sharpness ----------------------

#img1 = Image.open('sudhir.jpg')
#enhancer = ImageEnhance.Sharpness(img1)
#enhancer.enhance(10).save('edit.jpg')

# ------------------ Color ----------------------

#img1 = Image.open('sudhir.jpg')
#enhancer = ImageEnhance.Color(img1)
#enhancer.enhance(5).save('edit.jpg')

# ------------------ Brightness ----------------------

#img1 = Image.open('sudhir.jpg')
#enhancer = ImageEnhance.Brightness(img1)
#enhancer.enhance(3).save('edit.jpg')

# ------------------ Contrast ----------------------

#img1 = Image.open('sudhir.jpg')
#enhancer = ImageEnhance.Contrast(img1)
#enhancer.enhance(1.5).save('edit.jpg')

# ------------------ Bluer ----------------------

#img1 = Image.open('sudhir.jpg')
#img1.filter(ImageFilter.GaussianBlur(radius=5)).save('edit.jpg')