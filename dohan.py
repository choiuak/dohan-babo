def add(a, b):
    return a+b
def sub(a, b):
    return a-b
    
def mul(a, b):
    return a*b
def div(a, b):
	return a/b

def main():
    print("도한 바보")

	a = int(input("a ="))
	b = int(input("b ="))
	opertion = int(input("opertion ="))
	
	if opertion == 0:
		print(add(a, b))
	elif opertion == 1:
		print(sub(a, b))
	elif opertion == 2:
		print(mul(a, b))
	else:
		print(div(a, b))
	
if __name__ == "__main__":
    main()
