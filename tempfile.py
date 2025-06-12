lst = [1, 2, 2, 3, 4, 4, 5] 
lst2 = []

for num in lst:
	if num not in lst2:
		lst2.append(num)

print(lst2)
