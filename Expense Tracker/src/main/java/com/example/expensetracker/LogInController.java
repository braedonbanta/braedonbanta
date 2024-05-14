package com.example.expensetracker;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;

public class LogInController {

    @FXML
    private Button logInbutton;

    @FXML
    private TextField password;

    @FXML
    private TextField username;

    protected Account account;


    @FXML
    void loginPressed(ActionEvent event) { // Make sure username and password are entered
        /**
         * @Purpose: Controls event when the login button is pressed
         * @Param: (ActionEvent): The event that happens when clicked
         */
        try {
            if (username.getText().isBlank() || password.getText().isBlank()){
                throw new IllegalArgumentException();
            }

            FXMLLoader loader = new FXMLLoader(getClass().getResource("ExpenseTracker.fxml"));
            Parent root = loader.load();
            ExpenseTrackerController control = loader.getController();

            //Create scene and title
            Stage expenseTrackerStage = new Stage();
            expenseTrackerStage.setTitle("Expense Tracker");
            expenseTrackerStage.setScene(new Scene(root));


            expenseTrackerStage.show();
            account = new Account(username.getText(), password.getText());
            control.setAccount(account);

            ((Stage) logInbutton.getScene().getWindow()).close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        catch (IllegalArgumentException e){ // Make sure username and password are entered correctly
            username.setText("Enter Username");
            username.selectAll();
            username.requestFocus();
            password.setText("Enter Password");
            password.selectAll();
        }
    }

}

