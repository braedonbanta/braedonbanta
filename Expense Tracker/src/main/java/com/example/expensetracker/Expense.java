/**
 * @Purpose: Class file for utilizing expenses
 * @DueDate: 11/26/2023
 */
package com.example.expensetracker;
public class Expense {
    /**
     * @Purpose: Superclass of each expense type. Allows for general creation of expenses
     */
    private float totalExpense;
    private String expenseType = "General Expense"; // This will always be changed when changed into a subclass

    public Expense (float totalExpense) {
        /**
         * @Purpose: Constructor for the expense class
         * @Param: (float) totalExpense: The total amount of the expense
         */
        this.totalExpense = totalExpense;
    }

    public void setTotalExpense(float totalExpense) {
        /**
         * @Purpose: Sets the total expense for the given expense object
         * @Param: (float) totalExpense: The new total expense for this object
         */
        this.totalExpense = totalExpense;
    }
    public void addtotalExpense(float totalExpense) {
        /**
         * @Purpose: Add to total expense
         * @Param: (float) totalExpense: The new total expense for this object
         */
        this.totalExpense+=totalExpense;
    }

    public float getTotalExpense(){
        /**
         * @Purpose: Returns the total expense for a given expense object
         * @Return: (float) totalExpense, the current total expense for this object
         */
        return this.totalExpense;
    }
}


