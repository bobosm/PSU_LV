import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

filename = r'C:\Users\Luka\Desktop\test.png'

img_original = mpimg.imread(filename)  
img = color.rgb2gray(img_original)
img = resize(img, (28, 28))

plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.axis('off')
plt.show()

img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')

model = models.load_model('najbolji_model_mnist.keras')

print("\nIzračunavam predikciju...")
predikcija = model.predict(img)
predvidjena_klasa = np.argmax(predikcija) 

print("\n" + "="*30)
print(f"Mreža je prepoznala znamenku: {predvidjena_klasa}")
print(f"Sigurnost mreže: {np.max(predikcija) * 100:.2f}%")
print("="*30 + "\n")