dir=[]
fileno=0
k=1
while(k):
	print("1:create new file\n 2:delete file\n3:search file\n 4:display files")
	n=int(input())
	if (n==1):
		print("enter the file name to be created")
		fname=input()
		if fname  not in dir:
			dir.append(fname)
			fileno+=1
		else:
			print("file already exists")
	elif (n==2):
		print("enter the file name")
		fname=input()
		if fname in dir:
			dir.remove(fname)
			fileno-=1
		else:
			print("no such files")
	elif (n==3):
		print("enter the file to be searched")
		fname=input()
		if fname in dir:
			print("found")
		else:
			print("not found")
	elif (n==4):
		for i in dir:
			print(" \n"+i+"")
	else:
		print("invalid entry")
	k=input("enter 1 to continue  and 0 to stop")

