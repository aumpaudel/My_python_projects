from functools import reduce
#functions and classes used in calculator:- 
def Adition_1(a,b):
    return a+b
def Modulo_2(a,b):
    return a%b 
def Subtraction_3(a,b):
    return a-b 
def Square_4(x):
    return x**2
def Multiplication_5(a,b):
    return a*b
def Squareroot_6(x):
    return x**(1/2)
def Division_7(a,b):
    return a/b
def Intrest_Calculator_8(p,r,t):
    return (p*r*t)/100
def Exponentiation_9(a,b):
    return a**b 
class Area_10():
    @staticmethod
    def square(n):
        return n*n
    @staticmethod
    def reactangle(l,b):
        return l*b
    @staticmethod
    def circle(r):
        return (3.14)*(r*r)
    @staticmethod
    def triangle (b,h):
        return (1/2)*b*h 
class Perimeter_11():
    @staticmethod
    def square(n):
        return 4*n 
    @staticmethod
    def reactangle(l,b):
        return 2*(l+b)
    @staticmethod
    def circle(r):
        return (3.14)*(r*2)
    @staticmethod
    def triangle (a,b,c):
        return a+b+c 
class Unit_Conversion_12():
    @staticmethod
    def celsius_fahrenheit(n):
        return (n - 32) * 5/9 
    @staticmethod
    def inches_centimeters(n):
        return n * 2.54
    @staticmethod
    def kilogram_pound(n):
        return n * 2.20462
    @staticmethod
    def liter_gallon(n):
        return n * 0.264172
class Corrency_Conversion_13():
    @staticmethod
    def usd_eur(n):
        return n * 0.85
    @staticmethod
    def usd_inr(n):
        return n * 83.50
    @staticmethod
    def eur_gbp(n):
        return n * 0.86
    @staticmethod
    def usd_jpy (n):
        return n * 157.3

#class shortcut 
A  = Area_10()
UC = Unit_Conversion_12()
CC = Corrency_Conversion_13()
P  = Perimeter_11()

#aking the operation user want to do in calculator
while True:   
    try:
        print('''The Function You need to use :-
        1. Addition ➕
        2. Modulo % 
        3. Subtraction ➖
        4. Square 
        5. Multiplication ✖️
        6. Squareroot √
        7. Division ➗
        8. Simple Intrest Calculator 🧮
        9. Exponentiation
        10.Area 
        11.Perimeter
        12.Unit Conversion 🔄
        13.Corrency Conversion 🔄''')
        print("")
        option = int(input("Enter Operation's Number you want to do in Calculator:- "))
        break
    except ValueError:
        print("Please use Integer number of option not anything else.")

#working of some operations 
while True:
    try:
        if(option==1):                                  #addition
            numbers = []
            while True:
                user_input = input("Enter the number:- ")
                if(user_input.lower()=="d"):
                    if numbers:
                        print("Your all numbers is recorded")
                        answer = reduce(Adition_1,numbers)
                        print(f"The Sum of all number = {answer}")
                        break 
                    else:
                        print("No numbers entered.")
                else:
                    try:
                        n = int(user_input)
                        numbers.append(n)
                    except ValueError:
                        print("ERROR: Please enter an integer or 'd' to finish.")
        elif(option==2):                                #modulo
            a = int(input("Enter your Divident:- "))
            b = int(input("Enter your Diviser:- "))
            answer = Modulo_2(a,b)
            print(f"Remainder after deviding {a} from {b} is {answer}")
            break
        elif(option==3):                                #subtraction
            numbers = []
            while True:
                user_input = input("Enter the number:- ")
                if(user_input.lower()=="d"):
                    if numbers:
                        print("Your all numbers is recorded")
                        answer = reduce(Subtraction_3,numbers)
                        print(f"The Subtraction of all number = {answer}")
                        break 
                    else:
                        print("No numbers entered.")
                else:
                    try:
                        n = int(user_input)
                        numbers.append(n)
                    except ValueError:
                        print("ERROR: Please enter an integer or 'd' to finish.")
        elif(option==4):                                #square
            x = int(input("Enter number whose square is needed:- "))
            answer = Square_4(x)
            print(f"square of number {x} is {answer}")
            break
        elif(option==5):                                #multipication
            numbers = []
            while True:
                print("d if all numbers are written")
                user_input = input("Enter the number:- ")
                if(user_input.lower()=="d"):
                    if numbers:
                        print("Your all numbers is recorded")
                        answer = reduce(Multiplication_5,numbers)
                        print(f"The Product of all number = {answer}")
                        break 
                    else:
                        print("No numbers entered.")
                else:
                    try:
                        n = int(user_input)
                        numbers.append(n)
                    except ValueError:
                        print("ERROR: Please enter an integer or 'd' to finish.")
        elif(option==6):                                #squareroot
            x = int(input("Enter number whose squareroot is needed:- "))
            answer = Squareroot_6(x)
            print(f"Squareroot of number {x} is {answer}")
            break
        elif(option==7):                                #division
            a = int(input("Enter your Divident:- "))
            b = int(input("Enter your Divisor:- "))
            answer = Division_7(a,b)
            print(f"Quotient after dividing {a} from {b} is {answer}")
            break
        elif(option==8):                                #simple intrest calculator
            p = int(input("Enter your principle value:- "))
            r = int(input("Enter your rate of intrest:- "))
            t = int(input("Enter your time in days:- "))
            answer = Intrest_Calculator_8(p,r,t)
            print(f"Simple intrest when Principle is {p}, rate of intrust is {r}% and time is {t}days is {answer}")
            break
        elif(option==9):                                #exponential
            a = int(input("Enter "))
            b = int(input("Enter "))
            answer = Exponentiation_9(a,b)
            print(f"{a}^{b} = {answer}")
            break
    except ValueError:
        print("Please use Integer number")

