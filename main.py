from utils import load_students, load_professions, get_student_by_pk,\
    get_profession_by_title,check_fitness

dict_students = load_students()

dict_prof = load_professions()

# Получив номер студента вывод его данных

d = int(input("Введите номер студента "))

name_dict = get_student_by_pk(d, dict_students)
if name_dict is None:
    print("Такого студента нет")
    quit()
else:
    name_student = name_dict['full_name']
    skills_student = " ".join(name_dict['skills'])
    skills_student_list = name_dict['skills']
    print(f"Студент: {name_student} Знает: {skills_student}")

# Выбор специальности

print(f"Выберите специальность для оценки студента {name_student}")
x = input().title()

prof_dict = get_profession_by_title(x, dict_prof)
if prof_dict is None:
    print("У нас нет такой специальности ")
    quit()
else:
    skills_prof = prof_dict['skills']

# Вывод пригодности студента

check_fitness_dict = check_fitness(skills_student_list,skills_prof)

print(f"Пригодность: {check_fitness_dict['fit_percent']}%")
s = " ".join(check_fitness_dict['has'])
v = " ".join(check_fitness_dict['lacks'])
print(f"{name_student} знает: {s}")
print(f"{name_student} не знает: {v}")