package com.example.expensetracker;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.net.URL;
import java.util.ResourceBundle;

public class ExpenseTrackerController implements Initializable {

//instance variables

    @FXML
    private Button addButton;

    @FXML
    private TextField amount;

    @FXML
    private ChoiceBox<String> amountCategoryDrop;

    @FXML
    private Button calcFinal;

    @FXML
    private TextField personal;

    @FXML
    private TextField personalTextField;

    @FXML
    private TextField savingsTextField;

    @FXML
    private TextField savings;

    @FXML
    private Button setButton;

    @FXML
    private TextField total;

    @FXML
    private ChoiceBox<String> typeExpenseDrop;

    private final String[] expenses = {"Utilities", "Personal", "Savings"}; // List of possible expenses

    @FXML
    private TextField utilities;

    @FXML
    private TextField utilitiesTextField;

    private Account account;

    public void setAccount(Account account){
        this.account = account;
    }

    // Create utilities, budget instances
    private BigDecimal utilitiesamt = new BigDecimal(0);
    private BigDecimal savingsamt = new BigDecimal(0);
    private BigDecimal personalamt = new BigDecimal(0);
    private BigDecimal budget = new BigDecimal(0);
    private BigDecimal utilitiesBudget = new BigDecimal(0);
    private BigDecimal personalBudget = new BigDecimal(0);
    private BigDecimal savingsBudget = new BigDecimal(0);

    // Method to update charts with data
    public void updateCharts(BigDecimal budget, BigDecimal personalamt, BigDecimal savingsamt, BigDecimal utilitiesamt) {
        this.budget = budget;
        this.personalamt = personalamt;
        this.savingsamt = savingsamt;
        this.utilitiesamt = utilitiesamt;
    }


//addExpensePressed method
    @FXML
    void addExpensePressed(ActionEvent event) {
        try{
            // When the button to add an expense is clicked, get the necessary information and display it
            BigDecimal total = new BigDecimal(this.total.getText());
            if (typeExpenseDrop.getValue() == null){throw new NumberFormatException();}
            if (typeExpenseDrop.getValue().equals("Utilities")){
                utilitiesamt = utilitiesamt.add(total);
                account.addUtility(Float.parseFloat(String.valueOf(total)));
            }
            else if (typeExpenseDrop.getValue().equals("Savings")){
                account.addSavings(Float.parseFloat(String.valueOf(total)));
            }
            else{
                account.addPersonal(Float.parseFloat(String.valueOf(total)));
            }
            utilities.setText(String.format("%.2f", account.getUtility()));
            savings.setText(String.format("%.2f",account.getSavings()));
            personal.setText(String.format("%.2f", account.getPersonal()));
        }
        // Catch exceptions where the input was incorrect
        catch (NumberFormatException e){
            total.setText("Enter amount");
            total.selectAll();
            total.requestFocus();
        }
    }

    //calculatePressed method
    @FXML
    void calculatePressed(ActionEvent event) {
        try {
            FXMLLoader loader = new FXMLLoader(getClass().getResource("ExpenseDisplay.fxml"));
            Parent root = loader.load();

            // Access the controller of ExpenseDisplay.fxml
            ExpenseDisplayController displayController = loader.getController();
            displayController.setAccount(account);
            displayController.update(budget);

            // Pass the data to the ExpenseDisplayController
        updateCharts(
                new BigDecimal(total.getText()),
                utilitiesamt,
                savingsamt,
                personalamt
        );


            Stage expenseDisplayStage = new Stage();
            expenseDisplayStage.setTitle("Expense Display");
            expenseDisplayStage.setScene(new Scene(root));


            expenseDisplayStage.show();


            ((Stage) calcFinal.getScene().getWindow()).close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //setBudgetPressed method
    @FXML
    void setBudgetPressed(ActionEvent event) {
        try{
            BigDecimal amount = new BigDecimal(this.amount.getText());
            if (amountCategoryDrop.getValue() == null){throw new NumberFormatException();}
            if (amountCategoryDrop.getValue().equals("Utilities")){
                account.addUtilityb(Float.parseFloat(String.valueOf(amount)));
            }
            else if (amountCategoryDrop.getValue().equals("Personal")){
                account.addPersonalb(Float.parseFloat(String.valueOf(amount)));
            }
            else{
                account.addSavingsb(Float.parseFloat(String.valueOf(amount)));
            }
            //Format and display output
            double budgetD = Double.valueOf(String.valueOf(budget));
            utilitiesTextField.setText(String.format("%.2f", 100.0*(account.getUtilityb()/account.getBudget())));
            personalTextField.setText(String.format("%.2f", 100.0*(account.getPersonalb()/account.getBudget())));
            savingsTextField.setText(String.format("%.2f", 100.0*(account.getSavingsb()/account.getBudget())));
        }
        catch (NumberFormatException e){
            amount.setText("Enter amount");
            amount.selectAll();
            amount.requestFocus();
        }
    }

    //initialize method. for dropdowns
    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        typeExpenseDrop.getItems().addAll(expenses);
        amountCategoryDrop.getItems().addAll(expenses);
    }
}