#operatins which need more information from user
while True:
    try:
        if(option==10):
            print("Select the figure whose Area is needed:- ")
            print("1. Square")
            print("2. Reactangle")
            print("3. Circle")
            print("4. Triangle")
            print("")
            option_10 = int(input("Enter Operation's Number you want to do in Calculator:- "))
            break
        elif(option==11):
            print("Select the figure whose Perimeter is needed:- ")
            print("1. Square")
            print("2. Reactangle")
            print("3. Circle")
            print("4. Triangle")
            print("")
            option_11 = int(input("Enter Operation's Number you want to do in Calculator:- "))
            break
        elif(option==12):
            print("Select the figure whose Unit Conversion is needed:- ")
            print("1. Fahrenheit to Celsius")
            print("2. Inches to Centimeters")
            print("3. Kilograms to Pounds")
            print("4. Liters to Gallons ")
            print("")
            option_12 = int(input("Enter Operation's Number you want to do in Calculator:- "))
            break
        elif(option==13):
            print("Select the figure whose Currency Conversion is needed:- ")
            print("1. USD to EUR")
            print("2. USD to INR")
            print("3. EUR to GBP")
            print("4. USD to JPY")
            print("")
            option_13 = int(input("Enter Operation's Number you want to do in Calculator:- "))
            break
    except ValueError:
        print("Please use Integer number of option not anything else.")

#working of leftover operations 
while True:
    try:
        #area
        if(option==10 and option_10==1):                        #square
            side = int(input("Enter the value of side of square:- "))
            answer = A.square(side) 
            print(f"Area of square of side {side} is {answer}")
            break 
        elif(option==10 and option_10==2):                      #reactangle
            length = int(input("Enter value of length of reactangle:- "))
            breadth = int(input("Enter value of length of reactangle:- "))
            answer = A.reactangle(length,breadth)
            print(f"Area of your reactangle of length and breadth {length}, {breadth} is {answer}.")
            break 
        elif(option==10 and option_10==3):                      #circle
            radius = int(input("Enter the value of radius of circle:- "))
            answer = A.circle(radius)
            print(f"Area of circle with radius {radius} is {answer}.")
            break 
        elif(option==10 and option_10==4):                      #triangle
            base = int(input("Enter the value of base of triangle:- "))
            height = int(input("Enter the value of height of triangle:- "))
            answer = A.triangle(base,height)
            print(f"Area of triangle whose base and height is {base}, {height} is {answer}.")
            break 

        #perimeter
        elif(option==11 and option_11==1):                        #square
            side = int(input("Enter the value of side of square:- "))
            answer = P.square(side) 
            print(f"Perimeter of square of side {side} is {answer}") 
            break 
        elif(option==11 and option_11==2):                      #reactangle
            length = int(input("Enter value of length of reactangle:- "))
            breadth = int(input("Enter value of length of reactangle:- "))
            answer = P.reactangle(length,breadth)
            print(f"Perimeter of your reactangle of length and breadth {length}, {breadth} is {answer}.")
            break 
        elif(option==11 and option_11==3):                      #circle
            radius = int(input("Enter the value of radius of circle:- "))
            answer = P.circle(radius)
            print(f"Perimeter of circle with radius {radius} is {answer}.")
            break 
        elif(option==11 and option_11==4):                      #triangle
            base = int(input("Enter the value of base of triangle:- "))
            height = int(input("Enter the value of height of triangle:- "))
            answer = P.triangle(base,height)
            print(f"Perimeter of triangle whose base and height is {base}, {height} is {answer}.")
            break 
        
        #unit conversion 
        elif(option==12 and option_12==1):                        #Fahrenheit to Celsius
            value = int(input("Enter the value:- "))
            answer = UC.celsius_fahrenheit(value)
            print(f"{value}Fahrenheit = {answer}Celsius") 
            break 
        elif(option==12 and option_12==2):                      #Inches to Centimeters
            value = int(input("Enter the value:- "))
            answer = UC.inches_centimeters(value)
            print(f"{value}Inches = {answer}Centimeters") 
            break 
        elif(option==12 and option_12==3):                      #Kilograms to Pounds
            value = int(input("Enter the value:- "))
            answer = UC.kilogram_pound(value)
            print(f"{value}Kilograms = {answer}Pounds") 
            break 
        elif(option==12 and option_12==4):                      #Liters to Gallons
            value = int(input("Enter the value:- "))
            answer = UC.liter_gallon(value)
            print(f"{value}Liters = {answer}Gallons") 
            break 

        #corrency conversion
        if(option==13 and option_13==1):                        #USD to EUR
            value = int(input("Enter the value:- "))
            answer = CC.usd_eur(value)
            print(f"{value}USD = {answer}EUR")  
            break 
        elif(option==13 and option_13==2):                      #USD to INR
            value = int(input("Enter the value:- "))
            answer = CC.usd_inr(value)
            print(f"{value}USD = {answer}INR") 
            break 
        elif(option==13 and option_13==3):                      #EUR to GBP
            value = int(input("Enter the value:- "))
            answer = CC.eur_gbp(value)
            print(f"{value}EUR = {answer}GBP") 
            break 
        elif(option==13 and option_13==4):                      #USD to JPY
            value = int(input("Enter the value:- "))
            answer = CC.usd_jpy(value)
            print(f"{value}USD = {answer}JPY") 
            break 
    except ValueError:
        print("Please use Integer Number.")