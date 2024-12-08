# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

print('Задание 1')
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
names = {}
for men in students:
    name = men['first_name']
    if name in names:
        names[name] += 1
    else:
        names[name] = 1
for name in names:
    print(f'{name}: {names[name]}')




# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
print('__________')
print('Задание 2')
names = {}
for men in students:
    name = men['first_name']
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

mega_name = students[0]['first_name']
for name in names:
    if names[name] > names[mega_name]:
        mega_name = name
print(f'Самое частое имя среди учеников: {mega_name}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
print('__________')
print('Задание 3')

def name_count(klass):
    names = {}
    for men in klass:
        name = men['first_name']
        if name in names:
            names[name] += 1
        else:
            names[name] = 1
    return names

def frequent_name (class_list):
    mega_name = list(class_list.keys())[0]
    for name in class_list:
        if class_list[name] > class_list[mega_name]:
            mega_name = name    
    # print(mega_name)
    return mega_name

for s_klass in range(len(school_students)):
    nams = name_count(school_students[s_klass])
    name1 = frequent_name(nams)
    print(f'Самое частое имя в классе {s_klass+1}: {name1}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???

print('__________')
print('Задание 4')

def male_female_count(Class_people):
    male = 0
    female = 0
    for men in range(len(Class_people)):
        name = Class_people[men]['first_name']
        if is_male[name]:
            male += 1
        else:
            female += 1
        c_ount = {'male': male, 'female': female}
    return c_ount

for claz in school:
    claz_name = claz['class']
    people = claz['students']
    m_count = male_female_count(people)
    print(f'Класс {claz_name}: девочки {m_count['female']}, мальчики {m_count['male']}')



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

print('__________')
print('Задание 5')

new_school = []

for claz in school:
    claz_name = claz['class']
    people = claz['students']
    m_count = male_female_count(people)
    new_students = [m_count]
    claz['class'] = claz_name
    claz['students'] = new_students
    new_school.append(claz)

male_st_kl = 0
female_st_kl = 0

for kl in new_school:
    if male_st_kl == 0 and female_st_kl == 0:
        male_st_kl = kl['class']
        max_male = kl['students'][0]['male']
        female_st_kl = kl['class']
        max_female = kl['students'][0]['female']
        
    else:
        if kl['students'][0]['male'] > max_male:
            male_st_kl = kl['class']
            max_male = kl['students'][0]['male']
        if kl['students'][0]['female'] > max_female:
            male_st_kl = kl['class']
            max_female = kl['students'][0]['female']
print(f'Больше всего мальчиков в классе {male_st_kl}')            
print(f'Больше всего девочек в классе {female_st_kl}')
print('__________')