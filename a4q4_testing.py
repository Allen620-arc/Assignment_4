"""
  Name: Allen Keettikkal
  NSID: alk423
  Student Number: 11278995
  Instructor: Jeffrey Long
"""

import a4q4 as C

test_suite_add_max = [

    {"inputs": ['AH', '2H', '3H', '4H'],
     "outputs": [['3H', '3H'], ['3H', '3H']],
     "reason": "Check the maximum for one value in a list."},
]

for test_add_max in test_suite_add_max:

    # Call the operation.
    inputs = C.Card()
    outputs = inputs.deal(1, 4, test_add_max["inputs"])

    # If the output and inputs aren't the same, then return error.
    if outputs != test_add_max["outputs"]:
        print("Testing fault: add() + max() returned", outputs, "on inputs", inputs, "(", test_add_max["reason"], ")")