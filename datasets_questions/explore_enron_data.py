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
import json

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

enron_array_data = json.loads(json.dumps(enron_data))

ret = ''
count = 0;
for j in enron_array_data:
    # ret = ret+" "+enron_array_data[j]
    if(enron_array_data[j]['email_address']!="NaN"):
        count = count + 1

    print (enron_array_data[j]['email_address'], enron_array_data[j]['email_address']=="NaN")
    print "\n\r"

print count
# print json.dumps(enron_data, sort_keys=True, indent=4, separators=(',', ': '))


