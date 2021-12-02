import math
import os
print("Pythagorean theorem in Python")
print("This Project's Source Code Is Also Available On My Website https://apurvasingh.ml")
print("Pythagorean theorem refers to Side A Squared + Side B Squared = Hypotenuse Squared ")
print("Note: Please Enter Single Units Only. Decimal Numbers and words Are Allowed. Thanks ")
SideA=int(input("Please Enter Side A "))
print("you have entered Side A as  ", SideA, "Units")
SideB=int(input("Please Enter Side B "))
print("you have entered Side B as ", SideB, "Units")
notfinal = SideA*SideA+SideB*SideB
final = math.sqrt(notfinal)
print("hypotenuse Is ", final, "Units3")
input("Press Any Key to exit")