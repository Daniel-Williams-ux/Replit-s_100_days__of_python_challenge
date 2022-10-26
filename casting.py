'''
Generation Generator
What generation are you a part of?

Use this list to guide you.

Generation Name	Starting Birth Year	Ending Birth Year
Traditionalists	1925	1946
Baby Boomers	1947	1964
Generation X	1965	1981
Millenials	1982	1995
Generation Z	1996
'''

year = int(input("What year were you born? "))
if year >= 1925 and year <= 1946:
  print("You belong to the Traditionalists Generation")
  
elif year >= 1947 and year <= 1964:
  print("You belong to the Baby Boomers Generation")

elif year >= 1965 and year <= 1981:
  print("You belong to the Generation X Generation")

elif year >= 1982 and year <= 1995:
  print("You belong to the Millenials Generation")

elif year >= 1996 and year <= 2015:
  print("You belong to the Generation Z Generation")
  
else:
  print("Sorry I can not help you")
