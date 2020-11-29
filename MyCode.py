import csv
import os.path
def choice_Delete():
    loop = True
    while (loop):
        entrydelete = input("Enter the description of the entry you would like to delete")
        with open('expenses.csv', 'r+') as file_del:
            fieldnames = ["Description","Category","Amount"]
            reader = csv.DictReader(file_del, fieldnames)
            filtered_output = [line for line in reader if line['Description'] != entrydelete] #checks the ines for all entries barring the one to be deleted
            file_del.seek(0) #goto top of file
            writer = csv.DictWriter(file_del, fieldnames)
            writer.writerows(filtered_output) #inputs all entries back into the file barring the ones to be removed
            file_del.truncate() #removes whitespace
            print("Entry successfully deleted")
            delchoice = int(input("Would you like to delete another entry? 1.yes / 2.no"))
            if delchoice == 2:
                file_del.close()
                loop = False
                editMode()

def editMode():
    if os.path.isfile("expenses.csv"):
        filechoice = int(input("1.add data / 2.delete data / 3.Return to menu "))
        if filechoice == 1:
            with open('expenses.csv', 'a', newline='') as file: #RUNS IF FILE EXITS.
                fieldnames = ["Description","Category","Amount"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                loop = True
                while (loop):
                    Description = input("Enter a description")
                    Category = input("Enter a category")
                    Amount = int(input("Enter an amount"))
                    writer.writerow({"Description" : Description,"Category": Category,"Amount":Amount})
                    usexit = input("add another entry? y/n")
                    if usexit == "n":
                        file.close()
                        loop = False
                        menu()
        elif filechoice == 2:
            choice_Delete()
        elif filechoice == 3:
            menu()
    else: #CREATE FILE IF IT DOESNT ALREADY EXIST
        with open('expenses.csv', 'w', newline='') as file:
            fieldnames = ["Description","Category","Amount"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader() #create top row containing fieldnames
            loop = True
            while (loop):
                Description = input("Enter a description")
                Category = input("Enter a category")
                Amount = int(input("Enter an amount"))
                writer.writerow({"Description":Description,"Category": Category,"Amount":Amount})
                usexit = input("add another entry? y/n")
                if usexit == "n":
                    file.close()
                    loop = False
                    menu()


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
