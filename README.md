# Модуль фитнес-трекера
Модуль расчета и отображения полной информации о тренеровках по данным от блока датчиков.
Задача
Реализовать программный модуль по методологии ООП для расчета и отображения информации о прошедшей тренировке по данным от блока датчиков.

Базовый класс
class Training
Свойства класса
action - основное считываемое действие во время тренировке (шаг - бег, ходьба; гребок - плавание);
duration - длительность тренировки;
weight - вес спортсмена;
COEFF_CONVERSION = 1000 - коэффициент перевода из метров в километры;
LEN_STEP = 0.65 - длина шага;
Методы класса
get_distance() - метод возвращает значение дистанции приодоленной за тренировку
# базовая формула расчета
шаг * длина_шага / коэффициент_перевода
get_mean_speed() - метод возвращает значение средней скорости движения во время тренировки
# базовая формула расчета
дистанция / длительность
get_spent_calories() - метод возвращает число потраченных колорий
show_training_info() - метод возвращает объект информационного сообщения
Классы наследнки
Класс беговой тренировки

class Running
Свойства класса
наследуюутся

Методы класса
пререопределить метод:

get_spent_calories() - метод возвращает число потраченных колорий
# формула расчета
(18 * скорость - 20) * вес / 1000 * время_тренировки * 60
Класс спортивной ходьбы

class SportsWalking
Свойства класса
Добавляемые свойства:

height - рост
Методы класса
пререопределить метод:

get_spent_calories() - метод возвращает число потраченных колорий
# формула расчета
(0.035 * вес + (скорость ** 2 // рост) * 0.029 * вес) * длительность * 60
Класс тренировки в бассейне

class Swimming
Свойства класса
Добавляемые свойства:

length_pool - длина бассейна
count_pool - количество проплытых бассейнов
Методы класса
пререопределить метод:

get_mean_speed() - метод возвращает значение средней скорости движения во время тренировки
# формула расчета
длина_бассейна * количество_бассейнов / коэф_пресчета_из_м_в_км / длительность
get_spent_calories() - метод возвращает число потраченных колорий
# формула расчета
(скорость + 1.1) * 2 * вес
Класс информационного сообщения
class InfoMessage
Свойства класса
training_type - тип тренировки
duration - длительность тренировки
distance -дистанция приодоленная за тренировку
speed - средняя скорость движения во время движения
calories - потраченные за время тренировки килокалории
Методы класса
get_message() - метод выводит в терминал информационное сообщени о пройденной тренировке
# выводимое сообщение
# все значения типа float округляются до 3 знаков после запятой
'Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}.'
Функции модуля
def read_package()
Вызывает функцию печати стартового сообщения
Получает эмулированные данные пакета через терминал
Возвращает объект класса тренировки, определнные по длине пакета
def get_start_message()
Выводит в терминал стартовое сообщение
Стартовое сообщение:

Для эмуляции получения пакетов от блока датчиков
введите параметры для опереденного типа тренировки:
Бег: количество шагов, длительность, вес тела;
Спортиная ходьба: количество шагов, длительность, вес тела, рост;
Плавание: количество гребков, длительность, блина бассейна, количество бассейнов;
def main(training)
получает на вход типа Training
результат выполнения - вывод информационного сообщения из созданного объекта типа InfoMessage
