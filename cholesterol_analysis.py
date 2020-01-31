# interface


def LDL_analysis(LDL_level):
    if LDL_level >=190:
        return "Very High"
    elif 160 >= LDL_level > 189:
        return "High"
    elif 130 <= LDL_level <159:
        return "Borderline High"
    elif 130 >LDL_level:
        return "Normal"
        


def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Borderline low"
    else:
        return "Low"


def cholesterol_analysis():
    print("Cholesterol Analysis")
    HDLinput = input("Enter test results: ")
    test_info =  HDLinput.split("=")
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The level is {}".format(answer))
    elif test_info[0] == "LDL":
        answer = LDL_analysis(int(test_info[1]))
        print("The level is {}".format(answer))

def new_feature():
    pass 

def name_function():
    first_name = input("Enter the first name")
    last_name = input("Enter the last name")
    full_name = [first_name, last_name]
    print(full_name)

    
def interface():
    #choice = 0
    while True:
        print("Cholesterol Calculator")
        print("Options: ")
        print("   1 - Cholesterol Analysis")
        print(" 9  - Quit")
        choice = input("Enter your options: ")
        if choice == "9":
            return
        elif choice == "1":
            cholesterol_analysis()
        
def fever_check():
    fever = False
    for temperature in temp_list:
        if temperature > 98.6:
            fever = True
    return fever
    

if __name__ == "__main__":
    interface()
