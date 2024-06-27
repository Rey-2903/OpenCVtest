#Возьмём уже натренированную модель для распознавания лиц с гитхаба
#Ссылка на гихаб: https://github.com/opencv/opencv/tree/master/data/haarcascades
#Возьмём модель haarcascade_frontalface_default.xml

import cv2

img = cv2.imread('../images/Friends.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #метод, который вытягивает файл как натренированную модель (путь к файлу)

#Работаем с информацией на сером изображении
results = faces.detectMultiScale(gray, scaleFactor=1.03, minNeighbors=65) #координаты найденных лиц, scaleFactor-размер лиц на фото, можно увеличивать в зависимоти от размера фото, minNeighbors-кол-во соседей рядом

#Выделение лиц в квадраты
#Выводим результат на цветном изображении
for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

cv2.imshow('Friends', img)
cv2.waitKey(0)


