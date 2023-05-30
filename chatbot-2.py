def greet(bot_name,birth_year):
    print("Hello ! My name is {0}.".format(bot_name))
    print("I was  Developed in {0}.".format(birth_year))
greet('AI_bot','2023' )

def remind_name():
    print('\n Please , Introduce your self.')
    name= input('enter your name:')
    print(' What a great name you have,{0}.'.format(name))
   
remind_name()

def designation():
    print("\n please enter your designation")
    desg=input("Enter your designation:")
    print("You are at nice post,{0}".format(desg))

designation()

def salary():
    print("\n please enter your salary")
    sal=int(input())
    if(sal<50000):
        print("you have a good salary")
    else:
        print("You have a great salary,{0}".format(sal))

salary()

def guess_age():
    print('Let me guess your age.')
    print("Enter remainders of dividing your age by 3,5 and 7 .")
    rem3=int(input())
    rem5=int(input())
    rem7=int(input())
    age=(rem3*70 + rem5*21 + rem7*15)%105
    print("your age is : {0}.".format(age))

guess_age()


def count():
    print("Now I will prove to you that I can count to any number you want.")
    num=int(input())

    counter=0

    while counter<=num:
        print("{0}".format(counter))
        counter+=1
    
        

count()



