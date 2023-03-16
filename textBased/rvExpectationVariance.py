# program to calculate expected value and variance value
# given probabilities and outcomes

from math import sqrt

def get_inputs():
    outcome_count = int(input("Enter how many outcomes you have: "))

    outcomes, probabilities = [], []

    for i in range(outcome_count):
        outcomes.append(int(input(f"Enter value of outcome {i+1}: ")))
        probability_i = (input(f"Enter probability of outcome {i+1}: "))
        # convert probability to float
        if '/' in probability_i:
            num, denom = probability_i.split('/')
            probabilities.append(float(num)/float(denom))
        else:
            probabilities.append(float(probability_i))

    return outcomes, probabilities


def get_expected_value(outcomes, probabilities):
    expected_val = 0
    for i in range(len(outcomes)):
        expected_val += outcomes[i] * probabilities[i]

    return expected_val


def get_variance_value(outcomes, probabilities, expected_val):
    variance_val = 0
    for i in range(len(outcomes)):
        variance_val += (outcomes[i]-expected_val)**2 * probabilities[i]

    return variance_val


out, prob = get_inputs()
exp = get_expected_value(out, prob)
var = get_variance_value(out, prob, exp)
std = sqrt(var)

print(f"Expected value: {exp}\nVariance value: {var}\nStandard deviation: {std}")
