#!/usr/bin/python
import heapq

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    errors = abs(predictions - net_worths)

    ### your code goes here
    print errors, heapq.nlargest(9, abs(predictions - net_worths))
    
    return cleaned_data

