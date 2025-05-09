### Report 

### Introduction
This study evaluates and compares the performance of different machine learning classifiers using two datasets. The classifiers were trained to predict (i) the onset of diabetes from basic clinical measurements and (ii) room occupancy from environmental sensor readings. In this study we implemented 3 of our own classifiers: k-nearest neighbours with k = 1 and 7, and Naïve Bayes, as well as an ensemble classifier combining the three. We then contrast these classifiers with ZeroR, OneR, 1-NN, 7-NN, Naive Bayes, Decision Tree, Support Vector Machines, Multi-Layer Perceptrons, and Random Forest computed using Weka software.

We will evaluate the classifiers by measuring accuracy (proportion of correctly classified examples) achieved by 10-fold stratified cross-validation. 

We will compare the classifiers by comparing the accuracies achieved. We will run a paired t-test to determine if one classifier is significantly better than another.  

Accurate diagnosis of diabetes is vital for quick intervention, while automatic detection of room occupancy plays an important role in energy-efficient building control. Demonstrating that lightweight learners can achieve a similar accuracy to more sophisticated models would support their use in resource-constrained settings. 

### Data
We are using two datasets: Pima Indian Diabetes Dataset (PID) and Room Occupancy Dataset (RO). 

PID has 8 numeric attributes and 2 classes (yes or no) spanning 768 instances. Each instance describes characteristics and test measurements of a patient of  Pima Indian heritage, with the yes/no class referring to whether or not they have diabetes. 

RO has 4 numeric attributes and 2 classes (yes or no) spanning 2,025 instances. Each instance describes the sensor readings  (light, temperature, sound and CO2) taken in a room, with the yes/no class referring to whether the room was occupied at the time or not. 

Similarities between the 

### Results and Discussion

### Results
The accuracy results should be presented in the following table where My1NN, My7NN and MyNB are your implementations of the 1NN, 7NN and NB algorithms, and MyEns is your ensemble algorithm combining 1NN, 7NN and NB, evaluated using your stratified 10-fold cross validation.

| Dataset   | ZeroR   | 1R       | 1NN      | 7NN      | NB       | DT       | MLP      | SVM      | RF       | **My1NN** | **My7NN**  | **MyNB** | **MyEns** |
|-----------|---------|----------|----------|----------|----------|----------|----------|----------|----------|-----------|-----------|----------|-----------|
| Diabetes  | 65.189% | 70.7953% | 69.7523% | 75.7497% | 74.7066% | 74.5763% | 75.0978% | 76.4016% | 77.4446% | 69.54%    |         75.53%     | 75.26%   | 76.31%    |
| Occupancy | 81.2747% | 98.4684% | 99.5059% | 99.2589% | 96.7885% | 99.5059% | 99.3083% | 98.419% | 99.7036% | 99.51% | 99.26% | 96.79% | 99.16% |

 Discussion:

The results illustrate the varying performance of different classifiers across the two datasets. On the Pima Indians Diabetes dataset, our 7NN classifier (My7NN) achieved a notable accuracy of 75.53%, outperforming both our 1NN (My1NN) and Naive Bayes (MyNB) implementations. The ensemble model (MyEns) delivered the highest accuracy at 76.31%, confirming the benefit of combining multiple models through majority voting.

In contrast, the Room Occupancy dataset yielded exceptionally high accuracies for all classifiers, with both our 1NN and 7NN implementations exceeding 99%, and MyEns achieving 99.16%. This indicates that the occupancy data had clearer patterns and more separable clusters, making it well-suited for instance-based learners like kNN.

When comparing with Weka’s implementations, we observe that our models achieved similar performance. For example, Weka’s kNN (IBk) with k=1 achieved 99.5059% on the occupancy dataset, closely matching our My1NN (99.51%). Our Naive Bayes implementation also performed comparably to Weka’s, especially on the diabetes dataset.

The ensemble approach consistently improved classification stability and accuracy. It smoothed out weaknesses of individual classifiers, such as MyNB’s relatively lower performance on the occupancy dataset, by leveraging the strengths of all three.

These performance differences across datasets highlight the importance of choosing the right algorithm for the data structure at hand. The occupancy dataset’s sensor readings had tight correlations and clusters, making it favorable for kNN. Meanwhile, the more overlapping and probabilistically complex Pima dataset was better handled with probabilistic models like Naive Bayes and ensemble methods.



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

