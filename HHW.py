while True:
    print()
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print(" \t \t \t \t \t \t \tWELCOME TO SSA AIRWAYS")
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
                    print()
                else:

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
                print()

    
        else:
            print("Error, Invalid input.")
            print("Press 'ENTER' to try again")
            input()
            print()
            
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
            print()

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
                print()

            else:
                conf_1 = input("Enter 1 to confirm \nEnter any key to Register again \n===> ")
                print()
                if conf_1 == '1':
                    print("Confirmed!")
                    print("Press 'ENTER' to continue")
                    input()
                    print()
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
            print()
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
            print()
        
        else:
            DD,MM,YY = str(date),str(ind_s),str(year)
            d_form = 'DD/MM/YY'
            d_date = f"{DD}/{MM}/{YY}"
            
            print(f"Your Departure date is {d_date}, in the format {d_form}")
            print()
            conf_1 = input("Enter 1 to confirm \nEnter any key to Register again \n===> ")
            print()
            if conf_1 == '1':
                print("Date Confirmed!")
                print("Press 'ENTER' to continue")
                input()
                print()
                break
            else:
                continue

    print("============================================================================================================================================")
    print()

    #AVAILIBLITY OF FLIGHTS
    while True:
        print("FLIGHTS AVAILIBILITY")
        print()
        print("Currencies accepted ==>")
        L_cur = ['AED','USD','INR','GPB','EUR']
        L_ncur = ['Dirhams','American Dollars','Rupees','British Pounds','Euros']
        pr1,pr2,pr3,pr4,pr5 = 1500,1680,1748,2400,3000
        hr1,hr2,hr3,hr4,hr5 = 8,7,6,3,3

        for i in range(len(L_cur)):
            print(f"{L_ncur[i]} ({L_cur[i]})")

        cur = input("First, Please enter your preffered currency(by the ISO code):- ").upper()
        if cur in L_cur:
            if cur == 'GPB':
                pr1,pr2,pr3,pr4,pr5 = pr1,pr2,pr3,pr4,pr5
                break
            elif cur == 'AED':    
                pr1,pr2,pr3,pr4,pr5 = 3.6*pr1,3.6*pr2,3.6*pr3,3.6*pr4,3.6*pr5
                break
            elif cur == 'INR':
                pr1,pr2,pr3,pr4,pr5 = 82.8*pr1,82.8*pr2,82.8*pr3,82.8*pr4,82.8*pr5
                break
            elif cur == 'USD':
                pr1,pr2,pr3,pr4,pr5 = 1.27*pr1,1.27*pr2,1.27*pr3,1.27*pr4,1.27*pr5
                break 
            elif cur == 'EUR':
                pr1,pr2,pr3,pr4,pr5 = 1.15*pr1,1.15*pr2,1.15*pr3,1.15*pr4,1.15*pr5
                break
        else:
            print('ERROR, Invalid input')
            print("Press 'ENTER' to try again")
            input()
            print()
            continue
            
    while True:        
        from asciiSS import ALL, PLA
        al=ALL
        pl=PLA
        air = ['BER','','','','DEL','','','','BSB','','','','DCA','','','','DXB']
        
        ind_d = air.index(dept)
        ind_a = air.index(arv)
        f='A'

        print(f)
        print('------------------------------------------------------------------------')
        print(f'|\t\t',hr1,f'hour',f"\t\t",f'Over-lay  \t\t\t|')
        for i in range(4):
        
            print('|','\t',ALL[ind_d],'\t',pl[i],'\t',ALL[ind_a],'\t','|')
            ind_d+=1
            ind_a+=1 
        print(f'|\t\t{pr1}',cur,f"\t\t",f'ECONOMY  \t\t\t|')
        print('------------------------------------------------------------------------')

        ind_d = air.index(dept)
        ind_a = air.index(arv)
        f='B'

        print(f)
        print('------------------------------------------------------------------------')
        print(f'|\t\t',hr2,f'hour',f"\t\t",f'Over-lay  \t\t\t|')
        for i in range(4):
        
            print('|','\t',ALL[ind_d],'\t',pl[i],'\t',ALL[ind_a],'\t','|')
            ind_d+=1
            ind_a+=1 
        print(f'|\t\t{pr2}',cur,f"\t\t",f'ECONOMY  \t\t\t|')
        print('------------------------------------------------------------------------')

        ind_d = air.index(dept)
        ind_a = air.index(arv)
        f='C'

        print(f)
        print('------------------------------------------------------------------------')
        print(f'|\t\t',hr3,f'hour',f"\t\t",f'Over-lay  \t\t\t|')
        for i in range(4):
        
            print('|','\t',ALL[ind_d],'\t',pl[i],'\t',ALL[ind_a],'\t','|')
            ind_d+=1
            ind_a+=1 
        print(f'|\t\t{pr3}',cur,f"\t\t",f'ECONOMY  \t\t\t|')
        print('------------------------------------------------------------------------')

        ind_d = air.index(dept)
        ind_a = air.index(arv)
        f='D'

        print(f)
        print('------------------------------------------------------------------------')
        print(f'|\t\t',hr4,f'hour',f"\t\t",f'Over-lay  \t\t\t|')
        for i in range(4):
        
            print('|','\t',ALL[ind_d],'\t',pl[i],'\t',ALL[ind_a],'\t','|')
            ind_d+=1
            ind_a+=1 
        print(f'|\t\t{pr4}',cur,f"\t\t",f'ECONOMY  \t\t\t|')
        print('------------------------------------------------------------------------')

        ind_d = air.index(dept)
        ind_a = air.index(arv)
        f='E'

        print(f)
        print('------------------------------------------------------------------------')
        print(f'|\t\t',hr5,f'hour',f"\t\t",f'Over-lay  \t\t\t|')

        for i in range(4):
        
            print('|','\t',ALL[ind_d],'\t',pl[i],'\t',ALL[ind_a],'\t','|')
            ind_d+=1
            ind_a+=1 
        print(f'|\t\t{pr5}',cur,f"\t\t",f'ECONOMY  \t\t\t|')
        print('------------------------------------------------------------------------')

        select = input('Select Flight(by the letter assigned to it):-- ').upper()
        print()
        conf_1 = input("Enter 1 to confirm \nEnter any key to Register Again \n==> ")
        if conf_1 == '1':
            print("Confirmed")
            print("Press 'Enter' to continue")
            input()
            print()    
            break
        else:
            continue
    print("============================================================================================================================================")
    print()


    while True:
        #SEAT RESERVATION
        L = [['|A1|', '|B1|', '|C1|', '|D1|', '|E1|', '|F1|'], ['|A2|', '|B2|', '|C2|', '|D2|', '|E2|', '|F2|'], ['|A3|', '|B3|', '|C3|', '|D3|', '|E3|', '|F3|'], ['|A4|', '|B4|', '|C4|', '|D4|', '|E4|', '|F4|'], ['|A5|', '|B5|', '|C5|', '|D5|', '|E5|', '|F5|'], ['|A6|', '|B6|', '|C6|', '|D6|', '|E6|', '|F6|'], ['|A7|', '|B7|', '|C7|', '|D7|', '|E7|', '|F7|']]
        
        xx='|XX|'
        print('','  A ','  B ','  C ',' ','  D ','  E ','  F ')
        n = 1
        for i in range(len(L)):
            for m in range(1):
                print(n,L[i][m], L[i][m+1], L[i][m+2],' ',L[i][m+3], L[i][m+4], L[i][m+5])
                n += 1
        nmp = n_pass
        n2 = 1
        n3 = 1
        n4 = 0
        if nmp == 1:
            sea_t = input('Choose your seat from the available options:-- ')
            line = '|'
            seat = line + sea_t + line
            print(seat)
            conf_1 = input("Enter 1 to confirm \nEnter any key to Register again \n==> ")
            if conf_1 == '1':
                print()
                print("Seat reserved")
                print("Press 'ENTER' to continue")
                input()
                for i in range(7):
                    if seat in L[i]:
                        i2 = i
                    else:
                        n4 += 1
                if n4 >= 7:
                    print("ERROR, Invalid input")
                    print("Press 'Enter' to try again")
                    input()
                    print()
                else:
                
                    L2=L[i2]         
                    ind_st = L2.index(seat)        
                    L2[ind_st] = xx     
                    L[i2] = L2
                    break
                
            else:
                print("Press 'ENTER' to Register again")
                input()
                print()
                        
        else:
            for j in range(nmp):
                n4 = 0
                n2=1
                sea_t=input(f'Choose the seat for passenger {n2}:-- ')
                line = '|'
                seat = line + sea_t + line
                print(seat)
                n2 += 1

                conf_1 = input("Enter 1 to confirm \nEnter any key to Register again \n==> ")
                if conf_1 == '1':
                    print()
                    print("Seat reserved")
                    print("Press 'ENTER' to continue")
                    input()
                    for i in range(7):
                        if seat in L[i]:
                            i2 = i
                
                        else:
                            n4 += 1
                    if n4 >= 7:
                        print("ERROR, Invalid input")
                        print("Press 'Enter' to continue")
                        input()
                        print()
                    else:
                        L2=L[i2] 
                        ind_st = L2.index(seat)        
                        L2[ind_st] = xx
                        L[i2] = L2
                        print('','  A ','  B ','  C ',' ','  D ','  E ','  F ')
                        for i in range(len(L)):
                            for m in range(1):
                                    
                                    print(n3,L[i][m], L[i][m+1], L[i][m+2],' ',L[i][m+3], L[i][m+4], L[i][m+5])
                                    n3 += 1
                

                elif conf_1 != '1':
                    print("Press 'ENTER' to Register again")
                    input()
                    print()
                    break
                if j+1 == nmp:
                    break
                
                



        


        
        
        
        
                                        


        
        

        
        
        
        
            















