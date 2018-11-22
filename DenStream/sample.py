#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:48:21 2017

@author: anr.putina
"""


class Sample:
    
    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = 0
        self.real_timestamp = timestamp
        self.micro_cluster_number = 0
        
    def get_value(self):
        return self.value
    
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
        
    def set_real_timestamp(self, timestamp):
        self.real_timestamp = timestamp

    def set_micro_cluster_number(self, micro_cluster_number):
        self.micro_cluster_number = micro_cluster_number
