def enterage(age):
    if age<0:
        raise ValueError("only positive integers are allowed")
    if age%2==0:
        print("Age is even")
    else:
        print("age is odd")
try:
    num=int(input("Enter your age:"))
    enterage(num)
except ValueError:
    print("There should only be a positive integer no negative integers")
except:
    print("Something is wrong")            