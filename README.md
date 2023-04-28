# Database_to_CSV
  
This repository takes data from a database stored in MySQL and commits it to a CSV file.  
  
Steps:  
1) First I create imaginary laboratory HPLC data in MySQL by running the Data.sql file in MySQL RDBMS
2) Then I use python to connect to the database, extract the data, and write the data to a CSV file. The CSV file gets named as the date.
3) [Optional] To automate the script to running daily, you can use Window's Task Schedule to automatically run at a certain time each day.  
a) Open Window's Task Scheduler  
b) Action --> Create Task...  
c) Give the trigger a name  
d) Trigger --> New --> Create a trigger that occurs daily  
e) Actions --> New... -->  
For "Program/script:", enter in your Python program's file.  
To find our Pythom program file location, type "where python" in the command line.  It will return your python location on your Window's computer  
For "Add arguments (optional)": main.py  
For "start in (optional)": put the location of main.py  
  
My "Edit Action" Entries:
Program/script: C:\Users\DTran\AppData\Local\Programs\Python\Python310\python.exe
Add arguments (optional): main.py
Start in (optional): C:\Users\DTran\Desktop\Coding\Python\Projects\Database to CSV
 


