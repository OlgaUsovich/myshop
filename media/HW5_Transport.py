# ДЗ5. Задача про Транспорт. 25.11.2020 Усович Ольга гр. 07.10.2020

# Условие задачи или то, как я его поняла:
# Создать классификацию транспорта, используя наследование классов.
# По заданным пользователем 4м критериям, находить класс, который первый в цепочке наследования
# содержит такие атрибуты и создавать 1 его экземпляр.
# Выводить пользователю информацию, экземпляр какого класса был создан и какие у него есть методы
# и атрибуты (включая все родительские методы и атрибуты).
# P.S. Вся ответственность за неправильно понятое условие лежит на постановщике задачи =)

import inspect


class Transport:
    engine = '+'
    control = '+'

    def move(self):
        print("Передвигается")

    def start(self):
        print("Заводится")

    def stop(self):
        print("Тормозит")

    def use_fuel(self):
        print("Использует топливо")

    def __str__(self):
        return 'экземпляр класса "Транспорт"'


class WaterTransport(Transport):
    water_type = '+'
    no_wheels = 'нет колес'

    def swim(self):
        print('Плавает')

    def __str__(self):
        return 'экземпляр класса "Водный транспорт"'


class Ship(WaterTransport):
    no_road = 'плывет по воде'

    def go_to_sea(self):
        print('Выходит в плаванье')

    def __str__(self):
        return 'экземпляр класса "Корабль"'


class AirTransport(Transport):
    air_type = '+'


    def fly(self):
        print('Летает')

    def __str__(self):
        return 'экземпляр класса "Воздушный ранспорт"'


class Airplane(AirTransport):
    wings = '+'

    def go_far(self):
        print('Передвигается на ограмные расстояния')

    def __str__(self):
        return 'экземпляр класса "Самолет"'


class LandTransport(Transport):
    land_type = '+'

    def drive(self):
        print('Ездит')

    def __str__(self):
        return 'экземпляр класса "Наземный транспорт"'


class RWTransport(LandTransport):
    land_tr_type = 'Железнодорожный'
    iron_wheel = '+'

    def drive_special(self):
        print('Ездит по рельсам')

    def __str__(self):
        return 'экземпляр класса "Железнодорожный транспорт"'


class AutoTransport(LandTransport):
    land_tr_type = 'Автотранспорт'
    wheel_type = '+'

    def go_road(self):
        print('Передвигается по дороге')

    def __str__(self):
        return 'экземпляр класса "Автотранспорт"'


class Car(AutoTransport):
    wheel_4 = '+'

    def stalls(self):
        print('Может заглохнуть')

    def __str__(self):
        return 'экземпляр класса "Машина"'


class MercedesBenz(Car):
    sedan = '+'
    petrol = '+'
    rear_drive = '+'
    automatic = '+'
    mileage = '300000 км'

    def rides_smoothly(self):
        print('Едет плавно')

    def __str__(self):
        return 'экземпляр класса "Mercedes-Benz"'


class KiaCarens(Car):
    minivan = '+'
    disel = '+'
    front_wheel = '+'
    mechanics = '+'
    mileage = '246957 км'

    def strange_noise(self):
        print('Периодически издает странные звуки')

    def drive_field(self):
        print('Ездит даже там, где нет дорог')

    def __str__(self):
        return 'экземпляр класса "Kia Carens"'


class FordFocus(Car):
    sedan = '+'
    petrol = '+'
    front_wheel = '+'
    automatic = '+'
    mileage = '193000 км'

    def fast_start(self):
        print('Быстро разгоняется')

    def __str__(self):
        return 'экземпляр класса "Ford Focus"'


class Bmw5(Car):
    universal = '+'
    disel = '+'
    front_wheel = '+'
    automatic = '+'
    mileage = '350000 км'

    def fast_start(self):
        print('Быстро разгоняется')

    def __str__(self):
        return 'экземпляр класса "BMW 5"'


class HyundaiSanta(Car):
    suv = '5 дв.'
    petrol = '+'
    rear_drive = '+'
    automatic = '+'
    mileage = '18020 км'

    def fast_start(self):
        print('Быстро разгоняется')

    def drive_field(self):
        print('Ездит даже там, где нет дорог')

    def __str__(self):
        return 'экземпляр класса "Hyundai Santa"'


class InfinityFX(Car):
    suv = '5 дв.'
    disel = '+'
    full_dr = 'постоянный полный привод'
    automatic = '+'
    mileage = '186000 км'

    def fast_start(self):
        print('Быстро разгоняется')

    def drive_field(self):
        print('Ездит даже там, где нет дорог')

    def growl(self):
        print('Рычит при быстром разгоне')

    def __str__(self):
        return 'экземпляр класса "Infinity FX"'


class SkodaRapid(Car):
    hatchback = '5 дв.'
    front_wheel = '+'
    petrol = '+'
    automatic = '+'
    no_mileage = '0 км пробега'

    def fast_start(self):
        print('Быстро разгоняется')

    def __str__(self):
        return 'экземпляр класса "Skoda Rapid"'


class KiaSorento(Car):
    suv = '5 дв.'
    disel = '+'
    full_dr = 'подключаемый полный привод'
    automatic = '+'
    no_mileage = '0 км пробега'

    def fast_start(self):
        print('Быстро разгоняется')

    def __str__(self):
        return 'экземпляр класса "Kia Sorento"'


