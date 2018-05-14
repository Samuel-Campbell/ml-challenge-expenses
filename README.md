# Requirements
Before running the application run the following instructions to ensure all libraries and dependencies are installed.
* cd ../ml-challenge-expenses/
* python3 -r requirements.txt

# Running the app
* cd ../ml-challenge-expenses/src/
* python3 main.py

# Data Processing
For the purpose of this task, the employee.csv file seemed completely useless and was disregarded.  
*Note: After further inspection, I believe the employee role does play its part. Including it in the data would make the classifier better*

Within the trainig_data_example.csv the *date* and *emplyee id* also seemed useless.

The category column is used for outputs while all other subsequent columns are input data.

We notice that there are a combination of both numerical and string values in the table. For this reason, all output string types are re-mapped to integers while input string types are booleans.

Here are the unique string types:

### Outputs
```
['Travel' 'Meals and Entertainment' 'Computer - Hardware'
'Computer - Software' 'Office Supplies']
```

### Inputs
```
['Taxi ride' 'Team lunch' 'HP Laptop Computer' 'Microsoft Office'
'Dropbox Subscription' 'Coffee with Steve' 'Client dinner'
'Flight to Miami' 'Macbook Air Computer' 'iCloud Subscription' 'Paper'
'Dinner with potential client' 'iPhone' 'Airplane ticket to NY'
'Starbucks coffee' 'Dinner with client' 'Dinner'] 
```

```
['NY Sales tax' 'CA Sales tax']
```

## Final data visualization
Originally the input vector is instantiate to all 0's. All unique input string types are represented by a different column/dimension in the input vector. If information is present then the column representing the string becomes a 1 or else it stays 0. Numerical types are simply entered as is in their column.

After preprocessing the data, a json file is created in /ml-challenge-expenses/data/ where this sort of meta data about vector configurations can be found.


# ML Technique used
## Hypothesis
### Decision Trees 
Would have made sense if money spent was directly correlated to the category of prediction. (brackets of spent money). In this context, using continuous values didn't feel appropriate as spending 1000$ could indicate a very expensive dinner or a plane ticket. For this reason, the decision tree would have performed very poorly in my opinion (**in the long run with more data given the bias**).

### Support Vector Machines
Support vector machines are great at binary classification OR combinational results where 1 estimator is chosen for every classification. However, for this problem an output may have many values. The only option would be a one vs. rest classifier at which point I believe there are more elegant techniques for this approach. The SVM is hard to configure although it may still give higher accuracy given a small dataset than other techniques.

### Deep Learning (Chosen)
The Deep Learning classifier is excellent for this particular problem as it solves both problematic stated above. The classifier can predict multiple categories while updating feature weights in order to give context to the input data. For instance, 1000$ may signify travels, or luxury dinner (paid for many people) but that can't be determined unless there is context attributed to this dollar value. This is where decisions trees may fail in my opinion for this particular problem.

For the purpose of a quick demo/assignment as well as for the fact that there is a very limited amount of data available, I have opted to go with a simple feed forward network.

The epochs is set to 700, high enough to converge without trying to overfit the data. Note that setting the epoch to 1500 also yielded 83% thus showing forth that this is the classifier's limits in regards to the data collected.

### Random Forest
I think this classifier would have performed the best with small amounts of data. It is also a relatively safe approach for a first attempt at classification. I did not use this simply because I would assume that the system would have a very large amount of data from which ANN might outperform this technique given a full training set.


# Results
```
Test accuracy: 83.33333333333333%
Precision: [1.         0.77777778 1.         1.        ]
Recall: [0.5 1.  1.  0.5]
F1: [0.66666667 0.875      1.         0.66666667]

Confusion Matrix:
[[1 1 0 0]
 [0 7 0 0]
 [0 0 1 0]
 [0 1 0 1]]

```

# Interpretation
Some values of F1, Recall, and Precision are 1 or 0 which signifies that there simply isn't enough validation data. As for the accuracy, it is high enough for us to notice that there indeed is some correlation between spending habbits and its associated category. With more abundant information it would perhaps be possible to increase this value.

Furthermore, a small project as this one which took me around 2 hours to evaluate and code is sufficient to demonstrate whether machine learning can truly solve the problem. Because there are 5 possible outputs AND the accuracy is over 0.20% then we can assume that the prediction functioned without randomness.

Finally, I would of liked to verify the results by adding the employee roles. Unfortunately I did not think of it originally and they are not part of the inputs currently.

# Question 2
*Mixing of personal and business expenses is a common problem for small business. Create an algorithm that can separate any potential personal expenses in the training data. Labels of personal and business expenses were deliberately not given as this is often the case in our system. There is no right answer so it is important you provide any assumptions you have made*

I do not have time to work on this because I am in my final school semester (Not to mention that I am unavailable to accept this job offer in the coming month). However this sounds like an NLP problem with binary classification. Very easy to do with a large enough dataset of words which either relate to business expenses or personal expenses. Naive Bayes for this, it almost sounds plug and play. Recursive Neural Networks if you are feeling fancy.

Clustering was also an idea but it is a VERY bad one as there are no empirical evidence to compare the clusters to.
