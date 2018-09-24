# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 20:50:19 2018

@author: Pranjal Agnihotri
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('mlbootcamp5_train.csv', sep=';')

x= df.iloc[: , :].values