import random
import string
div=1
n=random.randrange(0,101)
print("I have a number between 1 and 100.")
num=input("Can you guess it?\nHint:Type the number you want to guess or type 'Clue' to get a clue.Type 'Lose' to give up.\nEnter your guess here:")
for chances in range(1,50,1):
    try:
        num1=int(num)66
        typeofi="int"
    except:
        num1=num
        typeofi="str"
    if typeofi=="int":
        if abs(num1-n)>50:
            print("That's too big!Try a smaller number with the help of clues...\n\n")
        elif abs(num1-n)<50:
            print("You are close!Use clues to get the answer faster...\n\n")
        if n>num1:
            print("My number is bigger than this!\n")
        else:
            print("My number is smaller than this!\n")
        if num1 == n:
            print("Hooray!You have guessed it right.The number was:",str(n)+"\nNumber of chances used:",str(chances))
            break
        else:
            print("Oops...do you want a Clue?If YES type 'Clue' on your next chance.")
            num=input("Can you guess it yet?")
    elif typeofi=="str":
        if num1 =="Clue":
            div=div+1
            if n%(div)==0:
                print("It is a multiple of "+str(div))
            else:
                print("It is not a multiple of "+str(div))
            num=input("Can you guess it yet?")
        elif num1 =="Lose":
            print("Tired?The answer was:",str(n))
            break
        else:
            print("Oops...do you want a Clue?Type Clue here...:")
            num=input("Can you guess it yet?")
