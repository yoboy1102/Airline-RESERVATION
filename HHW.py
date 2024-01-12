print(""" 
      WELCOME TO EMIRATES
                        fly better.....
             """)
airports = ['DCA', 'DEL', 'BSB', 'BER', 'DXB']
print(""" Airports available:
                 USA: Ronald Reagan Washington National Airport (DCA)
                 IND: Indira Gandhi International Airport (DEL)
                 BRA: Brasília International Airport (BSB)
                 GER: Berlin Brandenburg Airport (BER)
                 UAE: Dubai International Airport(DXB)
                 """)



while True:
    dept = input("ENTER YOUR DEPARTURE POINT (BY THE AIRPORT CODE ASSIGNED TO IT):-- ").upper()
    arv = input("ENTER YOUR ARRIVAL POINT (BY THE AIRPORT CODE ASSIGNED TO IT):-- ").upper()
    if dept and arv in airports:
        cond = True
    else:
        print ("invalid input")
        cond = False
    if cond== True:
        conf_1 = int(input(f"your  departure point is {dept} and arrival point is {arv} enter 1 to confirm or 0 to not confirm"))
        if conf_1 == 1:
            print("done")





        elif conf_1 == 0:
            n_dept = input("ENTER YOUR DEPARTURE POINT (BY THE AIRPORT CODE ASSIGNED TO IT):-- ").upper()
            n_arv = input("ENTER YOUR ARRIVAL POINT (BY THE AIRPORT CODE ASSIGNED TO IT):-- ").upper()
            if n_dept and n_arv in airports:
                cond = True
            else:
                print("invalid input")
                cond = False
            if cond:
                print("done")
            else:
                print("airport code invalid....server timed out")





    elif cond == False:
        dept = input("ENTER YOUR DEPARTURE POINT (BY THE AIRPORT CODE ASSIGNED TO IT):-- ").upper()
        arv = input("ENTER YOUR ARRIVAL POINT (BY THE AIRPORT CODE ASSIGNED TO IT):-- ").upper()
        print(f"departure: {dept}  arrival: {arv}")
        print("done")


