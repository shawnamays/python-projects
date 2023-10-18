#lets plan a holiday together

destination = input("where do you want to go?")

guest1 = "Jasmine"
guest2 = "Andres"
guest3 = "Mia"

#provide the ages in separate variables

age1 = 31
age2 = 28
age3 = 24

#put the names of the people defined in a list, and their ages

nameList = [guest1, guest2, guest3]
ageList = [age1, age2, age3]

temp = 80

coldWeather = ("Bring a coat!")
hotWeather = ("Leave your coat home")

if temp < 70:
    print(coldWeather)

else:
    print(hotWeather)

nameList.append("Edgar")
ageList.append(23)

#check to see if someone is under 25, if they are, print their names

for a in range(0,len(ageList)):
    