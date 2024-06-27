import cv2
import numpy as np

# #Обработка картинки
# img = cv2.imread('images/Monya.jpg') #чтение изображение, передаём путь к изображению

# #1. Уменьшение изображения
#new_img = cv2.resize(img, (500, 300)) #изменение размеров изображения
#new_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2)) #пропорциональное уменьшение изображения (1-индекс ширины, 0-индекс длины)

# #2. Показ картинки
# cv2.imshow('Monya', new_img) #показ изображения, передаём подпись изображения и картинку
# cv2.waitKey(0) #время показа картинки, 0 - каринка показывается бесконечно
#
# #3. Обрезка изображения
# cv2.imshow('Monya', img[0:100, 0:150]) #обрезка по ширине и длине
# cv2.waitKey(0)

# #4. Размытие изображения
# imgRazm = cv2.GaussianBlur(img, (7, 7), 10) #метод размытия
#                                             # (изображение, степень размытия (только нечётные значения),
#                                             # сигма-икс-умножитель размытия)
# cv2.imshow('Monya', imgRazm)
# cv2.waitKey(0)

# #5. Приведение формата
# imgKonvert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #метод конвертации (картинка, формат приведения)
# cv2.imshow('Monya', imgKonvert)
# cv2.waitKey(0)

# #6. Нахождение углов изображения
# imgDegrees = cv2.Canny(img, 70, 70) #(изображение, порог (точность) 1, порог 2)
# cv2.imshow('Monya', imgDegrees)
# cv2.waitKey(0)

# #7. Изменение обводки углов изображения
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBorder = cv2.Canny(img, 200, 200)
# kernel = np.ones((5, 5), np.uint8) #создание матрицы с 1 (кол-во элементов, кол-во списков, формат чисел)
# imgBorder = cv2.dilate(img, kernel, iterations=1) #(изображение, кол-во точек ширины (матрица), цикличность)
#
# imgBorder = cv2.erode(img, kernel, iterations=1) #уменьшение жирности обводок
#
# cv2.imshow('Monya', imgBorder)
# cv2.waitKey(0)
#
# print(img.shape) #вывод размеров картинки (высота, ширина, количество слоёв - rgb, чёрно-белая)

# #8. Создание своего изображения
# #Создадим матрицу - числа в списках влияют на изображение
# import numpy as np
#
# photo = np.zeros((450, 450, 3), dtype='uint8') #метод для создания матрицы ((кол-во элементов, кол-во списков, кол-во слоёв), формат)
#                                                #сама матрица является расширением для изображения
# #photo[100:150, 200:280] = 255, 0, 0 #окрашивание изображения, т.к. формат в OpenCV BGR, а не RGB, поэтому для синего цвета первое значение ставим на максимум
#                                     #:-закрасить всё изображение, числа-закрашивается квадрат [100:150-ширина, 200:280-высота]
#
# #9. Создание квадрата
# cv2.rectangle(photo, (70, 70), (100, 100), (119, 201, 105), thickness=3) #создание квадрата на изображении
#                                                                     #(изображение, (,)-точка начала-верхний левый угол,
#                                                                     #(,)-точка конца-нижний правый угол, (,,)-цвет обводки, thickness-жирность обводки (thickness=cv2.FILLED-залить весь квадрат))
#
# #10. Создание обычной линии
# cv2.line(photo, (0, photo.shape[0] // 2), (100, photo.shape[1] // 2), (119, 201, 105), thickness=3) #метод для создания линии (изображение, (,)-нач. точка, (,)-конеч. точ., (,,)-цвет, thickness-толщина линии)
#                                                                                                     #photo.shape[0] // 2 - середина изображения по ширине
#
# #11. Создание круга
# cv2.circle(photo, (photo.shape[0] // 2, photo.shape[1] // 2), 50, (119, 201, 105), thickness=3) #метод для создания круга (изображение, (,)-точ. центра, радиус, цвет, ширина обводки)
#
# #12. Обводка текстовых надписей
# cv2.putText(photo, 'Monya', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), thickness=1) #метод для обводки текста (изображение, текстовая надпись,
#                                                                                                 # (,)-точка нач. текста, формат шрифта, размер увеличения текста,
#                                                                                                 # цвет, толщина обводки)
#
# cv2.imshow('Photo', photo)
# cv2.waitKey(0)

# #Функции трансформации изображений
# img = cv2.imread('images/Monya.jpg')

# #1. Зеркальное изображение
# img = cv2.flip(img, -1) #зеркальное изображение, 0-по вертикали, 1-по горизонтали, -1-во горизонтали и по вертикали

