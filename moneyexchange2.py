currency = raw_input("Please input the currency type")
Number = input("Please input a number")

currency = raw_input("What is your currency?: (dollars/euros/yens)")
money = input("Please insert your amount:")
dollars = 0.00
euros = 0.00
yens = 0.00
    
elif currency == "dollars":
    euros = money * 0.92
    yens = money * 124.35
    print "Your $", money, "are: €", euros,"and ¥", yens
    
elif currency == "euros":
    dollars = money * 1.09
    yens = money * 135.39
    print "Your €", money, "are $", dollars,"and ¥", yens
elif currency == "yens":
    dollars = money * 0.0081
    euros = money * 0.0074
    print "Your ¥", money, "are: $", dollars,"and €",euros
else: 
    print "Select the correct currency, please try again" 
