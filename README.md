# MyCs1822Project
Created by Tyler Trembeth & Qasim Baig

The file is split up into 3 main functions, edit(+delete)-analysis-menu.

The menu acts as the primary point from which the other 2 functions are called.
The approach we took for data handling was to use a csv file to contain user input.
The edit functions job is to allow user input and modification of data in a csv file.
The user is prompted with an option to either add or delete data as well as a return to menu option.

Adding data is achieved by creating a expenses.csv file if one does not exist, then within a while
loop the user is prompted to input data into the required fields: Description - Category - Amount.
If the file already exists then the program branches of into a similar section of code where
data can be appended rather than a new file being created.

Within the edit function, a function for deleting data is called upon user selection
The delete data function opens the file to read from and write to.
The user is prompted to enter the description of the item they want to delete.
The program then stores all the rows of the csv file, barring the one the user wants to delete to a variable.
Then all the rows stored in the variable are written back into the file. leaving out the one the user wants to get rid off. Thus being deleted.

The analysis function was used to perform calculations on the data within the expenses csv's data. This was achieved by creating a function which initialises variables to zero and adds to them as each item is iterated over. The third variable initialised is a dictionary which is used to store each catagories total expenditure and is printed out as per the analysis requirements. 
