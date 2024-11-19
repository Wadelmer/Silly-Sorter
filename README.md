# Silly-Sorter
Silly sorter made by the TWENTY team.

## Description  
This interactive Python program allows the user to create a dictionary of data with numeric keys and values. Once created, the data can be filtered and sorted based on different conditions. It is useful for quickly and efficiently exploring small datasets.  

## Features  
- Collection of key-value pairs.  
- Input validation to ensure values are numeric.  
- Filtering of data using comparative operators (>, >=, <, <=).  

## How to Use the Program  
### Input the Data:  
1. Enter a key (any text).  
2. Enter an associated numeric value.  
3. Repeat the process to add more data.  
4. Leave the key field empty and press Enter to finish.  

### Filter the Data:  
#### Specify a comparison operator:  
##### >: Greater than  
##### >=: Greater than or equal to  
##### <: Less than  
##### <=: Less than or equal to  
#### Enter a numeric value as a condition.  
#### The program will display the data that meets the condition, sorted according to the operator.  

### Result:  
The filtered data will be displayed in a tabular format along with the size of the filtered dataset.  

## Example  
### Input:  

Insert key: Juan  
Insert value: 7  
Insert key: María  
Insert value: 4  
Insert key: Pedro  
Insert value: 6  
Insert key: Ana  
Insert value: 3  
Insert key:  

### Filter:  
Enter operation (>, >= or <, <=): >=  

Enter condition: 5  

### Output:  

------------  

Juan      :       7.0  

Pedro     :       6.0  

------------  
Size of filtered data: 2  

Showing values >= than 5  

### Another Filter:  
Enter operation (>, >= or <, <=): <  

Enter condition: 5  

### Output:  

------------  

María     :       4.0  

Ana       :       3.0  

------------  
Size of filtered data: 2  
Showing values < than 5 

## Notes  
- If you enter a non-numeric value, the program will display an error message and prompt you to try again.  
- You can restart the filtering process if you make a mistake in the input.  
