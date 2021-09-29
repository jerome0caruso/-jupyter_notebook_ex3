#Write a function that prompts the user for their birth month and return there birthstone.
#If they input an invalid month tell them to try again
import datetime

def getBirth():
    stones={1:"Garnet", 2:"Amethyst", 3:"Aquamarine", 4:"Diamond", 5:"Emerald", 6:"Pearl", 7:"Ruby",8:"Peridot", 9:"Sapphire", 10:"Opal", 11:"Topaz", 12:"Turquoise"}
    months = ["january", "February", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    birthMonth = input("What is your birth Month? ").strip().lower()
    if birthMonth in months:
        print(stones[months.index(birthMonth) +1])
    else:
        print("try again!")    

getBirth()


# def trying():
#     stones={1:"Garnet", 2:"Amethyst", 3:"Aquamarine", 4:"Diamond", 5:"Emerald", 6:"Pearl", 7:"Ruby",8:"Peridot", 9:"Sapphire", 10:"Opal", 11:"Topaz", 12:"Turquoise"}
#     if stones.get(122):
#         print("true")
#     else:
#         print("False")    
# trying()        