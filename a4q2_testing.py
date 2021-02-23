"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""

import Statistics as S


def close_enough(a, b, tolerance):
    """
    Purpose:
        Check if 2 floating point values are close enough to be considered equal.

    Pre-Conditions:
        :param a: a floating point value
        :param b: a floating point value
        :param tolerance: a small positive floating point value

    Post-Conditions:
        none

    Return:
        :return True if the difference between a and b is small
    """
    return abs(a - b) < tolerance


test_suite_add_count = [

    {"inputs": [0],
     "outputs": 1,
     "reason": "Check count after one value is counted."},

    {"inputs": [0, 1],
     "outputs": 2,
     "reason": "Check count after two values are counted."},

    {"inputs": [0, 1, 2],
     "outputs": 3,
     "reason": "Check count after three values are counted."},
]

for test_add_count in test_suite_add_count:

    # Call the operation.
    inputs = S.Statistics()
    for v in test_add_count["inputs"]:
        inputs.add(v)
    outputs = inputs.count()

    # If the output and inputs aren't the same, then return error.
    if outputs != test_add_count["outputs"]:
        print("Testing fault: add() + count() returned", outputs, "on inputs", inputs, "(", test_add_count["reason"],
              ")")

test_suite_add_mean = [

    {"inputs": [0, 0, 0],
     "outputs": 0,
     "reason": "Check average from three values in a list."},

    {"inputs": [1, 2, 3, 4, 5],
     "outputs": 3,
     "reason": "Check average from five values in a list."},

    {"inputs": [1.00001, 1.000001, 1.0000001],
     "outputs": 1.0000037,
     "reason": "Check count after three decimal value are added regarding error bounds"},

    {"inputs": [21, 62, 17],
     "outputs": 33.333333333333333,
     "reason": "Check count after three decimal value are added regarding error bounds"},
]

for test_add_mean in test_suite_add_mean:

    # Call the operation.
    inputs = S.Statistics()
    for v in test_add_mean["inputs"]:
        inputs.add(v)
    outputs = inputs.mean()

    # If the output and inputs aren't the same, then return error.
    if outputs != test_add_mean["outputs"]:
        print("Testing fault: add() + mean() returned", outputs, "on inputs", inputs, "(", test_add_mean["reason"], ")")

    # We shouldn't test the floating point values for equality, because or round-off error so use the close_enough()
    # function.
    if not close_enough(test_add_mean["outputs"], outputs, 0.000001):
        print("Testing fault: add() + mean() returned", outputs, "on inputs", inputs, "(", test_add_mean["reason"], ")")

print('*** Test script completed ***')
