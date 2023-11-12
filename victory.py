""" 'Ленин': 1870,
        'Сталин': 1878,
         'Леннон': 1940,
         'Гейтс': 1955,
         'Джобс': 1955"""
while True:
    answer_true = 0
    answer_false = 0
    borns = {'Ленин': 1870,
            'Сталин': 1878,
             'Леннон': 1940,
             'Гейтс': 1955,
             'Джобс': 1955}
    for born in borns:
#        print(born, borns[born])
        born_input = int(input('В каком году родился ' + born + '?'))
        if born_input == borns[born]:
            answer_true += 1
#            print("Yes", answer_true)
        else:
            answer_false += 1
#            print("No", answer_false)
    print('Количество правильных ответов:', answer_true)
    print('Количество ошибок:', answer_false)
    print('Процент правильных ответов:', answer_true*100/5)
    print('Процент неправильных ответов:', answer_false*100/5)
    answer_cont = input('Будем продолжать?')
    if answer_cont == 'Нет':
        break
