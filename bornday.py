as_year_born = (int(input('В каком году родился АС Пушкин?: ')))
if as_year_born == 1799:
    as_day_born = (int(input('Какой день рождения АС Пушкина?: ')))
    if as_day_born == 6:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Не верный год')
