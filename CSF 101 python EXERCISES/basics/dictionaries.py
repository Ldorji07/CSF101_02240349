name = 'Lhundup Dorji'
age = 18
heignt = 1.7
is_student = True

personal_info = {
    'name': name,
    'age': age,
    'height': heignt,
    'is_student': is_student
}
print(personal_info)

personal_info['Favorite_color']= 'blue'
print(personal_info)

try :
    print(personal_info['weight'])
except KeyError as e:
    print(f'Error:{e}')