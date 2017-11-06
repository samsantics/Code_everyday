num=input("Please enter a number: ")
new_num=int(num)-1
def multiples(new_num):
	total=0
	while new_num>0:
		if new_num%3==0 or new_num%5==0:
			total+=new_num
		print new_num
		new_num-=1
	return total
		
		
		

print multiples(new_num)