"""
-- ------------------------------------------------------------------
-- Title: Select a random somple of paient.
-- Description: 
--     data.sample(db=eicu, sample_size=1000, 
--                 seed=22, output="patients.csv")
-- return: resulting list of patientID 
-- ------------------------------------------------------------------
"""
import pandas as pd
import random
import csv

raw_path = "../../data/raw/"
interim_path = "../../data/interim/"

def sample(db="eicu", sample_size=1000, 
           seed=22, output=None, path="", label=""):
    # set path and table name
    if path is not None:
        raw_path = path
        interim_path = path

    if db == "eicu":
        dbPath = raw_path + db + "/patient.csv"
        idLabel = "patientunitstayid"
    elif db == "mimic":
        dbPath = raw_path + db + "/PATIENTS.csv"
        idLabel = "ROW_ID"
    else:
        dbPath = interim_path + db + "/patientids.csv"
        idLabel = "patientid"

    if label is not None:
        idLabel = label

    # Read patient list
    dfPatients = pd.read_csv(dbPath)
    dfPatientIds = dfPatients[idLabel]
    
    # Generate random list
    random.seed(seed)
    
    # list of sampleIds
    sampleIds = random.sample(list(dfPatientIds),sample_size)
    
    if output is not None:
        if output.lower().endswith('.csv'):
            with open(output, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows([sampleIds,])
        else:
            with open(output, "w") as output:
                output.write(str(sampleIds))

    # return the list of patient Ids
    return sampleIds
