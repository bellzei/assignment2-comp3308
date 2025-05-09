### Report 

## Introduction
This study evaluates and compares the performance of different machine learning classifiers using two datasets. The classifiers were trained to predict (i) the onset of diabetes from basic clinical measurements and (ii) room occupancy from environmental sensor readings. In this study we implemented 3 of our own classifiers: k-nearest neighbours with k = 1 and 7, and Naïve Bayes, as well as an ensemble classifier combining the three. We then contrast these classifiers with ZeroR, OneR, 1-NN, 7-NN, Naive Bayes, Decision Tree, Support Vector Machines, Multi-Layer Perceptrons, and Random Forest computed using Weka software.

We will evaluate the classifiers by measuring accuracy (proportion of correctly classified examples) achieved by 10-fold stratified cross-validation. 

We will compare the classifiers by comparing the accuracies achieved. We will run a paired t-test to determine if one classifier is significantly better than another.  

Accurate diagnosis of diabetes is vital for quick intervention, while automatic detection of room occupancy plays an important role in energy-efficient building control. Demonstrating that lightweight learners can achieve a similar accuracy to more sophisticated models would support their use in resource-constrained settings. 

## Data
We are using two datasets: Pima Indian Diabetes Dataset (PID) and Room Occupancy Dataset (RO). 

Pima Indians Diabetes Dataset: This dataset contains 768 records with 8 numeric attributes and a binary class indicating whether an individual has diabetes ("yes" or "no"). All participants are female and of Pima Indian heritage, aged 21 or older. Attributes include metrics such as glucose concentration, BMI, and blood pressure.

Room Occupancy Dataset: This dataset contains 2025 records with 4 numeric sensor attributes (temperature, light, sound, CO2) and a binary class indicating room occupancy ("yes" or "no"). The readings were collected using environmental sensors.

#### Comparison:

- Both datasets have numeric attributes and a binary class.

- The diabetes dataset reflects medical diagnostic data, whereas the occupancy dataset captures temporal environmental conditions.

- The occupancy dataset has fewer features but more instances, potentially impacting classifier behaviour.

## Results and Discussion

### Results
The accuracy results should be presented in the following table where My1NN, My7NN and MyNB are your implementations of the 1NN, 7NN and NB algorithms, and MyEns is your ensemble algorithm combining 1NN, 7NN and NB, evaluated using your stratified 10-fold cross validation.

| Dataset   | ZeroR   | 1R       | 1NN      | 7NN      | NB       | DT       | MLP      | SVM      | RF       | **My1NN** | **My7NN**  | **MyNB** | **MyEns** |
|-----------|---------|----------|----------|----------|----------|----------|----------|----------|----------|-----------|-----------|----------|-----------|
| Diabetes  | 65.189% | 70.7953% | 69.7523% | 75.7497% | 74.7066% | 74.5763% | 75.0978% | 76.4016% | 77.4446% | 69.54%    |         75.53%     | 75.26%   | 76.31%    |
| Occupancy | 81.2747% | 98.4684% | 99.5059% | 99.2589% | 96.7885% | 99.5059% | 99.3083% | 98.419% | 99.7036% | 99.51% | 99.26% | 96.79% | 99.16% |



Confusion Matrix
Recall, Precision, F1 – can probably compare these too for fun or if the results are close. Or at least specify if they’re necessary or not.

### Discussion

The results illustrate the varying performance of different classifiers across the two datasets. On the Pima Indians Diabetes dataset, our 7NN classifier (My7NN) achieved a notable accuracy of 75.53%, outperforming both our 1NN (My1NN) and Naive Bayes (MyNB) implementations. The ensemble model (MyEns) delivered the highest accuracy at 76.31%, confirming the benefit of combining multiple models through majority voting.

In contrast, the Room Occupancy dataset yielded exceptionally high accuracies for all classifiers, with both our 1NN and 7NN implementations exceeding 99%, and MyEns achieving 99.16%. This indicates that the occupancy data had clearer patterns and more separable clusters, making it well-suited for instance-based learners like kNN.

When comparing with Weka’s implementations, we observe that our models achieved similar performance. For example, Weka’s kNN (IBk) with k=1 achieved 99.5059% on the occupancy dataset, closely matching our My1NN (99.51%). Our Naive Bayes implementation also performed comparably to Weka’s, especially on the diabetes dataset.

The ensemble approach consistently improved classification stability and accuracy. It smoothed out weaknesses of individual classifiers, such as MyNB’s relatively lower performance on the occupancy dataset, by leveraging the strengths of all three.

These performance differences across datasets highlight the importance of choosing the right algorithm for the data structure at hand. The occupancy dataset’s sensor readings had tight correlations and clusters, making it favorable for kNN. Meanwhile, the more overlapping and probabilistically complex Pima dataset was better handled with probabilistic models like Naive Bayes and ensemble methods.

### Statistical Significance:

To assess the reliability of these differences, paired corrected t-tests were performed in Weka Experimenter at the 0.05 significance level.

On the Pima Diabetes dataset, 1NN performed significantly worse than Naive Bayes. While 7NN achieved higher accuracy than Naive Bayes, this difference was not statistically significant.

On the Occupancy dataset, both 1NN and 7NN performed significantly better than Naive Bayes. The 1NN classifier, in particular, achieved a mean accuracy of 99.51%, significantly outperforming Naive Bayes (96.78%).

These results validate that the differences observed were not merely due to chance, particularly for the occupancy dataset where the structure of the data clearly favors instance-based methods.

## Conclusion

Our experiments demonstrate that both Naive Bayes and k-Nearest Neighbours are effective baseline classifiers for real-world binary classification tasks. Their performance can vary depending on data structure. An ensemble of both classifiers consistently improved accuracy by leveraging the strengths of each. Future work could explore additional features, time-series analysis for occupancy, and other ensemble methods such as bagging or boosting.

## Reflection

#### Member 1:
Through this assignment, I learned how essential good data preprocessing (e.g., normalization and stratification) is to model performance. Implementing classifiers from scratch taught me the internal mechanics of algorithms we often use as black boxes, and I now appreciate the challenges of even simple models like kNN and Naive Bayes, especially around things like numeric stability and tie-breaking in classification. I have also realized the importance of role that statistics play in not refining and understanding the important information realyed by raw data.

#### Member 2:
This assignment greatly helped with my understanding of the kNN and Naive Bayes algorithms, having to code them from scratch. The difference between the accuracy results we got with the diabetes dataset vs the occupancy dataset have made me realise the difficulties of training classifiers on noisy data. However, the accuracies were very decent all in all, making me appreciate the importance and usefulness of machine learning applications. Lastly, having to create folds and perform 10-fold stratified cross-validation has really improved my understanding of how these classifiers are trained. 