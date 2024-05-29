def add(a, b):

def sub(a, b):

def mul(a, b):

def div(a, b):

def main():
	a = int(input("a ="))
	b = int(input("b ="))
	opertion = int(input("opertion ="))
	
	if opertion == 0:
		print(add(a, b))
	elif opertion == 0:
		print(sub(a, b))
	elif opertion == 0:
		print(mul(a, b))
	else:
		print(div(a, b))
	
if __name__ == "__main__":
    main()