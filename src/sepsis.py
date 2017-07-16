"""
-- ------------------------------------------------------------------
-- Title: Explore data on sepsis patients
-- Description: 
--     Start off on comparing mortality rates
--      Followed by comparing teaching hospitals
-- ------------------------------------------------------------------
"""

import data.sampling as sampling
import pandas as pd
import csv

#get sample population
sample_eicu = sampling.sample(path="../data/raw/")
sample_sepsis = sampling.sample(db="sepsis", path="../data/interim/")

df_eicu = pd.Series.to_frame(sample_eicu)
df_sepsis = pd.Series.to_frame(sample_sepsis)

