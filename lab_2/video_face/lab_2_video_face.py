import cv2
import imageio

cap = cv2.VideoCapture('zelenskiy_30.mp4')

# Ініціалізація класифікаторів для виявлення облич, очей та усмішок
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

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

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Виявлення облич у кадрі
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(85, 85))
    num_faces = len(faces)

    # Виявлення очей та усмішок
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        # Виявлення очей
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5, minSize=(1, 1))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        # Виявлення усмішки
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

    print("Кількість осіб у кадрі:", num_faces)
    cv2.imshow('Face Detection', frame)

    # Додавання кадру
    frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Закриття вікна при натисканні клавіші 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Збереження кадрів у гіф
imageio.mimsave('zelenskiy.gif', frames, fps=25)