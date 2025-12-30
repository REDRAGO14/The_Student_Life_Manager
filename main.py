'''Name: Dagim_Yosef      ID:BITS/UGR/0026/26'''

def user_grades():
    subject_count = 0
    total_grade = 0
    while True:
        grade = input("enter a grade or type done to exit: ").lower()
        if grade == 'done':
            break
        elif grade.isdigit() :
            total_grade += int(grade)
            subject_count += 1
        else:
            print("Your input is invalid!Try again") 
    return subject_count, total_grade 

        

def average_calculator_calculator(subject_count, total_grade):
    if subject_count == 0:
        return 0
    average_calculator_grade = total_grade / subject_count
    return round(average_calculator_grade)

def performance_evaluation(average_calculator_grade):
    if average_calculator_grade >= 90:
        return "Excellent"
    elif average_calculator_grade >= 70:
        return "Good"
    else :
        return "Needs Improvement"
def expense_checker(budget, cost):
    if budget >= cost:
        return True
        
    else:
        return False
    
def controler():
    name = input("Enter Your Name: ").upper()
    budget = float(input('Enter your monthly budget:'))
    subject_count, total_grade = user_grades()
    average_calculator = average_calculator_calculator(subject_count, total_grade)
    performance = performance_evaluation(average_calculator)
    if expense_checker(budget ,float(input('Enter cost of a celebration meal: '))) == True:
        Affordabillity = "Yes, you can afford the celebration meal🎉"
    else:
        Affordabillity ="No, you can't afford the celebration meal🥺"
    print(f" \n\n\n\n       Name: -----{name}----- \n       TOTAL NUMBER OF SUBJECT: {subject_count} \n       Final_Average_Grade: {average_calculator} \n       Performance_Status: {performance} \n       Affordabillity: {Affordabillity} \n\n\n\n")
    
controler()
    


    

    

        

        


