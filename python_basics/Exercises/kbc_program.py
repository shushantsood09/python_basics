# Create a program capable of displaying the questions to the users like KBC.
# Use list data type to store the questions and there correct ansers.
# Display the final amount the person is taking home after playing the game.

questions = [
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",3], 
[
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",2], [
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",3],[
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",3], 
[
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",2], [
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",3],[
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",3], 
[
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",2], [
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",3],[
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",3], 
[
    "Which language was use to create facebook ?",
    "Python", "Javascript", "Freanch", "C++",2],

levels = [1000,2000, 32000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

i =0
for i in range(0, len(questions)):
    question = questions[i]
    print(f'\n\nQuestion for Rs.{levels[i]}')
    print(question[0])
    print(f'a. {question[1]}           b. {question[2]}')
    print(f'c. {question[3]}           d. {question[4]}')
    reply = int(input("Enter your answer (1-4) "))
    if(reply == question[-1]):
        print("Correct answer, you have won Rs.", levels[i])
        if(i == 4):
            money = 10000
        elif(i ==9):
            money = 320000
    else:
        print("Wrong answer")
        break



