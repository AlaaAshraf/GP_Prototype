#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:56:25 2016

@author: Alaa
"""
cd desktop/GP_Prototype/src
python
import fer_loader
training_data, validation_data, test_data = fer_loader.load_data_wrapper()
import network
net = network.Network([2304, 50, 7])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)