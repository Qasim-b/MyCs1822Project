import java.util.Scanner
static Scanner kbd = new Scanner(System.in);
public class Mycode{
    public static void main (String [] args){
    System.out.println("testing github");
    boolean exit = false;
        while (!exit){
        System.out.println("1. Edit mode");
        System.out.println("2. Analysis mode");
        int choice = kbd.nextInt();
            if (choice == 1){
              // do something with classes
            }
            if (choice == 2){
              // something with edit class
            }


        }
    }
}

//Edit mode
//Analysis mode
//In edit mode, users can add and delete expense items. An expense item should include

//Description
//Category
//Amount
//Exiting edit mode should return the user to the initial menu.

//In analysis mode, the user will be shown summary data of the expenses they have entered. This will include

//Breakdown of expenditure by category.
//Average spend per item.
//Total expenditure.
