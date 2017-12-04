#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Module for collecting statistics on the training data in order to perform pre-processing
Created on Mon Dec  4 16:30:20 2017

@author: leo
"""

import numpy as np

def get_activation_ratio(orch):
    num_activation = np.sum(orch>0, axis=0)
    ratio_activation = num_activation / float(orch.shape[0])
    return ratio_activation