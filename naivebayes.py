import math

# Helper functions
def load_data(filename, has_class=True):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            
            # splitting and formatting the csv file for taining and testing datasets
            if has_class:
                attribute_strings = parts[:-1]
                attribute_floats = []
                for item in attribute_strings:
                    number = float(item)
                    attribute_floats.append(number)
                attributes = attribute_floats
                label = parts[-1]
                data.append((attributes, label))
            else:
                attribute_floats = []
                for item in parts:
                    number = float(item)
                    attribute_floats.append(number) 
                attributes = attribute_floats
                data.append(attributes)
    return data

def mean(values):
    return sum(values) / len(values)

def stddev(values, mean_value):
    variance = sum((x - mean_value) ** 2 for x in values) / len(values)
    return math.sqrt(variance) if variance > 0 else 1e-6  # Avoid zero division

def gaussian_prob(x, mean, std):
    exponent = math.exp(-((x - mean) ** 2) / (2 * std ** 2))
    return (1 / (math.sqrt(2 * math.pi) * std)) * exponent

def classify_nb(training_file, testing_file):


    # Load training and testing data
    training_data = load_data(training_file, has_class=True)
    testing_data = load_data(testing_file, has_class=False)

    # Separate by class
    separated = {'yes': [], 'no': []}
    for attributes, label in training_data:
        separated[label].append(attributes)

    # Compute priors
    total_examples = len(training_data)
    priors = {
        'yes': len(separated['yes']) / total_examples,
        'no': len(separated['no']) / total_examples
    }

    # Compute mean and stddev for each attribute for each class
    summaries = {}
    for class_value in ['yes', 'no']:
        # Initialize an empty list to hold (mean, stddev) tuples for this class
        summaries[class_value] = []

        # Get all the rows of data that belong to this class
        class_rows = separated[class_value]

        # Transpose the list of rows so we group all values for each attribute
        class_data = list(zip(*class_rows))
        for attribute_values in class_data:
            mu = mean(attribute_values)
            sigma = stddev(attribute_values, mu)
            summaries[class_value].append((mu, sigma))

    # Predict each test instance
    predictions = []
    for instance in testing_data:
        posteriors = {}
        for class_value in ['yes', 'no']:
            posterior = math.log(priors[class_value])  # use log to prevent underflow
            for i in range(len(instance)):
                mu, sigma = summaries[class_value][i]
                prob = gaussian_prob(instance[i], mu, sigma)
                posterior += math.log(prob if prob > 0 else 1e-9)
            posteriors[class_value] = posterior

        # Pick the class with higher posterior
        if posteriors['yes'] > posteriors['no']:
            predictions.append("yes")
        elif posteriors['no'] > posteriors['yes']:
            predictions.append("no")
        else:
            predictions.append("yes")  # tie breaker
    return predictions
