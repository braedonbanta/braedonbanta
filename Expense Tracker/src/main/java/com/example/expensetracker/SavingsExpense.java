package com.example.expensetracker;
public class SavingsExpense extends Expense {
    /**
     * @Purpose: Allows the user to create an expense specifically under the SavingsExpense category
     */
    private String expenseType;
    private float totalExpense;

    public SavingsExpense(float totalExpense) {
        /**
         * @Purpose: Constructor for the SavingsExpense class
         * @Param: (float) totalExpense: The total expenses for this SavigsExpense object
         */
        super(totalExpense);
        this.expenseType = "Savings expense";
    }

    public String getType() {
        /**
         * @Purpose: Tells the user what kind of expense a given expense object is
         * @Return: (String) expenseType: The name of the type of expense
         */
        return this.expenseType;
    }
@Override
    public void setTotalExpense(float totalExpense) {
        /**
         * @Purpose: Sets the new total expense for a given expense object
         * @Param: (float) totalExpense: The new total expense amount
         */
        this.totalExpense = totalExpense;
    }
@Override
    public void addtotalExpense(float totalExpense) {
        /**
         * @Purpose: Add to total expense
         * @Param: (float) totalExpense: The new total expense for this object
         */
        this.totalExpense+=totalExpense;
    }
    @Override
    public float getTotalExpense() {

        /**
         * @Purpose: Gives the user the current expense amount for a given expense object
         * @Return (float) totalExpense: The total dollar amount of a given expense
         */
        return this.totalExpense;
    }
}
