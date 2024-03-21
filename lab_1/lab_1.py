# Версія OpenCV
import cv2

print(cv2.__version__)

# Зчитування зображення
IMG = 'image.png'
img = cv2.imread(IMG)
img_gray = cv2.imread(IMG, 0)

# Відображення зображення
cv2.imshow('Colored cat', img)
cv2.waitKey()
cv2.destroyAllWindows()

# Збереження зображення
cv2.imwrite('bw_image.png', img_gray)
cv2.imshow('BW cat', img_gray)
cv2.waitKey()
cv2.destroyAllWindows()

# Отримання доступу до окремих пікселів
(blue, green, red) = img[100, 50]
print(f'{red = }, {green = }, {blue = }')

# Вирізання зображення
roi = img[70:245, 125:315]
cv2.imshow('ROI cat', roi)
cv2.waitKey()
cv2.destroyAllWindows()

# Зміна розміру зображення
resized = cv2.resize(img, (200, 200))
cv2.imshow('Resized cat', resized)
cv2.waitKey()
cv2.destroyAllWindows()

# Пропорційна зміна розміру зображення
IMG_RECT = 'image_rect.png'
img_rect = cv2.imread(IMG_RECT)
cv2.imshow('Rectangle cat', img_rect)
cv2.waitKey()
cv2.destroyAllWindows()

h, w = img_rect.shape[0:2]
h_new = 200
ratio = w / h
w_new = int(h_new * ratio)
resized = cv2.resize(img_rect, (w_new, h_new))
cv2.imshow('Prorortion resized cat', resized)
cv2.waitKey()
cv2.destroyAllWindows()

# Зміна розміру зображення за допомогою imutils
import imutils

resized = imutils.resize(img_rect, width=250)
cv2.imshow('Imutils resized cat', resized)
cv2.waitKey()
cv2.destroyAllWindows()

# Поворот зображення
resized = imutils.resize(img, width=250)
h, w = resized.shape[0:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(resized, M, (w, h))
cv2.imshow('Rotated cat', rotated)
cv2.waitKey()
cv2.destroyAllWindows()

# Поворот зображення за допмогою imutils
rotated = imutils.rotate(resized, +45)
cv2.imshow('Imutils rotated cat', rotated)
cv2.waitKey()
cv2.destroyAllWindows()

# Розмиття зображення
blured = cv2.GaussianBlur(resized, (11, 11), 0)
cv2.imshow('Blured cat', blured)
cv2.waitKey()
cv2.destroyAllWindows()

# Склеювання нормального та розмитого зображень
import numpy as np

sum = np.hstack((resized, blured))
cv2.imshow('Both cat', sum)
cv2.waitKey()
cv2.destroyAllWindows()

# Малювання прямокутника
cv2.rectangle(resized, (140, 80), (230, 140), (0, 0, 255), 2)
cv2.imshow('Cat with rectangle', resized)
cv2.waitKey()
cv2.destroyAllWindows()

# Малювання лінії
line = np.zeros((200, 200, 3), np.uint8)
cv2.line(line, (0, 0), (200, 200), (255, 0, 0), 5)
cv2.imshow('Line', line)
cv2.waitKey()
cv2.destroyAllWindows()

# Малювання ліній за набором точок
line = np.zeros((200, 200, 3), np.uint8)
points = np.array([[0, 0], [100, 200], [200, 100], [0, 0]])
cv2.polylines(line, np.int32([points]), 1, (255, 255, 255))
cv2.imshow('Polyline', line)
cv2.waitKey()
cv2.destroyAllWindows()

# Малювання кола
line = np.zeros((200, 200, 3), np.uint8)
cv2.circle(line, (100, 100), 50, (0, 0, 255), 2)
cv2.imshow('Circle', line)
cv2.waitKey()
cv2.destroyAllWindows()

# Розміщення тексту на зображенні
line = np.zeros((200, 550, 3), np.uint8)
font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(
    line, 'monday mood', (0, 100), font, 2, (255, 255, 255), 4, cv2.LINE_4
)
cv2.imshow('Text', line)
cv2.waitKey()
cv2.destroyAllWindows()