package com.example.expensetracker;
public class PersonalSpendingBudget extends Budget {
    /**
     * @Purpose: A subclass to allow for specification of the type of budget
     */
    private float totalBudget;

    public PersonalSpendingBudget(float totalBudget) {
        /**
         * @Purpose: Constructor for personal spending budget. Uses superclass value for totalBudget
         * @Param: (float) totalBudget: The total budget amount from the superclass
         */
        super(totalBudget);
    }
}
