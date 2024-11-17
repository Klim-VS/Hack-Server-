import random
import string

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

str1 = generate_random_string(10)
str2 = generate_random_string(10)

combined_str = str1 + str2

result_str = ''.join(char for char in combined_str if not char.isdigit())

print("Перший рядок:", str1)
print("Другий рядок:", str2)
print("Об'єднаний рядок без цифр:", result_str) 