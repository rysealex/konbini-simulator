class JapanFood:

    # class attributes
    konbini = {}

    # constructor
    def __init__(self, name, cost, quant):
        self.name = name
        self.cost = cost
        self.quant = quant
        JapanFood.konbini[name] = self

    # method to print total cost
    def print_total_cost(self):
        print(f"Total Cost: \t${self.cost * self.quant}\n")

    # method to print the details
    def print_details(self):
        print(f"Japanese Food: \t{self.name}\nCost Per {self.name}: ${self.cost}\nQuantity: \t{self.quant}")

    # method to display all food currently in konbini
    def get_konbini_food():
        if not JapanFood.konbini:
            print("No food items in the konbini right now!\n")
            return
        print(f"Konbini currently has {len(JapanFood.konbini.items())} item(s):\n")
        for name, food in JapanFood.konbini.items():
            food.print_details()
            print()

    # method to print the instructions
    def print_instr():
        print("Instructions:\n1: to add new food\n2: to get konbini info\n3: to exit simulation\n")

# create new instances of JapanFood
#sushi = JapanFood("Salmon Sushi", 2.50, 5)
#ramen = JapanFood("Pork Ramen", 3.75, 2)

# get konbini info
#JapanFood.get_konbini_food()

# start simulation
print("Welcome to the Konbini Simulation\n")

while True:
    
    # print instructions and get user choice
    JapanFood.print_instr()
    choice = input("Your choice: ")
    print()

    # check the choice
    if choice == '1':
        name = input("Enter food name: ")
        cost = input("Enter food cost: ")
        quant = input("Enter food quantity: ")
        newFood = JapanFood(name, cost, quant)
        print(f"{name} added successfully\n")
    elif choice == '2':
        JapanFood.get_konbini_food()
    elif choice == '3':
        print("Exiting the simulation")
        break
    else:
        print("Try again\n")
    






