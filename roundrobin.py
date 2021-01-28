def findwaitingtime(process,n,bt,wt,quantum):
	rem_bt=[0]*n
	for i in range(n):
		rem_bt[i]=bt[i]
	t=0
	while(1):
		done=True
		for i in range(n):
			if(rem_bt[i]>0):
				done=False
				if (rem_bt[i]>quantum):
					t+=quantum
					rem_bt[i]-=quantum
				else:
					t+=quantum
					wt[i]=t-bt[i]
					rem_bt[i]=0
		if (done ==True):
			break
def findturnaroundtime(process,n,bt,wt,tat):
	for i in range(n):
		tat[i]=wt[i]+bt[i]

def findavgtime(process,n,bt,quantum):
	wt=[0]*n
	tat=[0]*n
	twt=0
	ttat=0
	findwaitingtime(process,n,bt,wt,quantum)
	findturnaroundtime(process,n,bt,wt,tat)
	for i in range(n):
		print(""+process[i]+"\n"+"wt"+str(wt[i])+"\n"+"tat"+str(tat[i])+"\n\n")
		twt=twt+wt[i]
		ttat=ttat+tat[i]
	twt=twt/n
	ttat=ttat/n
	print("average  waiting time:"+str(twt)+"\n average turn around time:"+str(ttat)+"\n")

n=int(input("enter no of process:"))
process=[0]*n
bt=[0]*n
for i in range(n):
	process[i]=input("enter  process id:\n")
	bt[i]=int(input("enter burst time \n"))
quantum=int(input("enter tht time quantum"))
findavgtime(process,n,bt,quantum)
