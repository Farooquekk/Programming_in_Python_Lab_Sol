# Lab: File Operations - Read, Store, Manipulate, and Output Data to a File

In this lab, you will work with file operations: reading the contents of a file, writing specific contents to another file, and storing file contents in a list to allow for easy access and manipulation.  
<br><br>

> ### **Tips: Before you Begin**
> #### **To view your code and instructions side-by-side**, select the following in your VSCode toolbar:
> - View -> Editor Layout -> Two Columns
> - To view this file in Preview mode, right-click on this README.md file and select `Open Preview`
> - Select your code file in the file tree to open it in a new VSCode tab
> - Drag your assessment code files over to the second column 
> - Great work! You can now see instructions and code at the same time.
> - Questions about using VSCode? Please see our support resources [here](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
> #### **To run your Python code**
> - Select your Python file in the Visual Studio Code file tree
> - Right-click the file and select "Run Python File in Terminal" 
>   or use the play button in the upper right-hand corner of VSCode.  
    (Select "Run Python File in Terminal" in the provided button dropdown)
> - Alternatively, you can follow lab instructions that use python3 commands to run your code in the terminal.
> 

<br>

## There are three main objectives of this activity:
1. Create a function to read in a file.
2. Create a function for writing specific contents to a file.
3. Use lists to store file contents for easier data manipulation.
<br><br>

## Exercise Instructions:
<br>

1. Verify that the `sampletext.txt` and `file_ops.py` files exist and are present inside the project folder.  You can run the `file_ops.py` file by opening a terminal and executing the following command:
    ```
    python3 file_ops.py 
    ```


2. Modify the `file_ops.py` script to complete the `read_file()` function. This function should:
   - Open and read the contents of `sampletext.txt`.
   - Return the entire contents of the file as a string.<br></br>

3. Modify the `file_ops.py` script to complete the `read_file_into_list()` function. This function should:
   - Read `sampletext.txt` line-by-line.
   - Store each line as an element in a list and return this list.<br></br>

4. Modify the `file_ops.py` script to complete the `write_first_line_to_file()` function. This function should:
   - Accept two arguments:
     - **file_contents** (a string with multiple lines of content).
     - **output_filename** (the name of the output file).
   - Write only the first line of `file_contents` into the specified output file.  
     (Identify the first line as everything before the first newline character, `\n`).<br></br>

5. Modify the `file_ops.py` script to complete the `read_even_numbered_lines()` function. This function should:
   - Read `sampletext.txt` line-by-line.
   - Return a list containing only the even-numbered lines (lines 2, 4, 6, etc.) based on the line number in the file.<br></br>

6. Complete the `read_file_in_reverse()` function. This function should:
   - Read `sampletext.txt` and store its lines in reverse order.
   - Return a list of the lines in reverse order.

<br>

## Final Step: Submit Your Code!
Nice work! To complete this assessment:
- Save your file through File -> Save 
- Select "Submit Assignment" in your Lab toolbar. 

Your code will be autograded and feedback will be returned shortly under the "Grades" tab.  
You can also see your score in your Programming Assignment "My Submission" tab.
<br><br>
