# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#   Defines the Statistics ADT
#   Calculate mean and variance and other statistical summaries  
#   of numeric data.

# Implementation
# Do the calculations without storing all the data!
# Use a Python dictionary as a record to store three quantities:
#   _count':     the number of data values added
#   _avg':       the running average of the values added

# These values can be modified every time a new data value is 
# added, so that the mean and variance can be calculated quickly  
# as needed.  This approach means that we do not need to store  
# the data values themselves, which could save a lot of space.
#
# NOTE: This file does not contain the full ADT as shown in class.  
#       The calculations for var() and sampvar() were removed to 
#       keep the exercise concise.

class Statistics(object):
    def __init__(self):
        """
        Purpose:
            Initialize a Statistics object instance.
        """
        self.__count = 0  # How many data values seen so far.
        self.__avg = 0  # The running average so far.
        self.__range = 0  # The running range so far.
        self.__max = None  # The largest value so far.
        self.__min = None  # The smallest value so far.
        self.__mode = None  # The running mode so far.
        self.__dict = {}  # An empty dictionary of the recorded values.

    def add(self, value):
        """
        Purpose:
            Use the given value in the calculation of mean and variance.
        Pre-Conditions:
            :param value: The value to be added.
        Post-Conditions:
            (none)
        Return:
            (none)
        """
        self.__count += 1
        self.__avg += (value - self.__avg) / self.__count

        # Finds the max and min of a list.
        if self.__max is None or self.__min is None:
            self.__min = value
            self.__max = value
        if value > self.__max:
            self.__max = value
        if value < self.__min:
            self.__min = value

        # Finds the range of a list.
        self.__range = self.__max - self.__min

        # Dictionary for the purposes of finding mode.
        if value in self.__dict:
            self.__dict[value] += 1
        else:
            self.__dict[value] = 1

    def mean(self):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__avg

    def count(self):
        """
        Purpose:
            Return the values seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__count

    def max(self):
        """
        Purpose:
            Return the largest value seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__max

    def min(self):
        """
        Purpose:
            Return the smallest value seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__min

    def range(self):
        """
        Purpose:
            Return the range of values seen so far.
        Post-conditions:
            (none)
        Return:
            The range of the values seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__range

    def dict(self):
        """
        Purpose:
            Return the most common value seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__dict

    def mode(self):
        """
        Purpose:
            Return the most common value seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: If no data has been seen, 0 is returned. This is clearly false.
        """
        return self.__mode