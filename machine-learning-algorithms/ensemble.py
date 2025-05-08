from naivebayes import classify_nb
from nn import classify_nn

def classify_ens(training_file, testing_file, k1, k2):
    # Get predictions from each model
    pred_k1 = classify_nn(training_file, testing_file, k1)
    pred_k2 = classify_nn(training_file, testing_file, k2)
    pred_nb = classify_nb(training_file, testing_file)

    # Combine predictions with majority voting
    final_predictions = []
    for i in range(len(pred_k1)):
        votes = [pred_k1[i], pred_k2[i], pred_nb[i]]
        if votes.count("yes") > votes.count("no"):
            final_predictions.append("yes")
        elif votes.count("no") > votes.count("yes"):
            final_predictions.append("no")
        else:
            final_predictions.append("yes")  # Tie-breaker

    return final_predictions