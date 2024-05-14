package com.example.expensetracker;
public class UtilityExpense extends Expense {
    /**
     * @Purpose: Allows the user to create an expense specifically under the UtilityExpense category
     */
    private String expenseType;
    private float totalExpense;

    public UtilityExpense(float totalExpense) {
        /**
         * @Purpose: Constructor for the UtilityExpense class
         * @Param: (float) totalExpense: The total expenses for this UtilityExpense object
         */
        super(totalExpense);
        this.expenseType = "Utility expense";
    }

    public String getType() {
        /**
         * @Purpose: Tells the user what kind of expense a given expense object is
         * @Return: (String) expenseType: The name of the type of expense
         */
        return this.expenseType;
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
    public void setTotalExpense(float totalExpense) {
        /**
         * @Purpose: Sets the new total expense for a given expense object
         * @Param: (float) totalExpense: The new total expense amount
         */
        this.totalExpense = totalExpense;
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
