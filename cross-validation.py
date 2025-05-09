# using the folds i just created, make one testing data and the rest training data
# run our algorithms on them - naive bayes + knn for a few different values of k
# evaluate accuracy and any other measures we deem important for our report
# 

import random
from collections import defaultdict
from naivebayes import classify_nb
from nn import classify_nn
from ensemble import classify_ens


def parse_folds_from_file(filename):
    """Parses a fold file in the format described and returns a list of folds."""
    folds = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip() != '']
    
    current_fold = []
    for line in lines:
        if line.startswith("fold"):
            if current_fold:
                folds.append(current_fold)
                current_fold = []
        else:
            current_fold.append(line)
    if current_fold:
        folds.append(current_fold)

    return folds

def cross_validate_from_folds_file(folds_file, classify_fn, *args):
    """Evaluates a classifier using cross-validation based on a fold file."""
    folds = parse_folds_from_file(folds_file)
    accuracies = []

    for i in range(len(folds)):
        test_set = folds[i]
        train_set = [row for j, fold in enumerate(folds) if j != i for row in fold]

        # Prepare training and testing files
        with open("train_temp.csv", "w") as f:
            f.write('\n'.join(train_set))
        with open("test_temp.csv", "w") as f:
            f.write('\n'.join([','.join(row.split(',')[:-1]) for row in test_set]))

        true_labels = [row.split(',')[-1] for row in test_set]
        predictions = classify_fn("train_temp.csv", "test_temp.csv", *args)

        correct = sum(1 for true, pred in zip(true_labels, predictions) if true == pred)
        accuracy = correct / len(test_set)
        accuracies.append(accuracy)

    avg_accuracy = sum(accuracies) / len(accuracies)
    return avg_accuracy

# Evaluate on Pima dataset
acc_nb = cross_validate_from_folds_file("pima-folds.csv", classify_nb)
print(f"Naive Bayes Accuracy (Pima): {acc_nb:.4f}")

acc_knn1 = cross_validate_from_folds_file("pima-folds.csv", classify_nn, 1)
print(f"KNN (k=1) Accuracy (Pima): {acc_knn1:.4f}")

acc_knn7 = cross_validate_from_folds_file("pima-folds.csv", classify_nn, 7)
print(f"KNN (k=7) Accuracy (Pima): {acc_knn7:.4f}")

acc_ensemble = cross_validate_from_folds_file("pima-folds.csv", classify_ens, 1, 7)
print(f"Ensemble Accuracy (Pima): {acc_ensemble:.4f}")

# Evaluate on Occupancy dataset
acc_nb_occ = cross_validate_from_folds_file("occupancy-folds.csv", classify_nb)
print(f"Naive Bayes Accuracy (Occupancy): {acc_nb_occ:.4f}")

acc_knn1_occ = cross_validate_from_folds_file("occupancy-folds.csv", classify_nn, 1)
print(f"KNN (k=1) Accuracy (Occupany): {acc_knn1:.4f}")

acc_knn7_occ = cross_validate_from_folds_file("occupancy-folds.csv", classify_nn, 7)
print(f"KNN (k=7) Accuracy (Occupany): {acc_knn7:.4f}")

acc_ensemble_occ = cross_validate_from_folds_file("occupancy-folds.csv", classify_ens, 1, 7)
print(f"Ensemble Accuracy (Occupancy): {acc_ensemble:.4f}")