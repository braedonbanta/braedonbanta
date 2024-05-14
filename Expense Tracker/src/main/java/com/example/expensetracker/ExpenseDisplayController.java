package com.example.expensetracker;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.chart.BarChart;
import javafx.scene.chart.PieChart;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;
import java.math.BigDecimal;

public class ExpenseDisplayController {

    @FXML
    private BarChart<?, ?> barChart;

    @FXML
    private TextField budgetDisp;

    @FXML
    private TextField leftOverDisp;

    @FXML
    private TextField expenseDisp;

    @FXML
    private PieChart pieDisp;

    @FXML
    private TextField totalPersonalDisp;

    @FXML
    private TextField totalSavingsDisp;

    @FXML
    private TextField totalUtilityDisp;

    @FXML
    private Button newBudgetbutton;

    private Account account;

    public void setAccount(Account account){
        this.account = account;
    }


    @FXML
    // When the budget button is clicked, set budget values and display percent breakdowns of budgets
    private void handleNewBudgetButtonClick(ActionEvent event) {
        /**
         * @Purpose: Controls what happens when a new budget is added
         * @Param (ActionEvent) event: The event that occurs
         */
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("ExpenseTracker.fxml"));
            Parent root = loader.load();
            ExpenseTrackerController control = loader.getController();

            Stage expenseTrackerStage = new Stage();
            expenseTrackerStage.setTitle("Expense Tracker");
            expenseTrackerStage.setScene(new Scene(root));


            expenseTrackerStage.show();
            account = new Account(account.getUsername(), account.getPassword());
            control.setAccount(account);

            ((Stage) newBudgetbutton.getScene().getWindow()).close();
        } catch (IOException e) {
            e.printStackTrace(); // Handle the exception appropriately
        }
    }
    //Update information on the final page
    public void update(BigDecimal budget){
        /**
         * @Purpose: Updates information on the final display page
         * @Param: (BigDecimal) budget, the total budget amounts
         */
        budgetDisp.setText(String.format("%.2f", budget));
        expenseDisp.setText(String.format("%.2f", account.getExpenses()));
        totalPersonalDisp.setText(String.format("%.2f", account.getPersonalb()));
        totalSavingsDisp.setText(String.format("%.2f", account.getSavingsb()));
        totalUtilityDisp.setText(String.format("%.2f", account.getUtilityb()));
        leftOverDisp.setText(String.format("%.2f", account.getBudget()-account.getExpenses()));
    }
}
