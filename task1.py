#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""
class pet:
    animal= ''
    breed= ''
    name= ''
    owner= ''
    birthdate= ''

    def __init__(self):
        self.animal= input("Type of animal? : ")
        self.vreed= input("What kind of breed? : ")
        self.name = input("Enter animal name: ")
        self.owner = input("Enter your name: ")
        self.birthdate = input("Enter animal birthdate(in the form of year-month-day): ")
    
    def display(self):
        print(self.name+''+self.animal)
        print(self.breed+' is owned by '+self.owner)

pets=[]

i=0
while True:
    print('1. Enter a new pet')
    print('2. Retrieve a pet')
    print('3. Exit')
    a=int(input('').strip())
    if a==1:
        pets.append(pet())
        continue
    elif a==2:
        b=input("which pet? : ")
        for i in pets:
            index=pets.index(i)
            if b == i.name:
                pets[index].display()
                break
    else:
        break
    