print('MathHomeWork.py')

problem = input('Enter a task or q to exit:')

while (problem != 'q'):
    print('Answer to', problem, 'is equal', eval(problem))
    problem = input('Enter another task or q to exit:')