def main():

    #Step 1

    Title = "Python Basic Commands Practice"

    print(Title)

    print("")

    #Step 2

    Date = "September 22, 2021"

    print(Date)

    print("")

    #Step 3
    
    num1 = 30
    num2 = 60
    
    print(num1 + num2)

    print("")

    #Step 4
    Students = [20,80,157]
    TrueNumber = False

    for i in range (len(Students)):
        print("There are currently " + str(Students[i]) + " number of students in the USG")
        TrueNumber = False
        if Students[i] == 157:
            TrueNumber = True
        print(TrueNumber)
            
        
    

if __name__ == "__main__":
    main()
