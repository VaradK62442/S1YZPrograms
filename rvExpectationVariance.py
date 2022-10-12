# program to calculate expected value and variance value
# given probabilities and outcomes

from math import sqrt

def getInputs():
    outcomeCount = int(input("Enter how many outcomes you have: "))

    outcomes, probabilities = [], []

    for i in range(outcomeCount):
        outcomes.append(int(input(f"Enter value of outcome {i+1}: ")))
        probability_i = (input(f"Enter probability of outcome {i+1}: "))
        # convert probability to float
        num, denom = probability_i.split('/')
        probabilities.append(float(num)/float(denom))

    return outcomes, probabilities


def getExpectedValue(outcomes, probabilities):
    expectedVal = 0
    for i in range(len(outcomes)):
        expectedVal += outcomes[i] * probabilities[i]

    return expectedVal


def getVarianceValue(outcomes, probabilities, expectedVal):
    varianceVal = 0
    for i in range(len(outcomes)):
        varianceVal += (outcomes[i]-expectedVal)**2 * probabilities[i]

    return varianceVal


out, prob = getInputs()
exp = getExpectedValue(out, prob)
var = getVarianceValue(out, prob, exp)
std = sqrt(var)

print(f"Expected value: {exp}\nVariance value: {var}\nStandard deviation: {std}")
