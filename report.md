### Report 

### Introduction
This section should briefly state the aim of your study and include a paragraph about why this study is important according to you.

This study evaluates and compares the performance of different machine learning classifiers using two datasets. The classifiers we will compare are: Our own implementations of k-nearest neighbours with varying k and Naïve Bayes, as well as ZeroR, OneR, decision trees, random forest, support vector machines, neural networks, K-NN, and Naïve Bayes, all using Weka.

We will evaluate the classifiers by measuring accuracy (proportion of correctly classified examples) achieved by 10-fold stratified cross-validation. 


We will compare the classifiers by comparing the accuracies achieved. We will run a paired t-test to determine if one classifier is significantly better than another.  

### Data
This section should describe the datasets, mentioning the number of attributes and classes. You should also briefly summarise the similarities and differences between the datasets.
We are using two datasets: Pima Indian Diabetes Dataset (PID) and Room Occupancy Dataset (RO). 

PID has 8 numeric attributes and 2 classes (yes or no) spanning 768 instances. Each instance describes characteristics and test measurements of a patient of  Pima Indian heritage, with the yes/no class referring to whether or not they have diabetes. 

RO has 4 numeric attributes and 2 classes (yes or no) spanning 2,025 instances. Each instance describes the sensor readings  (light, temperature, sound and CO2) taken in a room, with the yes/no class referring to whether the room was occupied at the time or not. 

### Results and Discussion

### Results
The accuracy results should be presented in the following table where My1NN, My7NN and MyNB are your implementations of the 1NN, 7NN and NB algorithms, and MyEns is your ensemble algorithm combining 1NN, 7NN and NB, evaluated using your stratified 10-fold cross validation.

| Dataset   | ZeroR | 1R  | 1NN | 7NN | NB  | DT  | MLP | SVM | RF  | **My1NN** | **My7NN** | **MyNB** | **MyEns** |
|-----------|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----------|-----------|----------|-----------|
| Diabetes  |  65.189%     |  70.7953%   |     |     |     |     |     |     |     |  69.54%      |   75.53%        |    75.26%      |    76.31%       |
| Occupancy |       |     |     |     |     |     |     |     |     |    99.51%       |     0.9926      |     96.79%     |     99.16%      |

 

Confusion Matrix
Recall, Precision, F1 – can probably compare these too for fun or if the results are close. Or at least specify if they’re necessary or not.

### Discussion
•	Compare the performance of all classifiers in terms of accuracy (and other performance measures if you have other measures)
•	
•	Compare your kNN and NB classifiers with Weka's 
•	Compare your ensemble MyEns with the individual classifiers it combines (My1NN, My7NN, MyNB)
•	Discuss the changes in performance on the two datasets - did the classifiers perform differently and if so, did these differences make intuitive sense to you?
Include anything else that you consider important.

### Conclusion
Summarise your main findings and suggest future work.
Reflection

Write one or two paragraphs describing the most important thing that you have learned throughout this assignment. Each group member should write their own reflection.

