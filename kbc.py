def welcome(name):
    print(f"{name} KBC me aapka swagat hai\n")

def rules():
    print('''-----RULES-----\n 
    1.You have 7 questions
    2.You have 4 options
    3.If your choice is correct ou get the prize money\n''')

def question_bank():
    price = 0
    q1 = "1.How much goals has ronaldo scored till now?\n (a)300\t (b)983\t (c)321\t (d)42\n"
    ans1 = "b" 
    price = ask_questions(q1,ans1,price)
    if price == -1:
        return print("You Failed")
    print(f"Your choice is correct/n You have won {price} ")

    q2 = "2.How many days in a leap year\n (a)365\t (b)364\t (c)366\t (d)367\n"
    ans2 = "c"
    price = ask_questions(q2,ans2,price)
    if price == -1:
        return print("You Failed")
    print(f"Your choice is correct/n You have won {price} ")
    
    q3 = "Which city is called th 'pink city'\n (a)Kerala\t (b)Jaipur\t (c)Mumbai\t (d)\n"
    ans3 = "b"
    price = ask_questions(q3,ans3,price)
    if price == -1:
        return print("You Failed")
    print(f"Your choice is correct/n You have won {price} ")

    q4 = "Largest river in the world\n (a)amazon\t (b)neil\t (c)ganga\t (d)yamuna\n"
    ans4 = "a"
    price = ask_questions(q4,ans4,price)
    if price == -1:
        return print("You Failed")
    print(f"Your choice is correct/n You have won {price} ")

    q5 = "Smallest country\n (a)India\t (b)Australia\t (c)Vatican\t (d)Kerala\n"
    ans5 = "c"
    price = ask_questions(q5,ans5,price)
    if price == -1:
        return print("You Failed")
    print(f"Your choice is correct/n You have won {price} ")

    print("Yor have won the game!!")

def ask_questions(question, answer, current_price):
    print(question)
    ans = input("Enter Your Answer:\n")
    if ans==answer:
        current_price += 10000000
        return current_price
    else:
        return -1

name = input("Enter Your Name:")
welcome(name)
choice = input("Are You Ready (y/n)\n")
if choice=="n":
    print("Thank You For Playing")
elif choice=="y":
    print("Thank You For joing the game\n Lets Start!!" )
rules()
question_bank()