# #2. Вращение изображения
# def rotate(img_param, angle):
#     height, width = img_param.shape[:2] #до второго элемента получить значения (высота и ширина, без кол-ва слоёв)
#     point = (width // 2, height // 2) #точка вращения
#     mat = cv2.getRotationMatrix2D(point, angle, 1) #создание матрицы для вращения (точка вращения, угол, увеличение изображения)
#
#     return cv2.warpAffine(img_param, mat, (width, height)) #возвращение изображения
#
# img = rotate(img, -90)

# #3. Смещение изображения
# def transform(img_param, x, y):
#     mat = np.float32([[1, 0, x], [0, 1, y]]) #матрица с элементами-число с точкой
#     return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))
#
# img = transform(img, 30, 200)

# #4. Контуры изображения
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #поиск контуров в сером формате проще
# img = cv2.GaussianBlur(img, (5, 5), 0) #размытие нужно для сглаживания углов -> быстрая обработка фото
# img = cv2.Canny(img, 50, 50) #находим края для чёткого нахождения контуров, все значения цветов > 100 будут проигнорированы
# contur, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #нахождение контуров, возвращает 2 значения, 1-список со всеми контурами, 2-иерархия объектов (квадрат->линия и т.д.)
#                                                                             #(изображение, режим получения контуров (RETR_LIST-получать все контуры), метод получения самих контуров
#                                                                             #(CHAIN_APPROX_NONE-найти все координаты всех контуров, CHAIN_APPROX_SIMPLE-нач. и конеч. точки контуров))

# #5. Создание картинки на основе контуров
# new_img = np.zeros(img.shape, dtype='uint8')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.GaussianBlur(img, (5, 5), 0)
# img = cv2.Canny(img, 50, 50)
# contur, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(new_img, contur, -1, (230, 111, 148), 1) #метод для создания картинки на основе контуров (картинка, контуры, id контуров, цвет, толщина обводки)
# #получилась та же картинка, но мы не просто описали все контуры, а считали с картинки контуры и на основе их координат построили картинку
#
# cv2.imshow('Monya', new_img)
# cv2.waitKey(0)

# #Цветовые форматы
# img = cv2.imread('images/Monya.jpg')

# #1. Формат HSV - каждый цвет варьируется в формате градусов (0-360)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# #2. Формат LAB
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# #3. Обратная трансформация
# img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
# img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

# #4. Формат RGB
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# #5. Разбитие на слои
# r, g, b = cv2.split(img) #разбитие картинки по слоям (например, все цвета, приближённые к красному, становятся белыми и т.д.)
#
# #6. Объединение слоёв
# img = cv2.merge([r, g, b]) #объединение слоёв
#
# cv2.imshow('Monya', img)
# cv2.waitKey(0)

# #Обработка видео
# video = cv2.VideoCapture('videos/Monya.mp4') #импорт видео
# video = cv2.VideoCapture(0) #считывание с камеры
# video.set(3, 500) #размеры изображения (id, ширина)
# video.set(4, 300) #размеры изображения (id, высота)
#
# #цикл для перебора изображений в видео
# while True:
#     success, images = video.read() #чтение видео,
#                                    #success-знаение true или false-результат чтения изображения,
#                                    #images-текущее изображение
#
#     cv2.imshow('Monya', images)
#
#     if cv2.waitKey(10) & 0xFF == ord('q'): #ord - отслеживание клавиши
#         break

#Функции трансформации изображений
# cap = cv2.VideoCapture('videos/Monya.mp4')
#
# while True:
#     success, img = cap.read()
#
#     img = cv2.GaussianBlur(img, (9, 9), 0)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     img = cv2.Canny(img, 75, 75)
#
#     kernel = np.ones((5, 5), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)
#
#     cv2.imshow('Result', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



# #Побитовые операции
# photo = cv2.imread('images/Monya.jpg')
# img = np.zeros(photo.shape[:2], dtype='uint8')
# circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
# square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)
#
# #Побитовые методы
# img = cv2.bitwise_and(circle, square) #(изображение1, изображение2) находит одинаковые части изображений и отображает их
# img = cv2.bitwise_or(circle, square) #объединяет оба изображения полностью
# img = cv2.bitwise_xor(circle, square) #совпадения картинок не отображается
# img = cv2.bitwise_not(circle, square) #создание инверсии
#
# #Маски изображений
# img = cv2.bitwise_and(photo, photo, mask=square) #вырезка частей из изображения
#
# cv2.imshow('Monya', img)
# cv2.waitKey(0)