main_dict = {WaterTransport: dir(WaterTransport), AirTransport: dir(AirTransport), LandTransport: dir(LandTransport),
             Ship: dir(Ship), Airplane: dir(Airplane), RWTransport: dir(RWTransport), AutoTransport: dir(AutoTransport),
             Car: dir(Car), MercedesBenz: dir(MercedesBenz), KiaCarens: dir(KiaCarens), FordFocus: dir(FordFocus),
             Bmw5: dir(Bmw5), HyundaiSanta: dir(HyundaiSanta), InfinityFX: dir(InfinityFX), SkodaRapid: dir(SkodaRapid)}
                                                                # словарь всех классов и их дир.
                                                                 # Создала руками, не знаю можно ли сделать это быстро

attribute_name = {'Есть двигатель': 'engine', 'Есть система управления': 'control', 'Является водным транспортом': 'water_type',  # словарь атрибутов
                  'Колеса отсутствуют': 'no_wheels', 'Плывет по воде':'no_road', 'Является воздушным транспортом': 'air_type',
                  'Есть крылья': 'wings', 'Является наземным транспортом': 'land_type', 'Имеет железные колеса': 'iron_wheel',
                  'Является разновидностью наземного транспорта': 'land_tr_type', 'На колесах есть шины': 'wheel_type',
                  'Имеет 4 колеса': 'wheel_4', 'Седан': 'sedan', 'На бензине': 'petrol',
                  'Заднеприводной': 'rear_drive', 'С коробкой-автомат': 'automatic', 'С пробегом': 'mileage',
                  'Минивэн': 'minivan', 'Дизель': 'disel', 'Переднеприводной': 'front_wheel', 'На механике': 'mechanics',
                  'Универсал': 'universal', 'Внедорожник': 'suv', 'Полный привод': 'full_dr', 'Без пробега': 'no_mileage'}

method_name = {'move': 'Возможность двигаться', 'start': 'Возможность завестись', 'stop': 'Возможность остановиться',   # словарь методов
               'use_fuel': 'Использование топлива',  'go_to_sea': 'Возможность долгого плавания',
               'go_far': 'Перемещение на больште расстояния', 'swim': 'Возможность плавать', 'fly': 'Возможность летать',
               'drive': 'Возможность ездить', 'drive_special': 'Особенность езды', 'go_road': 'Передвижение по дороге',
               'stalls': 'Глохнет', 'rides_smoothly': 'Двигается плавно', 'strange_noise': 'Издает странные звуки',
               'fast_start': 'Быстрый разгон', 'drive_field': 'Возможность ездить по бездорожью', 'growl': 'Рычит'}


def get_translate(user_answer):  # функция для перевода значений, введенных пользователем, в названия атрибутов и методов в программе
    new_p = []
    for i in user_answer:
        if i in attribute_name:
            new_p.append(attribute_name[i])
        else:
            for k in method_name.keys():
                if method_name.get(k) == i:
                    new_p.append(k)
    return new_p


def print_items(items, string):   # функция для печати списков
    print(string)
    count = 0
    for i in items:
        print(i, end=' | ')
        count += 1
        if count == 5:
            print()
            count = 0
    print()


print_items(attribute_name.keys(), 'Выберите атрибуты: ')  # печатаю атрибуты для выбора
print_items(method_name.values(), 'И/или методы: ')  # печатаю методы для выбора

class_dir = []
while True:
    p = [input("Введите параметр 1: ").strip(), input("Введите параметр 2: ").strip(), input("Введите параметр 3: ").strip(),
         input("Введите параметр 4: ").strip()]  # запрашиваю атрибуты и методы у пользователя
# print(p)
    p = get_translate(p)  # перевожу введенные пользователем атрибуты и методы в их названия в программе
# print(p)
    for f in main_dict.values():  # Проверяю, или все 4 значения есть в дир класса,
        count = 0                 # запоминаю тот дир, в котором первым найдены все 4 атрибута.
        for i in p:               # Здесь важен порядок следования классов main_dict
            if i in f:
                count += 1
        if count == 4:
            class_dir = f
            break
    if not class_dir:
        print('По заданным параметрам невозможно создать экземпяр класса. Попробуйте еще раз.')
    else:
        break


selected_class = 0
for k, v in main_dict.items():  # Определяю по main_dict, к какому классу относится найденный dir
    if v == class_dir:
        selected_class = k
# print(selected_class)

new_example = selected_class()  # создаю экземпляр класса, найденного первым в цепочке наследования


def get_translate_reverse(list):   # функция перевода названия методов и атрибутов на человеческий язык для красивого вывода
    new_list = []
    for i in list:
        if i in method_name:
            new_list.append(method_name[i])
        else:
            for k in attribute_name.keys():
                if attribute_name.get(k) == i:
                    new_list.append(k)
    return new_list


def get_atr(my_list):   # функция получения отдельно названий атрибутов
    atr_list = []
    for i in my_list:
        if i in attribute_name.values():
            atr_list.append(i)
    return atr_list


def get_meth(my_list):  # функция получения отдельно названий методов
    meth_list = []
    for i in my_list:
        if i in method_name.keys():
            meth_list.append(i)
    return meth_list


# print(get_translate_reverse(dir(selected_class)))

print(f'\nСоздан новый {new_example}.\n')  # печатаю название созданного экземпляра класса
print('Список его свойств и их значений:\n')  # печатаю названия атрибутов и их значений
for i in range(len(get_atr(dir(selected_class)))):
    print(get_translate_reverse(get_atr(dir(selected_class)))[i], ':', getattr(selected_class, get_atr(dir(selected_class))[i]))

print('\nСписок его функций:\n')  # Вызываю все имеющиеся методы (печатается результат их вызова) - подсказал программист с работы
func_list = [i[1](new_example) for i in inspect.getmembers(selected_class, predicate=inspect.isfunction)]


# надо попытаться запрашивать еще и значения атрибутов