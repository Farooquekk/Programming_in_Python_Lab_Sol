# Lab: Mapping key-values to Dictionary data structures

In this lab, you will use Python techniques to modify sequences using functions like `map()` and comprehensions for both lists and dictionaries. Your goal is to create usernames for employees at Little Lemon and organize employee initials and IDs in a dictionary for easy access.

### **Goal:**
Practice using Python's `map()` function and comprehensions to efficiently transform and organize data in lists and dictionaries.

### **Objectives:**
1. Use the `map()` function to apply a custom function to all elements in a list.
2. Apply list comprehension to create and format strings based on given conditions.
3. Use dictionary comprehension to create key-value mappings for organized data access.

---

> ### **Tips: Before you Begin**
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

1. **Open the `comprehensions.py` file** under the **PROJECT** folder.

2. **Run the script**.
   - Open a terminal by navigating to `Terminal > New Terminal`.
   - Execute the following command to run the script:
     ```bash
     python3 comprehensions.py
     ```

3. **Implement the `to_mod_list()` function**. 
   - Use the `map()` function to apply the `mod()` function to each element in `employee_list`.
   - Store the result in a variable called `map_emp`, convert it to a list, and return it.
   - **Note:** The `mod()` function formats each entry as `name_department`, for example, `"Lisa_Cold Storage"`.

4. **Implement the `generate_usernames()` function**.  
   - Use list comprehension and the `replace()` method to replace spaces with underscores (`_`) in `mod_list`.
   - Return the modified list of usernames.

5. **Implement the `map_id_to_initial()` function**.  
   - Use dictionary comprehension to map each employee's ID to the first letter of their name.
   - The resulting dictionary should use initials as keys and IDs as values.

---

## Final Step: Submit Your Code

To complete this assessment:
- Save your file via `File -> Save`.
- Select "Submit Assignment" in your Lab toolbar.

Your code will be autograded and feedback will be provided in the "Grades" tab.  
You can also see your score in the Programming Assignment "My Submission" tab.
