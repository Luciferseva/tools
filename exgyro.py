import os
PI=3.14159265589723846
def main():
    #print(type(args))
    while(1):
        print("input 1 to select angle to lr ")
        print("input 2 to select lr to angel ")
        print("input 3 to quite the tool ")
        print("*"*20)
        args=input()
        if args==1:
            print "please input angle\r\n"
            angel1=float(input())
            print angel1
            lr=angel1*PI/180
            print "lr="+str(lr)
        elif args==2:
            print "please input lr"
            lr=float(input())
            print lr
            angle2=lr*180/PI
            print "angle="+str(angle2)
        elif args==3:
            break
        else:
            print "select error\r\n"
if __name__ == "__main__":

    main()
    pass