
#Roxana Villagomez
#Module 8 Lab Activities





#Problem 1

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a == b:
  print("Number a and b are equal")
elif a !=b:
  print("Numbers a and b are not equal")





#Problem 2
def compare10(x, y):  
    z = x + y

    if z > 10:
        print("The sum of", x, "and", y, "is greater than 10.")
    elif z < 10:
        print("The sum of", x, "and", y, "is less than 10.")
    else:
        print("The sum of", x, "and", y, "is equal to 10.")

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))





#Problem 3

def checkFunction(lst):

    if 5 in lst:
        print("Value 5 is present in that list")
    else:
        print("Value 5 is not present in that list")

checkfunction([1,2,3,4,5])
checkfunction([6,7,8,9,10])





#Problem 4


def checkleapyear(year):

    if (year % 4)== 0:
        if (year % 100)== 0:
            if (year % 400)== 0:
                print("{0} is a leap year".format(year))

            else:
                print("{0} is a leap year".format(year))

        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
              



#Problem 5

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname


    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
    
    def checks(self,p):
        print("Checks function")
        task = input("What is the character are going to do(climb,cook,write)")
        
        #Cook
        if task == "cook":
            if p.weaknesses == "small":
                print("The character can not cook")
                
            elif ('pan' in p.weapons) and ('groceries' in p.weapons):
                print("The character can cook")     
                
            else:
             print("The character will not Cook")
                
                
        #Climb        
        elif task == "climb":
            if p.weaknesses != "slow":
                print("The character can not climb the mountain")
                
            elif ('rope' in p.weapons) and ('coat' in p.weapons) and ("first aid kit") in p.weapons:
                print("The character can climb")
                
            else:
                print("The character will not climb a mountain")
                
        #Writing
        elif task == "write":
            if p.weaknesses != "confusion":
                print("The character can not write a book")
                
            elif ('pen' in p.weapons) and ('paper' in p.weapons) and ("idea") in p.weapons:
                print("The character can a write a book")
                
            else:
                print("The character will not write a book")
        
        
  
player1 = character('','','')
player1.nickname = 'Roxy'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
    
player1.checks(player1)
      




