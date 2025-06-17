#1. Remove Duplicates Without Using Set
#Write a program that takes a list and removes all duplicates without converting it into a set.
'''
lst = [1, 2, 2, 3, 4, 4, 5] 
lst2 = []

for num in lst:
	if num not in lst2:
		lst2.append(num)

print(lst2)
'''
#2. Rotate List k Times to Right
#Rotate a list to the right by k steps.
def Rotation(lst):
	k = int(input("How many rotation : "))
	for rota in range(k):
		a = lst.pop(-1)
		lst.insert(0,a)
	print(lst)
Rotation([1, 2, 3, 4, 5])
