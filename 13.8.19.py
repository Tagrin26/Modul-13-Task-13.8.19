ticket = int(input('Введите количество приобретаемых билетов: '))
amount = 0.0 # Вводим переменную которая показывает общую сумму
for i in range(ticket): # Запускаем цикл равный количеству билетов
    age = int(input('Введите возраст: ')) # Вводим возраст каждого, приобретающего билет
    if age < 18:  # Если возраст меньше 18 лет
        amount = amount + 0  # Сумма покупки не увеличивается (увеличивается на ноль)
    elif 18 <= age < 25:  # Иначе, если возраст от 18 лет включительно, до 25 лет
        amount = amount + 990  # Сумма покупки увеличивается на 990 руб.
    else: amount = amount + 1390  # Иначе (если возраст больше 25 лет), Сумма покупки увеличивается на 1390 руб.
    if ticket > 3:  # Вводим дополнительное условие, если количество приобретаемых билетов больше трёх
        amount = amount * 0.9  # То применяется скидка 10 % от общей суммы покупки
print('Итого'+ ' ' + str(round(amount)) + ' ' + 'рублей')  # Вывод строки с итоговой суммой за покупку билетов
