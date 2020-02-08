ans=True
while ans:
    print ("""
    1. Convert Miles to Kilometers
    2. Convert Kilometers to Miles
    3. Convert Pounds to Kilograms
    4. Convert Kilograms to Pounds
    5. Convert Farenheit to Celsius
    6. Convert Celsius to Farenheit
    7. Exit/Quit
    """)
    ans= input("What would you like to do? ") 
    # Miles to KM
    if ans=="1": 
      print("\n Miles to Kilometers") 
      ans = int(input("Enter number of Miles: "))
      km = ans * 0.62
      print(km)
    # KM to Miles
    elif ans=="2":
      print("\n Kilometers to Miles") 
      ans = int(input('Enter number of kilometers: '))
      mi = ans / 1.6
      print(mi)
    #Pounds to Kilograms
    elif ans=="3":
      print('\n Pounds to Kilograms')
      ans = int(input('Enter weight in pounds: '))
      kg = ans * 2.2
      print(kg)
    elif ans=="4":
      print("\n Kilograms to Pounds")
      ans = int(input('Enter weight in kilograms: '))
      lbs = kg / 2.2
      print(lbs)
    elif ans=="5":
      print("\n Farenheit to Celsius")
      ans = int(input('Enter temperature in farenheit:'))
      cels = (ans - 32) * 5/9
      print(cels)
    elif ans=="6":
      print("\n Celsius to Farenheit")
      ans = int(input('Enter temperature in celsius:'))
      fht = (ans - 32) * 5/9
      print(fht)
    elif ans=="7":
      print("\n Goodbye") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 