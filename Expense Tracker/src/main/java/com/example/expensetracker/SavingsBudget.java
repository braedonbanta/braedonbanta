package com.example.expensetracker;
public class SavingsBudget extends Budget {
    /**
     * @Purpose: A subclass to allow for specification of the type of budget
     */
    private float totalBudget;

    public SavingsBudget(float totalBudget) {
        /**
         * @Purpose: Constructor for savings budget. Uses superclass value for totalBudget
         * @Param: (float) totalBudget: The total budget amount from the superclass
         */
        super(totalBudget);
    }
}
