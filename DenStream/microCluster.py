#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:46:51 2017

@author: anr.putina
"""

import math
import numpy as np


def compute_reduction_factor(lamb, steps):
    return math.pow(2, -lamb * steps)


class MicroCluster:
    def __init__(self, current_timestamp, lamb, cluster_number):
        self.dimensions = None
        self.creationTimeStamp = current_timestamp
        self.lamb = lamb
        self.reductionFactor = compute_reduction_factor(self.lamb, 1)
        self.clusterNumber = cluster_number
        self.N = 0
        self.weight = 0
        self.LS = None
        self.SS = None
        self.center = None
        self.radius = 0

    def insert_sample(self, sample):

        if self.dimensions is None:
            self.dimensions = len(sample.value)
            # incremental parameteres ###
            self.N = 0
            self.weight = 0
            self.LS = np.zeros(self.dimensions)
            self.SS = np.zeros(self.dimensions)
            self.center = np.zeros(self.dimensions)
            self.radius = 0 

        self.N += 1
        self.update_real_time_weight()
        self.update_real_time_ls_and_ss(sample)
        
    def update_real_time_weight(self):
        
        self.weight *= self.reductionFactor
        self.weight += 1
        
    def update_real_time_ls_and_ss(self, sample):
        self.LS = np.multiply(self.LS, self.reductionFactor)
        self.SS = np.multiply(self.SS, self.reductionFactor)
                
        self.LS = self.LS + sample.value
        self.SS = self.SS + sample.value**2

        self.center = np.divide(self.LS, float(self.weight))

        lsd = np.power(self.center, 2)
        ssd = np.divide(self.SS, float(self.weight))

        max_rad = np.nanmax(np.sqrt(ssd.astype(float)-lsd.astype(float)))
        # maxRad = np.nanmax(np.lib.scimath.sqrt(SSd-LSd))
        self.radius = max_rad

    def no_new_samples(self):
        self.LS = np.multiply(self.LS, self.reductionFactor)
        self.SS = np.multiply(self.SS, self.reductionFactor)
        self.weight = np.multiply(self.weight, self.reductionFactor)
                
    def get_center(self):
        return self.center

    def get_radius(self):
        return self.radius
