currency = raw_input("Please input the currency type ")
Number = input("Please input a number ")

if currency == "dollars":
    print "One dollar is 123.12 Yens"
    print "One dollar is .92 Euros" 
    print "Your amount in Yens is", Number*123.12
    print "Your amount in Euros", Number*.92 
    
elif currency == "yens":
    print "One Yen is .0081 US dollars"
    print "One Yen is .0074 Euros"
    
elif currency == "euros":
    print "One Euro is 1.09 US dollars" 
    print "One Euro is 134.42 Yens"

#if currency == "Dollars":
   # if number == 1:
    #    print "One dollar is 123.12 Yens"
     #   print "One dollar is .92 Euros"
