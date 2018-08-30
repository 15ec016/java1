def main():
	a=1
	b=int(input())
	for i in range(1,b):
		a=a*i
	print(a)
try:
	main()
except:
	print('invalid')
