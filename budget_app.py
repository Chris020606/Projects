import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import Qt

class BudgetApp(QWidget):
    def __init__(self):
        super().__init__()

        self.expenses = []

        self.amount_label = QLabel("Enter a amount: ", self)
        self.amount_input = QLineEdit(self)
        self.description_label = QLabel("Enter a description: ", self)
        self.description_input = QLineEdit(self)
        self.submit_button = QPushButton("Enter", self)
        self.total_label = QLabel("Total: ", self)
        self.calculate_button = QPushButton("Calculate total", self)
        self.message_label = QLabel("", self)
        self.table = QTableWidget(self)
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Budget App")
        
        # Layouts
        hbox = QHBoxLayout()
        hbox.addWidget(self.amount_label)
        hbox.addWidget(self.amount_input)
        hbox.addWidget(self.description_label)
        hbox.addWidget(self.description_input)


        vbox = QVBoxLayout()
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.table)
        vbox.addWidget(self.total_label)
        vbox.addWidget(self.calculate_button)
        vbox.addWidget(self.message_label)
        # The vbox and hbox wasn't working so I need to make the main_layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(hbox)  # Add the horizontal layout
        main_layout.addLayout(vbox)  # Add the vertical layout
        
        self.setLayout(main_layout)

        # Place holder
        self.amount_input.setPlaceholderText("Amount")
        self.description_input.setPlaceholderText("Description")

        # Set CSS
        self.setStyleSheet(""" 
                           
                QPushButton, QLabel, QLineEdit{
                    padding: 10px;
                    font-weight: bold;
                    font-family: calibri;
                    font-size: 25px;   
                           }       
                QWidget{
                    background-color: rgb(233, 235, 234);
                           }
                QPushButton{
                    background-color: rgb(171, 174, 172);     
                           }
                
        """)
        self.table.setColumnCount(2) 
        self.table.setHorizontalHeaderLabels(["Amount", "Description"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setRowCount(0)  

        # Connect buttons
        self.submit_button.clicked.connect(self.submit)
        self.calculate_button.clicked.connect(self.calculate_total)
    
    def submit(self, message_label):
        
        amount = self.amount_input.text()
        description = self.description_input.text()
        
        if amount: 
            try:
                amount = float(amount) 
                self.expenses.append({"amount": amount, "description": description})
                # Add the entry to the table
                row_position = self.table.rowCount()
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(f"${amount:.2f}"))
                self.table.setItem(row_position, 1, QTableWidgetItem(description))

                self.message_label.setText(f"Submitted: ${amount:.2f} for {description}")
                self.reset()
            except ValueError:
                self.message_label.setText("Invalid amount. Please enter a valid number.")
        else:
            self.message_label.setText("Please enter an amount.")

    
    def reset(self):
        self.amount_input.clear()
        self.description_input.clear()
        
    def calculate_total(self):
        total = sum(expense["amount"] for expense in self.expenses)
        self.total_label.setText(f"Total: ${total:.2f}")

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    budget_app = BudgetApp()
    budget_app.show()
    sys.exit(app.exec_())
