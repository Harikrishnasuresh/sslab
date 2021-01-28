def findwaitingtime(process,bt,n,wt):
        wt[0]=0
        for i in range(1,n):
                wt[i]=bt[i-1]+wt[i-1]
                
def findturntime(process,bt,wt,n,tat):
        for i in range(n):
                tat[i]=wt[i]+bt[i]

def swap(process,bt):
	for j in range(n-1):
		for i in range(n-j-1):
			if(bt[i]>bt[i+1]):
				t=bt[i]
				bt[i]=bt[i+1]
				bt[i+1]=t
				k=process[i]
				process[i]=process[i+1]
				process[i+1]=k


def findavgtime(process,bt,n):
	wt=[0]*n
	tat=[0]*n
	twt=0
	ttat=0
	swap(process,bt)
	findwaitingtime(process,bt,n,wt)
	findturntime(process,bt,wt,n,tat)
	for i in range(n):
                twt=twt+wt[i]
                ttat=ttat+tat[i]
	twt=twt/n
	ttat=ttat/n
	for i in range(n):

                print(""+process[i]+":\n wt:"+str(wt[i])+"\n"+"tat"+str(tat[i])+"\n average turntime:"+str(ttat)+"\n average  waiting time:"+str(twt))












print("enter the no of entries")
n=int(input())
process=[0]*n
bt=[0]*n
for i in range(n):
        process[i]=(input())
        bt[i]=int(input())
findavgtime(process,bt,n)
