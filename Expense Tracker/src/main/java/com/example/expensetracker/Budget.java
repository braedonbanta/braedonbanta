/**
 * @Purpose: Allows for the creation of a budget object
 * @DueDate: 11/26/2023
 */
package com.example.expensetracker;
public class Budget {
    /**
     * @Purpose: Allows the user to instantiate a budget object. Uses polymorphism to set the correct type of budget
     */

    private float totalBudget;

    public Budget(float totalBudget) {
        /**
         * @Purpose: Constructor for budget superclass
         * @Param: (float) totalBudget: the new budget allotted
         */
        this.totalBudget = totalBudget;
    }

    public void setTotalBudget(float totalBudget) {
        /**
         * @Purpose: Sets the entire budget to one value for a category
         * @Param: (float) totalBudget: the new budget allotted
         */
        this.totalBudget = totalBudget;
    }

    public float getTotalBudget() {
        /**
         * @Purpose: Returns the total budget amount to the user
         * @Return: (float) totalBudget: the current totalBudget
         */
        float currentBudget = this.totalBudget;
        return currentBudget;
    }

    public void addToBudget(float amountToAdd) {// May not need, only if there is an option to add a certain amount to budget
        /**
         * @Purpose: Adds a new value to the current budget without completely replacing the budget amount
         * @Param: (float) amountToAdd: The amount that the budget should be increased by
         */
        this.totalBudget+=amountToAdd;
    }
}


