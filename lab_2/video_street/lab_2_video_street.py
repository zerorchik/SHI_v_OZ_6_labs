import cv2
import imageio

cap = cv2.VideoCapture('Video_1.mp4')

# Ініціалізація класифікатора для розпізнавання людей
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Список для збереження кадрів
frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Зменшення розміру кадру до 50% від оригінального розміру
    scale_percent = 50
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    frame = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

    # Розпізнавання людей у кадрі
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), scale=1.1)
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow('People Detection', frame)

    # Додавання кадру
    frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Закриття вікна при натисканні клавіші 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Збереження кадрів у гіф
imageio.mimsave('Video_1.gif', frames, fps=25)