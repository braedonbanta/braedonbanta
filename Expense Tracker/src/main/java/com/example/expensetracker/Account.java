package com.example.expensetracker;


public class Account {
    //instance variables
    private String username;
    private String password;
    private UtilityExpense utility;
    private PersonalSpendingExpense personal;
    private SavingsExpense savings;
    private double leftover;
    private Expense[] expenses;
    private Budget[] budgets;
    private UtilityBudget utilityb;
    private SavingsBudget savingsb;
    private PersonalSpendingBudget personalb;

    //constructor
    public Account(String username, String password){
        this.username = username;
        this.password = password;
        utilityb = new UtilityBudget(0);
        savingsb = new SavingsBudget(0);
        personalb = new PersonalSpendingBudget(0);
        utility = new UtilityExpense(0);
        personal = new PersonalSpendingExpense(0);
        savings = new SavingsExpense(0);
        leftover = 0;
        expenses = new Expense[3];
        expenses[0] = utility;
        expenses[1] = personal;
        expenses[2] = savings;
        budgets = new Budget[3];
        budgets[0] = utilityb;
        budgets[1] = personalb;
        budgets[2] = savingsb;
    }

    //mutator
    public void setExpenses(Expense[] expenses){
        this.expenses = expenses;
    }
    public void addUtility(float d){
        utility.addtotalExpense(d);
    }
    public void addPersonalb(float d){personalb.addToBudget(d);}
    public void addSavingsb(float d){savingsb.addToBudget(d);}
    public void addUtilityb(float d){utilityb.addToBudget(d);}
    public void addPersonal(float d){personal.addtotalExpense(d);}
    public void addSavings(float d){
        savings.addtotalExpense(d);
    }
    public void addLeftover(double d){
        leftover+=d;
    }
    public void setUsername(String username){
        this.username = username;
    }
    public void setPassword(String password){
        this.password = password;
    }

    //accessor
    public float getExpenses(){
        float ret = 0;
        for(Expense e: expenses){
            ret+=e.getTotalExpense();
        }
            return ret;
    }
    public float getBudget(){
        float ret = 0;
        for(Budget e: budgets){
            ret+= e.getTotalBudget();
        }
        return ret;
    }

    public Expense[] getExpenseArray(){return this.expenses;}
    public double getUtility(){
        return this.utility.getTotalExpense();
    }
    public double getPersonal(){
        return this.personal.getTotalExpense();
    }
    public double getSavingsb(){
        return this.savingsb.getTotalBudget();
    }
    public double getPersonalb(){
        return this.personalb.getTotalBudget();
    }
    public double getUtilityb(){
        return this.utilityb.getTotalBudget();
    }
    public double getSavings(){
        return this.savings.getTotalExpense();
    }
    public double getLeftover(){
        return this.leftover;
    }
    public boolean isUsername(String username){
        return username.equals(this.username);
    }
    public boolean isPassword(String password){
        return password.equals(this.password);
    }
    protected String getUsername(){
        return this.username;
    }
    protected String getPassword(){
        return this.password;
    }

}
