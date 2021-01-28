def test(x):
    if(state[(x+1)%5]!=2 and state[(x+4)%5]!=2 and state[x]==1):
        state[x]=2
        flag[x]=1
    
def initialisation():

    for k in range(5):
    
        state[k]=0
        flag[k]=0
    

def pickup(x):
    state[x]=1
    test(x)
    if(state[x]!=2):
        flag[x]=0
    
    if(flag[x]==1):
        print("\n Philo is eating"+str(x+1)+"")
    
    else:
        print("\n Philo %d cannot eat now"+str(x+1)+"")
    
    
    

def putdown(x):
    state[x]=0
    test((x+1)%5)
    test((x+4)%5)
    print("\n Philo %d is thinking"+str(x+1))


state=[0]*5
flag=[0]*5
initialisation()
while(1):
    print(" \n Menu \n 1)Start Eat \n 2)Stop Eating \n 3)EXIT \n Enter Choice : ")
    ch=int(input())
    print("Enter the philosopher you want to interact with : ")
    n=int(input())
    if ch==1:
        pickup(n-1)
        
    elif ch==2:
        putdown(n-1)
       
    else:
        exit(0)        
    
