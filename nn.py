import math 

def classify_nn(training_filename, testing_filename, k):
    training_data = get_entries(training_filename)
    testing_data = get_entries(testing_filename)

    decisions = []
    for test in testing_data:

        distances = []
        for train in training_data:
            label = train[-1]
            e_dist = euclidean_distance(test, train)    # compute the euclidean distance between the training data and testing data
            distances.append((e_dist, label))  # add a tuple (distance, class) 
        
        distances.sort(key = lambda t : t[0])   # sort the distances in increasing order
        k_neighbours = distances[:k]

        yes_count = sum(1 for _, label in k_neighbours if label == 'yes')   # count yes votes
        no_count = len(k_neighbours) - yes_count    # no_count is the rest

        decision = 'yes' if yes_count >= no_count else 'no' # tie or yes-majority => 'yes'
        decisions.append(decision)
    return decisions

def euclidean_distance(test, train):
    sq_sum = 0.0
    for test_val, train_val in zip(test, train[:-1]):
        sq_sum += (test_val - train_val) ** 2
    return math.sqrt(sq_sum)

def get_entries(filename):  # reads files and stores each line as an entry in a list
    entries = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            parts = line.split(',')
            entry = []
            for item in parts:
                try:
                    entry.append(float(item))
                except ValueError:
                    entry.append(item)
            entries.append(entry)
    return entries