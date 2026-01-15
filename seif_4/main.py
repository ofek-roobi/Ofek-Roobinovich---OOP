
def func(x,y):

    status= False
    if x==0 or y==0:
        return False
    if x%y ==0 or y%x==0:
        status=True
    print(status)
        
    

def main():

    while True:
        x=int(input("enter a int num "))
        y=int(input("enter a int num "))
        if x==-1 or y==-1:
            break

        func(x,y)
if __name__=="__main__":
     main()

