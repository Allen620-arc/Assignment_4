"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""

import a4q4 as C

test_suite_deal = [

    {"inputs": ['AH', '2H', '3H', '4H'],
     "outputs": [['3H', 'AH', '2H', '4H'], ['3H', 'AH', '2H', '4H'], ['3H', 'AH', '2H', '4H'], ['3H', 'AH', '2H', '4H']],
     "reason": "Check the maximum for one value in a list."},

    {"inputs": ['AH', '2H', '3H', '4H'],
     "outputs": [['AH', '4H', '3H', '2H'], ['AH', '4H', '3H', '2H'], ['AH', '4H', '3H', '2H'], ['AH', '4H', '3H', '2H']],
     "reason": "Check the maximum for one value in a list."},
]

for test_deal in test_suite_deal:

    # Call the operation.
    inputs = C.Card()
    outputs = inputs.deal(4, 4, test_deal["inputs"])

    # If the output and inputs aren't the same, then return error.
    if outputs != test_deal["outputs"]:
        print("Testing fault: deal() returned", outputs, "on inputs", inputs, "(", test_deal["reason"], ")")

test_suite_value = [

    {"inputs": 'AH',
     "outputs": 1,
     "reason": "The value of AH is 1."},

    {"inputs": 'JH',
     "outputs": 11,
     "reason": "The value of JH is 11."},

    {"inputs": 'QH',
     "outputs": 12,
     "reason": "The value of JH is 12."},

    {"inputs": 'KH',
     "outputs": 13,
     "reason": "The value of JH is 13."}
]

for test_value in test_suite_value:

    # Call the operation.
    inputs = C.Card()
    outputs = inputs.value(test_value["inputs"])

    # If the output and inputs aren't the same, then return error.
    if outputs != test_value["outputs"]:
        print("Testing fault: value() returned", outputs, "on inputs", inputs, "(", test_value["reason"], ")")

test_suite_highest = [

    {"inputs": ["5D", "10H", "QS", "8C", "JH"],
     "outputs": "QS",
     "reason": "Q is the largest value among the cards."},

    {"inputs": ['AH', '2H', '3H', '4H'],
     "outputs": "4H",
     "reason": "4 is the largest value among the cards."},
]

for test_highest in test_suite_highest:

    # Call the operation.
    inputs = C.Card()
    outputs = inputs.highest(test_highest["inputs"])

    # If the output and inputs aren't the same, then return error.
    if outputs != test_highest["outputs"]:
        print("Testing fault: highest() returned", outputs, "on inputs", inputs, "(", test_highest["reason"], ")")

test_suite_lowest = [

    {"inputs": ["5D", "10H", "QS", "8C", "JH"],
     "outputs": "5D",
     "reason": "5 is the smallest value among the cards."},

    {"inputs": ['AH', '2H', '3H', '4H'],
     "outputs": "AH",
     "reason": "A is the smallest value among the cards"},
]

for test_lowest in test_suite_lowest:

    # Call the operation.
    inputs = C.Card()
    outputs = inputs.lowest(test_lowest["inputs"])

    # If the output and inputs aren't the same, then return error.
    if outputs != test_lowest["outputs"]:
        print("Testing fault: lowest() returned", outputs, "on inputs", inputs, "(", test_lowest["reason"], ")")

test_suite_average = [

    {"inputs": ["5D", "10H", "QS", "8C", "JH"],
     "outputs": "5D",
     "reason": "The Q gets the highest value among the cards."},

    {"inputs": ['AH', '2H', '3H', '4H'],
     "outputs": "AH",
     "reason": "The 4 is the largest value among the cards"},
]

for test_average in test_suite_average:

    # Call the operation.
    inputs = C.Card()
    outputs = inputs.average(test_average["inputs"])

    # If the output and inputs aren't the same, then return error.
    if outputs != test_average["outputs"]:
        print("Testing fault: average() returned", outputs, "on inputs", inputs, "(", test_average["reason"], ")")