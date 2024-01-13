while True:
    print()
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print(" \t \t \t \t \t \t \tWELCOME TO ABC")
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print()

    while True:

        #Departure and Arrival points
        print("Departure and Arrival points ==>")
        airports = ['DCA', 'DEL', 'BSB', 'BER', 'DXB']

        print(""" Airports available:
                    USA: Ronald Reagan Washington National Airport (DCA)
                    IND: Indira Gandhi International Airport (DEL)
                    BRA: Brasília International Airport (BSB)
                    GER: Berlin Brandenburg Airport (BER)
                    UAE: Dubai International Airport(DXB)
                    """)
    
        print()
        dept = input("ENTER YOUR DEPARTURE POINT (BY THE AIRPORT CODE ASSIGNED TO IT):-- ").upper()
        arv = input("ENTER YOUR ARRIVAL POINT (BY THE AIRPORT CODE ASSIGNED TO IT):-- ").upper()
        print()

        
        #WORK ON dept and arv
        if dept in airports:
            if arv in airports:
                if dept == arv:
                    print("Domestic Flights Are Not Supported")
                    print("Press 'ENTER' to try again")    
                    input()
                print(f"Your  departure point is {dept} \nYour arrival point is {arv}")
                print()
                conf_1 = input("Enter 1 to Confirm \nEnter any key to Register again \n===> ")
                print()

                if conf_1 == '1':
                    print("Departure & Arrival points Confirmed!")
                    print("Press 'ENTER' to continue")
                    input()
                    break

                else:
                    continue
            else:
                print("Error, Invalid input.")
                print("Press 'ENTER' to try again")
                input()

    
        else:
            print("Error, Invalid input.")
            print("Press 'ENTER' to try again")
            input()
            
    print("============================================================================================================================================")
    print()
    
    while True:
        print("Number of Passengers ==> ")
        print()
        n_adults = int(input("Enter Number of Adults (16 or Above) in the Passenger`s list (Atleast 1):-- "))

        if n_adults <= 0:
            print()
            print("Atleast one Adult is Required to board the plane")
            print('Error, Invalid input.')
            print("Press 'ENTER' to try again")
            input()

        else:
            n_kids = int(input("Enter Number of Kids (Under-16) in the Passenger`s list:-- "))
            n_inf = int(input("Enter Number of Babies (Age 4 or below) in the Passenger`s list:-- "))
            print()
            n_seats = 42
            n_pass = n_kids+n_inf+n_adults
                            
            print(f"Number of Adults:-- {n_adults} \nNumber of Kids:-- {n_kids} \nNumber of Infants:-- {n_inf} \n\nTotal Number of Passengers:-- {n_pass} ")
            print()
        
            if n_pass > n_seats:
                print("Number of seats not available:")
                print("Press 'ENTER' to Register again")
                input()

            else:
                conf_1 = input("Enter 1 to confirm \nEnter any key to Register again \n===> ")
                print()
                if conf_1 == '1':
                    print("Confirmed!")
                    print("Press 'ENTER' to continue")
                    input()
                    break
                else:
                    continue

            


    print("============================================================================================================================================")
    print()
    #MONTH AND DATE
    while True:
        import calendar
        print("Date of Departure & Arrival ==> ")
        print()
        Months = ['January','February','March','April','May']
        year=2024
        print('The Available months for Reservation are ==> ')
        
        for i in range(len(Months)):
            print(Months[i])
        print()
        #Month
        month = input("SELECT A MONTH:-- ").capitalize()
        print()
        
        if month in Months:
            ind = Months.index(month)
            c_ind = ind+1
            c = calendar.TextCalendar(calendar.SUNDAY)
            cal = c.formatmonth(2024, c_ind)
            print(cal)
            break

        else:
            print('Error, Invalid input.')
            print("Press 'ENTER' to try again")
            input()
    while True:
        #Date
        if month == 'April':
            ndays = 30
        elif month == 'February':
            ndays = 29
        else:
            ndays = 31
    
        date = int(input("SELECT DATE:- "))
        print()
        
        ind_s=Months.index(month)+1
    
        if date > ndays or date < 0:
            print("ERROR, Invalid input")
            print("Press 'ENTER' to try again")
            input()
        
        
        else:
            DD,MM,YY = str(date),str(ind_s),str(year)
            d_form = 'DD/MM/YY'
            d_date = f"{DD}/{MM}/{YY}"
            
            print(f"Your Departure date is {d_date}, in the format {d_form}")
            print()
            conf_1 = input("Enter 1 to confirm \nEnter any key to Register again \n===> ")
            if conf_1 == '1':
                print("Date Confirmed!")
                print("Press 'ENTER' to continue")
                input()
                break
            else:
                continue

    print("============================================================================================================================================")
    print()

        #AVAILIBLITY OF FLIGHTS
    while True:
        print("FLIGHTS AVAILIBILITY")
        print("Currencies accepted ==>")
        L_cur = ['AED','USD','INR','GPB','EUR']

        for i in range(len(L_cur)):
            print(L_cur[i])

        cur = input("First, Please enter your preffered currency(by the ISO code):- ").upper
        if cur in L_cur:
            print('H')
            break

        

        pr1,pr2,pr3,pr4,pr5=1500,1680,1748,2400,3000
        
        

        from asciiSS import ALL, PLA
        al=ALL
        pl=PLA
        air = ['BER','','','','DEL','','','','BSB','','','','DCA','','','','DXB']
        
        ind_d = air.index(dept)
        ind_a = air.index(arv)

        print(f'\t\t','12 hour',f"\t\t",'Over-lay')
        print('--------------------------------------------------------------------------')
        for i in range(4):
        
            print('|','\t',ALL[ind_d],'\t',pl[i],'\t',ALL[ind_a],'\t','|')
            ind_d+=1
            ind_a+=1 

        print('--------------------------------------------------------------------------')

        print(f'\t\t{pr1}','INR',f"\t\t",'ECONOMY')


        
        
        
        
                                        


        
        

        
        
        
        
            















