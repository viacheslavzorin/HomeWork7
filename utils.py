import json


def load_students():
    """Загружает список студентов из файла"""

    with open('students.json', 'r') as file:
      student_dict = json.load(file)
    return student_dict


def load_professions():

     """Загружает список профессий из файла"""

     with open('profession.json', 'r') as file:
        profession_dict = json.load(file)
     return profession_dict


def get_student_by_pk(pk, dict_list):

    """Получает словарь с данными студента по его pk"""

    for i in dict_list:
        if pk == int(i['pk']):
            return i


def get_profession_by_title(title,dict_list):

    """Получает словарь с инфо о профе по названию"""

    for i in dict_list:
        if title == i['title']:
            return i

def check_fitness(student,profession):

    """Функция получив студента и профессию возвращает словарь"""

    cpeshial_dict = {}
    student_set=set(student)
    profession_set=set(profession)
    x = profession_set - student_set

    student_list=student_set.intersection(profession_set)

    a=len(list(student_list))/len((list(profession_set)))*100
    a=int(a)

    cpeshial_dict['has']=list(student_list)
    cpeshial_dict['lacks']=list(x)
    cpeshial_dict['fit_percent']=a

    return cpeshial_dict
