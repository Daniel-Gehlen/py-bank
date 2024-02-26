# Report: Development of a Banking System in Python

## Introduction
In response to a contract from a major bank to modernize their operations, we have developed a banking system in Python. This report outlines the methods employed, the results obtained, and concludes with an analysis of the system's performance and potential.

## Methods
The banking system was implemented using Python, focusing on three main operations: deposit, withdraw, and view statement. A `Banco` class was created to encapsulate the functionality of the system. The methods implemented include:
- `depositar`: Allows depositing positive values into the account.
- `sacar`: Permits up to three withdrawals per day, with a maximum limit of $500 per withdrawal.
- `extrato`: Displays a statement of all deposits, withdrawals, and the current account balance.

## Results
The system successfully performs the specified operations. Deposits and withdrawals are recorded and displayed accurately in the statement. The system enforces limits on withdrawals and provides appropriate error messages when necessary.

## Conclusion
The Python banking system fulfills the requirements set by the client. It provides a basic yet functional framework for managing account transactions. However, further enhancements could be made to improve error handling, optimize code structure, and implement additional features such as user authentication and persistent storage.

## Case Study: User Interaction
Consider a scenario where a user interacts with the banking system:
1. **Deposit**: The user deposits $1000 into their account.
2. **Withdrawals**: They make several withdrawals: $300, $600, $400, and $200.
3. **Statement**: Upon viewing their statement, they see all transactions listed, including deposits and withdrawals, along with the current balance.
