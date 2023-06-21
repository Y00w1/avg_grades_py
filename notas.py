'''The following code has different utilities according to the needs of the user,
who can select if he wants to know the average grades:
of a subject in the three cuts,
or a cut of a subject,
or the entire semester of various subjects.
Depending on what he selects, he will be asked for the corresponding grades:
if it is of a single matter in the 3 cuts,
he is asked if the percentages are evenly divided, if not, he's also asked to specify the averages,
and the grades that will be requested will be specified according to the indicated percentage;
if a cut of a subject is requested, it asks for the grades of said cut, with the same option of percentages above;
finally the entire semester of various subjects,
Only the number of subjects will be requested, and the final grade one of each one; there will not be asked for percentages, since this is equal'''

def main():
    print('Selecciona una opción: ')
    print('1. Calcula el promedio de una materia en los tres cortes')
    print('2. Calcula el promedio de un corte de una materia')
    print('3. Calcula el promedio de todo el semestre de varias materias')

    option = int(input('Ingresa la opción (1-3): '))
    
    #As there are no switch in python, we could use a dictionary instead
    options = {
        1: get_subj_avg,
        2: get_cut_subj_avg,
        3: get_many_subj_avg
    }

    # Call the selected function from the dictionary
    selected_function = options.get(option)
    if selected_function:
        selected_function()
    else:
        print("Invalid option. Please select a valid option.")
        main()

def same_weight(num_grades):
    grades = [float(input(f'ingrese la nota del corte {i +1}: '))for i in range(num_grades)]
    average = sum(grades)/num_grades
    print(f'La nota promedio de la materia es: {average}.')
        
def different_weight(num_grades):
    percentages = []
    grades = []
    total_perc = 0
    for i in range(num_grades):
        percentage = float(input(f'ingrese el porcentaje de la nota {i +1}: '))
        grade = float(input(f'ingrese la nota {i +1}: '))
        percentages.append(percentage)
        grades.append(grade)
        total_perc += percentage
    if total_perc != 100:
        print('Error: la suma de los porcentajes debe ser igual a 100.')
        get_subj_avg()
        return
    #join the list percentages and grades in couples
    grade_perc = zip(percentages, grades)
    #iterate over the couples and calculate the product of the grades * percentage / 100 for each couple
    weighted_grades = [percentage * grade / 100 for percentage, grade in grade_perc]
    average = sum(weighted_grades)
    print(f'La nota promedio es: {average}')

def get_subj_avg():
    equal_weight = input('¿Los porcentajes de las notas son iguales? (si/no): ')
    if equal_weight.lower() == 'si':
        same_weight(3)
    elif equal_weight.lower() == 'no':
        different_weight(3)
    else:
        print('Opción inválida')
        get_subj_avg()
        
        
def get_cut_subj_avg():
    num_grades = int(input('Ingresa el numero de notas del corte: '))
    equal_weight = input('¿Los porcentajes de las notas son iguales? (si/no): ')
    if equal_weight.lower() == 'si':
        same_weight(num_grades)
    elif equal_weight.lower() == 'no':
        different_weight(num_grades)
    else:
        print('Opción inválida')
        get_subj_avg()
    
def get_many_subj_avg():
    num_subj = int(input('Ingresa la cantidad de materias: '))
    subj_grades = [float(input(f'Ingresa la nota final de la materia {i+1}: ')) for i in range(num_subj)]
    average = sum(subj_grades)/num_subj
    print(f'La nota final de las {num_subj} materias es de {average}')

main()