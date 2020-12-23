
firstName = input("Adınız: ")
lastName = input("Soyadınız: ")
age = int(input("Yaşınız: "))
dateOfBirth = input("Doğum tarihiniz: ")

list = [firstName, lastName, age, dateOfBirth]

for i in list:
    print(i)

if age < 18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")