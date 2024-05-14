package com.example.expensetracker;
public class UtilityBudget extends Budget {
    /**
     * @Purpose: A subclass to allow for specification of the type of budget
     */
    private float totalBudget;

    public UtilityBudget(float totalBudget) {
        /**
         * @Purpose: Constructor for utility budget. Uses superclass value for totalBudget
         * @Param: (float) totalBudget: The total budget amount from the superclass
         */
        super(totalBudget);
    }
}
