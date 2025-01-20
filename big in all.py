numbers = [10, 20, 5, 100, 50]
current_max_number = numbers[0]

for number in numbers:
    if number > current_max_number:
        current_max_number = number
print(current_max_number)