import csv
def editMode():
    with open('expenses.csv', 'w', newline='') as file: #probs need to check if exists aswell.
        writer = csv.writer(file)
        loop = True
        ID = 0
        while (loop):
            Description = input("Enter a description")
            Category = input("Enter a category")
            Amount = int(input("Enter an amount"))
            writer.writerow(["ID","Description", "Category", "Amount"])
            writer.writerow([ID, Description, Category, Amount])
            ID = ID + 1
            usexit = input("add another entry? y/n")
            if usexit == "n":
                loop = False
                menu()

def menu():
    print("""Menu:
1. Edit mode
2. Analysis mode""")
    choice = int(input("Choose either option '1' or '2' "))
    if choice == 1:
        editMode()

if __name__ == "__main__":
    menu()
