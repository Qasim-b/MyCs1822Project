import csv
import os.path
def editMode():
    if os.path.isfile("expenses.csv"):
        with open('expenses.csv', 'a', newline='') as file: #probs need to check if exists aswell.
            writer = csv.writer(file)
            loop = True
            while (loop):
                Description = input("Enter a description")
                Category = input("Enter a category")
                Amount = int(input("Enter an amount"))
                writer.writerow(["Description", "Category", "Amount"])
                writer.writerow([Description, Category, Amount])
                usexit = input("add another entry? y/n")
                if usexit == "n":
                    loop = False
                    menu()
    else:
        with open('expenses.csv', 'w', newline='') as file: #probs need to check if exists aswell.
            writer = csv.writer(file)
            loop = True
            while (loop):
                Description = input("Enter a description")
                Category = input("Enter a category")
                Amount = int(input("Enter an amount"))
                writer.writerow(["Description", "Category", "Amount"])
                writer.writerow([Description, Category, Amount])
                usexit = input("add another entry? y/n")
                if usexit == "n":
                    loop = False
                    menu()

def totalExpenditure(listOfExpenditure):
	total = 0

	for n in listOfExpenditure:
		total += n


	return total

def avgExpenditure(listOfExpenditure):

    total = 0
    nItems = 0

    for n in listOfExpenditure:
    	total += n
    	nItems += 1


    return total / nItems


def performAnalysis():

	totalExpenditure = 0
	nExpenses = 0
	catagories = {}

	with open('expenses.csv', 'r', newline='') as expenses:
		reader = csv.DictReader(expenses)
		for record in reader:
				# print(record['Description'], record['Category'], record['Amount'])
				totalExpenditure += int(record['Amount'])
				if (record['Category'] not in catagories):
					catagories[record['Category']] = int(record['Amount'])
				elif (record['Category'] in catagories):
					catagories[record['Category']] += int(record['Amount'])
				nExpenses += 1

	averageExp = totalExpenditure / nExpenses


	print("\nExpenditure by catagory:")
	for key in catagories:
		print(key, " : ", catagories[key])

	print("\nAverage Expenditure: " + str(averageExp))

	print("\nTotal Expenditure: " + str(totalExpenditure))

def menu():
    print("""Menu:
1. Edit mode
2. Analysis mode""")
    choice = int(input("Choose either option '1' or '2' "))
    if choice == 1:
        editMode()
    elif choice == 2:
        performAnalysis()

if __name__ == "__main__":
    menu()
