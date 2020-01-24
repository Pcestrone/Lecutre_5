# interface

def cholesterol_analysis():
    print("Cholesterol Analysis")
    HDLinput = input("Enter test results: ")
    test_info =  HDLinput.split("=")
    if test_info[0] == "HDL":
        HDL_analysis()
        
    



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
        
if __name__ == "__main__":
    interface()