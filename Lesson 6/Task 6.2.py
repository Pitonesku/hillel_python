# ДЗ 6.2. Конвертер із числа в дату
# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
# Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення.
# Слово "день" підбирається на основі кількості днів, а години, хвилини і секунди повинні заповнюватися нулями при одноцифрових значеннях.
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек. Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів, годин, хвилин, а те що залишиться - це секунди, які менше 60 ;)
# Доповнити провідними нулями можна за допомогою методу zfill(2)

import string

while True:
        number = input("Please input number to convert to time format, or type 'exit' to exit:\n")
        if number.isdigit():
                number = int(number)
                min, sec = divmod(number, 60)
                hours, min = divmod(min, 60)
                days, hours = divmod(hours, 24)
                years, days = divmod(days, 365)

                if years % 10 == 1 and years % 100 != 11:
                        years_word = "Рik"
                elif 2 <= years % 10 <= 4 and not (12 <= years % 100 <= 14):
                        years_word = "Роки"
                else:
                        years_word = "Рокiв"

                if days % 10 == 1 and days % 100 != 11:
                        days_word = "День"
                elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
                        days_word = "Днi"
                else: 
                        days_word = "Днiв"
                print(f"{years if years >0 else ""} {years_word if years > 0 else ""} {days if days > 0 else ""} {days_word if days > 0 else ""} {hours:02}:{min:02}:{sec:02}")
                break 
        elif number == "exit":
                break
        else: print("Wrong input\n")
        continue