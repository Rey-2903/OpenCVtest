#Скачиваем библиотеку easyocr для считывания текста с картинок
#Команда для установки easyocr: pip install easyocr
#Библиотека imutils нужна для работы с изображениями (вращение и т.д.)
#Команда для установки imutils: pip install imutils
#Библиотека matplotlib для визуализации данных
#Команда для установки matplotlib: pip install matplotlib

import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img = cv2.imread('../images/Number2.jpeg') #импорт фото
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #приведение к серому цвету

#Оптимизация фотографии
img_filter = cv2.bilateralFilter(gray, 11, 15, 15) #накладывание фильтра для уменьшения различных точек (например, метод для уменьшения шума), передаём именно серое изображение
                                    #(серое изображение, диаметр-охват пикселей, цветовое пространство-как много пикселей с одинаковым цветом будут смешиваться, координатное пространство-насколько много различных пикселей, схожих по координатам, будут смешиваться)

#Найдём углы изображения
edges = cv2.Canny(img_filter, 30, 200) #(изображение с фильтром, мин порог, мах порог)

#Найдём контуры изображения
cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #поиск контуров (RETR_TREE-контуры по иерархии)
cont = imutils.grab_contours(cont) #считывание контуров
cont = sorted(cont, key=cv2.contourArea, reverse=True) #сортировка контуров (contourArea-метод сортировки, который ищет квадратные контуры, reverse-обратная сортировка для нахождения вверху нужных контуров, [:8]-показать последние 8 элементов)

#Поиск нужных контуров, которые оотвечают за отображение номерного знака
position = None
for c in cont: #перебираем все контуры
    approx = cv2.approxPolyDP(c, 10, True) #нахождение закрытых контуров (контур, на сколько сильно контур должен быть в форме квадрата, форма контуров является закрытой)
    if len(approx) == 4:  #проверка длины контура, если длина из 4 элементов, то это номерной знак (4 угла квадрата)
        position = approx
        break

#Выделение номерного знака из общего фото с помощью масок
mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [position], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask) #побитовая операция

#Вырезаем номерной знак из изображения
(x, y) = np.where(mask==255) #из матрицы (изображения) вытягиваем пиксили, которые подходят под определённые значения (например, приближены к белому цвету)
(x1, y1) = (np.min(x), np.min(y)) #верхняя левая координата номера
(x2, y2) = (np.max(x), np.max(y)) #нижняя правая координата номера
crop = gray[x1:x2, y1:y2] #обрежем изображение

#Прочитаем информацию с изображения
text = easyocr.Reader(['ru']) #(отслеживаемый язык) потребуется подождать загрузку языка
text = text.readtext(crop) #чтение изображения

#Вывод текста на фото
res = text[0][-2]
final_image = cv2.putText(img, res, (x1 - 200, y2 + 160), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
final_image = cv2.rectangle(img, (x1, x2), (y2, y2), (0, 255, 0), 1)


pl.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB)) #вывод изображение через библиотеку matplotlib
pl.show() #показ изображения




