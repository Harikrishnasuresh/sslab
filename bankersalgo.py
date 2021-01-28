process=int(input("enter the no. of process"))
resources=int(input("enter the nof resorces"))
a=list()
m=list()
print("enter the allocation matrix")
for i in range(process):
	s=input("process"+str(i)+":")
	l=s.split()
	t=list()
	if(len(l)==resources):
		for item in l:
			t.append(int(item))
		a.append(t)
	else:
		print("resources wrong ")
print("enter the max  matrix")
for i in range(process):
        s=input("process"+str(i)+":")
        l=s.split()
        t=list()
        if(len(l)==resources):
                for item in l:
                        t.append(int(item))
                m.append(t)
        else:
                print("resources wrong ")
n=list()
for i in range(process):
	l=list()
	for j in range(resources):
		temp=m[i][j]-a[i][j]
		l.append(temp)
	n.append(l)

avail=list()
print("enter the available resources")
s=input()
l=s.split()
if len(l)==resources:
	for i in l:
		avail.append(int(i))
else:
	print("wrong")
f=[0]*process
ans=[0]*process
ind=0
for k in range(process):
	f[k]=0
for k in range(5):
	for i in range(process):
		if (f[i]==0):
			flag=0
			for j in range(resources):
				if (n[i][j] >avail[j]):
					flag=1
					break
			if (flag==0):
				ans[ind]=i
				ind+=1
				for y in range(resources):
					avail[y]+=a[i][y]
				f[i]=1
print(ans)
