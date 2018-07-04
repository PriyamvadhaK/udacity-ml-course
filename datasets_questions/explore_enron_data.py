#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# number of examples in dataset
print(len(enron_data.keys()))

# number of features per example
for key, value in enron_data.items():
    print(len([item for item in value if item]))
    break
# count poi
count = 0 
for value in enron_data.items():
    for val in value[1].keys():
        if (val == "poi") and value[1]["poi"]==1:
            count = count + 1
print(count)

#

print(enron_data["PRENTICE JAMES"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])
print(enron_data.keys())
#print max(enron_data["SKILLING JEFFREY K"]["total_payments"], enron_data["LAY KENNETH"]["total_payments"], enron_data["FASTOW ANDREW"]["total_payments"])
count_s = 0
count_e = 0
for value in enron_data.items():
    if value[1]["salary"] != "NaN":
        count_s = count_s + 1
    if value[1]['email_address'] != "NaN":
        count_e = count_e + 1
print(count_s, count_e)

count_p = 0
for value in enron_data.items():
    if value[1]["total_payments"] == "NaN":
        count_p = count_p + 1
print(float(count_p))/len(enron_data.keys())
