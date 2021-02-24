"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""

import a4q3 as S


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


test_suite_add_max = [

    {"inputs": [0],
     "outputs": 0,
     "reason": "Check the maximum for one value in a list."},

    {"inputs": [0, 1],
     "outputs": 1,
     "reason": "Check the maximum for two values in a list."},

    {"inputs": [0, 1, 2],
     "outputs": 2,
     "reason": "Check the maximum for three values in a list."},

    {"inputs": [0, 0, 0],
     "outputs": 0,
     "reason": "Check the maximum for three values in a list."},

    {"inputs": [1, 2, 3, 4, 5],
     "outputs": 5,
     "reason": "Check the maximum for five values in a list."},

    {"inputs": [1.1, 1.01, 1.001],
     "outputs": 1.1,
     "reason": "Check the maximum for three values in a list."},

    {"inputs": [21, 62, 17],
     "outputs": 62,
     "reason": "Check the maximum for three values in a list."},

    {"inputs": [-1, 2, 2],
     "outputs": 2,
     "reason": "Check the maximum for three values in a list."},
]

for test_add_max in test_suite_add_max:

    # Call the operation.
    inputs = S.Statistics()
    for v in test_add_max["inputs"]:
        inputs.add(v)
    outputs = inputs.max()

    # If the output and inputs aren't the same, then return error.
    if outputs != test_add_max["outputs"]:
        print("Testing fault: add() + max() returned", outputs, "on inputs", inputs, "(", test_add_max["reason"], ")")

test_suite_add_min = [

    {"inputs": [0],
     "outputs": 0,
     "reason": "Check the minimum for one values in a list."},

    {"inputs": [0, 1],
     "outputs": 0,
     "reason": "Check the minimum for two values in a list."},

    {"inputs": [0, 1, 2],
     "outputs": 0,
     "reason": "Check the minimum for three values in a list."},

    {"inputs": [0, 0, 0],
     "outputs": 0,
     "reason": "Check the minimum for three values in a list."},

    {"inputs": [1, 2, 3, 4, 5],
     "outputs": 1,
     "reason": "Check the minimum for five values in a list."},

    {"inputs": [1.1, 1.01, 1.001],
     "outputs": 1.001,
     "reason": "Check the minimum for three values in a list."},

    {"inputs": [21, 62, 17],
     "outputs": 17,
     "reason": "Check the minimum for three values in a list."},

    {"inputs": [-1, 2, 2],
     "outputs": -1,
     "reason": "Check the minimum for three values in a list."},
]

for test_add_min in test_suite_add_min:

    # Call the operation.
    inputs = S.Statistics()
    for v in test_add_min["inputs"]:
        inputs.add(v)
    outputs = inputs.min()

    # If the output and inputs aren't the same, then return error.
    if outputs != test_add_min["outputs"]:
        print("Testing fault: add() + min() returned", outputs, "on inputs", inputs, "(", test_add_min["reason"], ")")

test_suite_add_range = [

    {"inputs": [0],
     "outputs": 0,
     "reason": "Check count after one value is counted."},

    {"inputs": [0, 1],
     "outputs": 1,
     "reason": "Check count after two values are counted."},

    {"inputs": [0, 1, 2],
     "outputs": 2,
     "reason": "Check count after three values are counted."},

    {"inputs": [0, 0, 0],
     "outputs": 0,
     "reason": "Check average from three values in a list."},

    {"inputs": [1, 2, 3, 4, 5],
     "outputs": 4,
     "reason": "Check average from five values in a list."},

    {"inputs": [1.1, 1.01, 1.001],
     "outputs": 0.0990000000000002,
     "reason": "Check average from three values in a list."},

    {"inputs": [21, 62, 17],
     "outputs": 45,
     "reason": "Check average from three values in a list."},

    {"inputs": [-1, 2, 2],
     "outputs": 3,
     "reason": "Check average from three values in a list."},
]

for test_add_range in test_suite_add_range:

    # Call the operation.
    inputs = S.Statistics()
    for v in test_add_range["inputs"]:
        inputs.add(v)
    outputs = inputs.range()

    # If the output and inputs aren't the same, then return error.
    if outputs != test_add_range["outputs"]:
        print("Testing fault: add() + range() returned", outputs, "on inputs", inputs, "(", test_add_range["reason"],
              ")")

test_suite_add_dict = [

    {"inputs": [0],
     "outputs": {0: 1},
     "reason": "Check count after one value is counted."},

    {"inputs": [0, 1],
     "outputs": {0: 1, 1: 1},
     "reason": "Check count after two values are counted."},

    {"inputs": [0, 1, 2],
     "outputs": {0: 1, 1: 1, 2: 1},
     "reason": "Check count after three values are counted."},

    {"inputs": [0, 0, 0],
     "outputs": {0: 3},
     "reason": "Check average from three values in a list."},

    {"inputs": [1, 2, 3, 4, 5],
     "outputs": {1: 1, 2: 1, 3: 1, 4: 1, 5: 1},
     "reason": "Check average from five values in a list."},

    {"inputs": [1.1, 1.01, 1.001],
     "outputs": {1.1: 1, 1.01: 1, 1.001: 1},
     "reason": "Check average from three values in a list."},

    {"inputs": [21, 62, 17],
     "outputs": {21: 1, 62: 1, 17: 1},
     "reason": "Check average from three values in a list."},

    {"inputs": [-1, 2, 2],
     "outputs": {-1: 1, 2: 2},
     "reason": "Check average from three values in a list."},
]

for test_add_dict in test_suite_add_dict:

    # Call the operation.
    inputs = S.Statistics()
    for v in test_add_dict["inputs"]:
        inputs.add(v)
    outputs = inputs.dict()

    # If the output and inputs aren't the same, then return error.
    if outputs != test_add_dict["outputs"]:
        print("Testing fault: add() + dict() returned", outputs, "on inputs", inputs, "(", test_add_dict["reason"], ")")

test_suite_add_mode = [

    {"inputs": [0],
     "outputs": 0,
     "reason": "Check count after one value is counted."},

    {"inputs": [0, 1],
     "outputs": 0,
     "reason": "Check count after two values are counted."},

    {"inputs": [0, 1, 2],
     "outputs": 0,
     "reason": "Check count after three values are counted."},

    {"inputs": [0, 0, 0],
     "outputs": 0,
     "reason": "Check average from three values in a list."},

    {"inputs": [1, 2, 3, 4, 5],
     "outputs": 1,
     "reason": "Check average from five values in a list."},

    {"inputs": [1.1, 1.01, 1.001],
     "outputs": 1.1,
     "reason": "Check average from three values in a list."},

    {"inputs": [21, 62, 17],
     "outputs": 21,
     "reason": "Check average from three values in a list."},

    {"inputs": [-1, 2, 2],
     "outputs": 2,
     "reason": "Check average from three values in a list."},
]

for test_add_mode in test_suite_add_mode:

    # Call the operation.
    inputs = S.Statistics()
    for v in test_add_mode["inputs"]:
        inputs.add(v)
    outputs = inputs.mode()

    # If the output and inputs aren't the same, then return error.
    if outputs != test_add_mode["outputs"]:
        print("Testing fault: add() + mode() returned", outputs, "on inputs", inputs, "(", test_add_mode["reason"], ")")

print('*** Test script completed ***')
