print("Welcome to Kaun Banega Karorpati")
Questions = ["What is the Capital of India", "What is the capital of MP", "Who is the PM of India", "Who is the president of BJP", "Who is the president of Congress"]

Options = [["Indore", "Mumbai", "Delhi", "Banglore"], ["Indore", "Bhopal", "Ujjain", "Burhanpur"], ["Amit Shah", "Narendra Modi", "Anurag Thakur", "Nitin Gadkari"], ["Amit Shah", "Narendra Modi", "J P Nadda", "Nitin Gadkari"], ["Rahul Gandhi", "Sachine Pilot", "Sonia Gandhi", "M L Kharge"]]

Answers = [3, 2, 2, 3, 4]
amount = 0
for i in range(len(Questions)):
    if i == 0:
        print(Questions[i])
        print(Options[i])
        Candidate_Answer = int(input("Please select your option from 1 to 4: "))
        if Candidate_Answer == Answers[i]:
            amount = amount + 50000
            print("Congratulation your answer is write, you won", "{:,}".format(amount))
        else:
            print("Your 1st answer was not right, better luck next time")
            break
    else:
        print(Questions[i])
        print(Options[i])
        Quit = int(input("Do you wanna quit (1 for Yes and 0 for No): "))
        if Quit == 1:
            print("Thank you for your participation, you won", "{:,}".format(amount))
            break
        else:
            # print(Options[i])
            Candidate_Answer = int(input("Please select your option from 1 to 4: "))
            # print(int(input("Please select your option from 1 to 4: ",)))
            if Candidate_Answer == Answers[i]:
                if i == 0:
                    amount = amount + 50000
                    print("Congratulation your answer is write, you won", "{:,}".format(amount))
                elif i == 1:
                    amount = amount + 50000
                    print("Congratulation your answer is write, you won", "{:,}".format(amount))
                elif i == 2:
                    amount = amount + 900000
                    # amount = "{:,}".format(amount)
                    print("Congratulation your answer is write, you won", "{:,}".format(amount))
                elif i == 3:
                    amount = amount + 4000000
                    print("Congratulation your answer is write, you won", "{:,}".format(amount))
                elif i == 4:
                    amount = amount + 5000000
                    print("Congratulation your Crorepati, you won 1 Crore", "{:,}".format(amount))
            else :
                print("Sorry your answer is wrong, better luck next time")
                if i == 1:
                    amount = amount - 25000
                    print("Sorry your answer was not right, Congratulations you won:", "{:,}".format(amount))
                    break
                elif i == 2:
                    amount = amount - 50000
                    print("Sorry your answer was not right, Congratulations you won:", "{:,}".format(amount))
                    break
                elif i == 3:
                    amount = amount - 500000
                    print("Sorry your answer was not right, Congratulations you won:", "{:,}".format(amount))
                    break
                elif i == 4:
                    amount = amount - 2500000
                    print("Sorry your answer was not right, Congratulations you won:", "{:,}".format(amount))
                    break
