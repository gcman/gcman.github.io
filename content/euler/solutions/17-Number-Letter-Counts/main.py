NUMS = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
		11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",
		20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
TEN_POW = ["one","ten","hundred","thousand","million","billion","trillion"]
UPPERCASE = True

def three_dig_name(n):
	if n in NUMS:
		return NUMS[n]
	else:
		name = []
		if n // 100 > 0:
			name.append(NUMS[n//100])
			name.append(TEN_POW[2])
		if n % 100 in NUMS:
			name.append(NUMS[n%100])
		else:
			if (n % 100) - (n % 10) > 0:
				name.append(NUMS[(n % 100) - (n % 10)]) # Tens digit
			if n % 10 > 0:
				name.append(NUMS[n % 10]) # Ones digit
		return " ".join(name)

def num_name(n):
	blocks = [(n // 1000**i) % 1000 for i in range(0,5)]
	name = []
	for i,block in enumerate(reversed(blocks)):
		if block > 0:
			block_name = three_dig_name(block)
			name.append(block_name)
			if i != 4:
				name.append(TEN_POW[-i-1])
	return " ".join(name)

T = int(input())
for _ in range(T):
	N = int(input())
	name = num_name(N)
	if UPPERCASE:
		name = name.title()
	print(name)