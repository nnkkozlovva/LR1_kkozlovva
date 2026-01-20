numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
clean_numbers = numbers[:4] + numbers[5:] # список без  NONE

total_clean_numbers = sum(clean_numbers) # расчет суммы для нового чистого списка
count_of_numbers = len(numbers) # расчет кол-ва по исходному списку

average_numbers = total_clean_numbers / count_of_numbers # среднее арифмитическое как по заданию
numbers[4] = average_numbers # замена None на полученное значение

print("Измененный список:", numbers)
