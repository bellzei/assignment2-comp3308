from naivebayes import classify_nb
from nn import classify_nn

def classify_ens(training_filename, testing_filename, k1, k2):

    bayes = classify_nb(training_filename, testing_filename)
    nn1 = classify_nn(training_filename, testing_filename, k1)
    nn2 = classify_nn(training_filename, testing_filename, k2)

    ens_decisions = []
    for x in range(len(bayes)):
        yes_count = 0
        if bayes[x] == 'yes':
            yes_count += 1
        if nn1[x] == 'yes':
            yes_count += 1
        if nn2[x] == 'yes':
            yes_count += 1
        
        if yes_count >= 2:
            decision = 'yes'
        else: 
            decision = 'no'
        
        ens_decisions.append(decision)
    return [ens_decisions]
