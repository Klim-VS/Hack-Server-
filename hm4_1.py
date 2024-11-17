#Написати програму, яка буде підраховувати суму всіх непарних чисел від 1 до 100. 
sum = sum(number for number in range(0, 100) if number % 2 != 0)
print (sum )