import requests
import cv2
import numpy as np

r = requests.get('https://www.random.org/integers/?num=384&min=0&max=255&col=1&base=10&format=plain&rnd=new')
print(r.status_code)
numbers = r.text.splitlines()
rgb_image = np.zeros((128, 128, 3), np.uint8)
c = 0
for i in range(128):
    for j in range(128):
        rgb_image[i, j, 0] = int(numbers[c])
        rgb_image[i, j, 1] = int(numbers[c + 1])
        rgb_image[i, j, 2] = int(numbers[c + 2])
    c = c + 3
output_name = "rgb_image.jpg"
cv2.imwrite(output_name, rgb_image)
#print(numbers)

#print(type(r.text))