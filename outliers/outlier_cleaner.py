#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    #predictions = [item for sublist in predictions for item in sublist]
    #net_worths = [item for sublist in net_worths for item in sublist]
    #err = [(x1 - x2)*(x1-x2) for (x1, x2) in zip(net_worths, predictions)]
    #err.sort(key=int)
    n_clean = 0.1 * len(predictions)
    for i in range(len(predictions)):
        err = abs(predictions[i] - net_worths[i])
        curr = (ages[i], net_worths[i], err)
        cleaned_data.append(curr)
    cleaned_data.sort(key=lambda tup: tup[2])
    cleaned_data = cleaned_data[0:int(0.9 * len(predictions))]
    return cleaned_data

