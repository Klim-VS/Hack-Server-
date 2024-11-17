#// 1. Є список ваги учнів в класі:
#weights = [46, 65, 60, 37, 42, 54]
#// Задача: знайти середню вагу для учнів, які важчі за 50 кг
#Середня вага учнів важчих за 50 кг=Сума всіх учнів які важчі за 50 кг, поділити на кількість учнів які важчі за 50 кг.
weights = [46, 65, 60, 37, 42, 54]
avarage_weight = sum(weights) / len(weights)
excellent_count = sum(1 for weight in weights if weight > 50)
total_weight_more_50 = sum(weight for weight in weights if weight > 50)
avarage_weight_more_50 = total_weight_more_50 / excellent_count 
print (avarage_weight_more_50) 