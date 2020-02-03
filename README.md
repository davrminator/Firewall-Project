# Illumio-Firewall
Coding Challange for Illumio Software Engineering Internship

- Created by Matthew Davin Kuangga
- Github: davrminator
- Made in 2 hours from 4:00pm to 6:00pm on Feb/1/2020 
- Execution of these classes and useful comments start at line 100 of the Firewall-Illumio.py file
- Made in Davis, California using Python 2.7


Interested-in = ["platform","policy","data team"]
//preference sorted by index

### Comments on the code & If I had more time:

- I tested this by making a CSV file based of the one in the prompt. That test file is in this repository named fw.csv
- If I had a little more time I would love to edit the accept_packet class function as it could be further imporved by making another function to make the process more modular
- I would also quick sort the lines on the .csv file based on attributes like "Outbound", "Inbound". I would do this sort before I run the search algorithm (implemented as a for loop). Sorting in this way could potentially cut the run time by half on bigger data sets with, for example, 500 thousand lines. Because then the search would be like binary search that would only consider half of the data set that matched the search argument. This change could potentialy make the search run time on average O(log n).
- Also, If i had more time, I would NOT make an array to store all of the values in the .csv file. This implementation of an array could take up a lot of space when the data in the .csv file would be say 500 thousand lines. I would instead run a for loop for every line of the .csv file and check if the values in that line matches with the user input. This implementation of an array would only be of index 4. Hence, much more efficient than the current implementation. This edit could make the space used by the array improve from potentially O(.CSV size) to become O(4) which is pretty much equal to O(1).
- I edited this code in Sublime Text using Python 2.7



