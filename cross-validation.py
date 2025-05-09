# using the folds i just created, make one testing data and the rest training data
# run our algorithms on them - naive bayes + knn for a few different values of k
# evaluate accuracy and any other measures we deem important for our report
# 

import random
from collections import defaultdict
from naivebayes import classify_nb
from nn import classify_nn
from ensemble import classify_ens


def stratified_k_folds(data, k=10):
    """Create k stratified folds from the data."""
    folds = [[] for _ in range(k)]
    class_buckets = defaultdict(list)

    # Separate examples by class
    for row in data:
        label = row.strip().split(',')[-1]
        class_buckets[label].append(row)

    # Shuffle and distribute into folds
    for label, rows in class_buckets.items():
        random.shuffle(rows)
        for i, row in enumerate(rows):
            folds[i % k].append(row)

    return folds

def evaluate_classifier(classify_fn, folds, *args):
    """Perform k-fold cross-validation using a given classifier function."""
    accuracies = []

    for i in range(len(folds)):
        test_fold = folds[i]
        train_folds = [row for j, fold in enumerate(folds) if j != i for row in fold]

        # Write to temporary files
        with open('train_temp.csv', 'w') as f:
            f.write('\n'.join(train_folds))
        with open('test_temp.csv', 'w') as f:
            test_lines = [','.join(row.strip().split(',')[:-1]) for row in test_fold]
            f.write('\n'.join(test_lines))

        # True labels
        true_labels = [row.strip().split(',')[-1] for row in test_fold]

        # Run classifier
        predictions = classify_fn('train_temp.csv', 'test_temp.csv', *args)

        # Evaluate
        correct = sum(1 for true, pred in zip(true_labels, predictions) if true == pred)
        accuracy = correct / len(true_labels)
        accuracies.append(accuracy)

    avg_accuracy = sum(accuracies) / len(accuracies)
    return avg_accuracy

# Load the full dataset (e.g., pima.csv or occupancy.csv)
with open("pima.csv", "r") as file:
    full_data = file.readlines()

# Create 10 stratified folds
folds = stratified_k_folds(full_data, k=10)

# Evaluate Naive Bayes
acc_nb = evaluate_classifier(classify_nb, folds)
print(f"Naive Bayes Accuracy: {acc_nb:.4f}")

# Evaluate kNN (k=3)
acc_knn3 = evaluate_classifier(classify_nn, folds, 3)
print(f"KNN (k=3) Accuracy: {acc_knn3:.4f}")

# Evaluate Ensemble (k1=3, k2=5)
acc_ensemble = evaluate_classifier(classify_ens, folds, 3, 5)
print(f"Ensemble Accuracy: {acc_ensemble:.4f}")
