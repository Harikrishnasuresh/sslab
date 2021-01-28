empty=int(input("enter the  no of buffer"))
l=[1,0,empty,0]
def wait(s):
	return s-1

def signal(s):
	return s+1

def producer(l):
	mutex=l[0]
	full=l[1]
	empty=l[2]
	count=l[3]
	mutex=wait(mutex)
	full=signal(full)
	empty=wait(empty)
	count=signal(count)
	l[0]=mutex
	l[1]=full
	l[2]=empty
	l[3]=count
	print("producer produced an item")
	l[0]=1
	return l
def consumer(l):
	mutex=l[0]
	full=l[1]
	empty=l[2]
	count=l[3]
	mutex=wait(mutex)
	full=wait(full)
	empty=signal(empty)
	count=wait(count)
	l[1]=full
	l[2]=empty
	l[3]=count
	print("product consumed by consumer")
	l[0]=1
	return l
while(1):
	print("enter 1:produce item   2:consume item    3:exit")
	s=int(input())
	if s==1:
		if l[0]==1 and  l[2]!=0:
			l=producer(l)
		else:
			print("buffer is full")
	elif s==2:
		if l[0]==1 and l[1]!=0:
			l=consumer(l)
	else:
		break

