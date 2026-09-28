import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_filtering(img,kernel,p,s):
  m,n=img.shape;x,y=kernel.shape
  if p!=0:
    padded_img=np.pad(img,p,'constant')
  else:
    padded_img=img
  m=int((padded_img.shape[0]-x+2*p)/s)+1
  n=int((padded_img.shape[1]-y+2*p)/s)+1
  filtered_img=np.zeros((m,n))
  for i in range(m):
    for j in range(n):
      filtered_img[i,j]=np.sum(kernel*padded_img[i*s:i*s+x, j*s:j*s+y])
  return filtered_img

img=cv2.imread("/content/drive/MyDrive/dove.jpg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
k_s=9

kernel = np.ones( (k_s, k_s),dtype=np.float32) / (k_s * k_s)
filtered_image=image_filtering(grayscale,kernel,0,1)

for i in range(1,m-1):
  for j in range(1,n-1):
    angle=orientation[i][j]
    p1,p2=angle_set[angle]
    if magnitude[p1[0]+i][p1[1]+j]>magnitude[p2[0]+i][p2[1]+j]:
      filtered_image[i][j]=0
    else:
      filtered_image[i][j]=magnitude[p1][j]
      magnitude[i][j]=0

Tl=12 ;Th=31
Strong_edge=magnitude>=Thigh*255
Weak_edge=(magnitude>=Tl*255) & (magnitude<Th*255)

plt.figure(figsize=(15,15))
plt.subplot(2, 2, 1)
plt.imshow(grayscale, cmap="gray")
plt.title("Original")

plt.subplot(2, 2, 2)
plt.imshow(filtered_image, cmap="gray")
plt.title("Filtered")
plt.show()

print("original size",grayscale.shape)
print("filtered size",filtered_image.shape)
