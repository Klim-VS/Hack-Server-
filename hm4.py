grades = [75, 88, 92, 85, 69, 94, 78, 81, 99, 65]
average_grade = sum(grades) / len(grades)
excellent_count = sum(1 for grade in grades if grade >= 90)
increased_grades = [min(grade * 1.05, 100) for grade in grades]
print(f"Середня оцінка у класі: {average_grade:.2f}")
print(f"Кількість учнів, які отримали оцінку 'відмінно': {excellent_count}")
print(f"Новий список оцінок, збільшених на 5%: {increased_grades}") 