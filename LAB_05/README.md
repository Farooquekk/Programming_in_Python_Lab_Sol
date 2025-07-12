# Lab Instructions: Abstract Classes and Methods

In this lab, you will create an abstract class for a bank and use it to develop a specific bank class. The abstract class will outline the essential structure, while the regular bank class will implement these methods to simulate bank functions.

### Goal:
To practice using Python's `ABC` and `@abstractmethod` decorators to create abstract classes and methods, and understand how to implement them in subclasses.

### Lab Objectives:
- Create an abstract base class.
- Define and implement abstract methods.
- Implement inheritance and method overriding.
- Handle data with class and instance variables.
- Perform conditional checks.
- Practice return values and print statements for outputs.

---

> ### **Tips: Before you Begin**
> 
> #### **To view your code and instructions side-by-side**, select the following in your VSCode toolbar:
> - View -> Editor Layout -> Two Columns
> - To view this file in Preview mode, right-click on this `README.md` file and select `Open Preview`.
> - Select your code file in the file tree to open it in a new tab, then drag it to the second column.
> - Great work! You can now see instructions and code at the same time.
> - Questions about using VSCode? Please see our support resources [here](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
> 
> #### **To run your Python code**
> - Right-click on your Python file in the file tree and select "Run Python File in Terminal".
> - Alternatively, use the play button at the top-right of VSCode and select "Run Python File in Terminal" from the dropdown.
> - Or, follow lab instructions to run your code using `python3` commands in the terminal.

---

## Exercise Instructions:

### Instructions:

1. Open the **`bank.py`** script present under the **PROJECT** folder. 

2. **Run the script**.
   - Open a terminal by navigating to `Terminal > New Terminal`.
   - Execute the following command to run the script:
     ```bash
     python3 bank.py
     ```

3. **Create a class called `Bank` and pass `ABC` to it.**
   - This will be an abstract base class (ABC) with methods that will be defined later in subclasses.

4. **Inside the `Bank` class, define two methods:**
   - **`basicinfo()`**: This function should print `"This is a generic bank"` and return `"Generic bank: 0"`.
   - **`withdraw()`**: Leave this function empty by adding a `pass` keyword under it. Mark it as an abstract method by placing `@abstractmethod` above the function declaration.

5. **Create a subclass called `Swiss` that inherits from `Bank`.**
   - This class will implement the `basicinfo` and `withdraw` methods with specific functionality.
   - **Define the constructor (`__init__`)**: Initialize an instance variable `bal` to 1000. 

6. **Override both methods from the `Bank` class in the `Swiss` class:**
   - **`basicinfo()`**: This function should print `"This is the Swiss Bank"` and return `"Swiss Bank: "` followed by the current balance (e.g., `"Swiss Bank: 80"` if `bal = 80`).
   - **`withdraw(amount)`**: Define a function called `withdraw` that accepts a parameter `amount` to withdraw.
     - **If `amount` is less than or equal to `bal`**: Deduct `amount` from `bal`, print the withdrawal amount and new balance, and return the new balance.
     - **If `amount` is greater than `bal`**: Print `"Insufficient funds"` and return the original balance.

---

### Example Walkthrough:

#### Setting up the `Bank` and `Swiss` classes:
- The `Bank` class is an abstract class, and `Swiss` inherits from it. The `bal` variable in `Swiss` is an **instance variable** because each instance of `Swiss` could have a different balance.

#### Expected Output Example:
1. Running `basicinfo()` on a `Swiss` instance should return `"This is the Swiss Bank"` and display the current balance.
2. Withdrawing an amount less than or equal to `bal` will update `bal`.
3. If trying to withdraw more than the balance, it will print `"Insufficient funds"` without updating `bal`.

---

## Final Step: Let's submit your code!
To complete this assessment:
- Save your file via `File -> Save`.
- Select "Submit Assignment" in your Lab toolbar.

Your code will be autograded and feedback will be provided in the "Grades" tab.  
You can also see your score in the Programming Assignment "My Submission" tab.
