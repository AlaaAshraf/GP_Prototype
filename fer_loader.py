#cd desktop/GP_Prototype/src

import csv
import numpy as np

def load_data_wrapper():
    reader = csv.reader(open('fer2013.csv'))
    #training_inputs = []
    #training_results = []
    #validation_inputs = []
    #validation_results = []
    #testing_inputs = []
    #testing_results = []
    training_inputs = [np.reshape(row[1].split(), (2304, 1)) for row in reader if row[2]=='Training']
    reader = csv.reader(open('fer2013.csv'))
    training_results = [vectorized_result(row[0]) for row in reader if row[2]=='Training']
    reader = csv.reader(open('fer2013.csv'))
    training_data = zip(training_inputs, training_results)
    reader = csv.reader(open('fer2013.csv'))
    validation_inputs = [np.reshape(row[1].split(), (2304, 1)) for row in reader if row[2]=='PublicTest']
    reader = csv.reader(open('fer2013.csv'))
    validation_results = [row[0] for row in reader if row[2]=='PublicTest']
    reader = csv.reader(open('fer2013.csv'))
    validation_data = zip(validation_inputs, validation_results)
    reader = csv.reader(open('fer2013.csv'))
    test_inputs = [np.reshape(row[1].split(), (2304, 1)) for row in reader if row[2]=='PrivateTest']
    reader = csv.reader(open('fer2013.csv'))
    test_results = [row[0] for row in reader if row[2]=='PrivateTest']
    reader = csv.reader(open('fer2013.csv'))
    test_data = zip(test_inputs, test_results)
    #for row in reader:
     #   if row[2]=='Training':
      #      training_inputs.append(np.reshape(row[1].split(),(48*48,1)))
       #     training_results.append(vectorized_result(int(row[0])))
        #elif row[2]=='PublicTest':
         
            #validation_inputs.append(np.reshape(int(row[1].split()),(48*48,1)))
            #validation_results.append(int(row[0]))
        #elif row[2]=='PrivateTest':
         #   testing_inputs.append(np.reshape(int(row[1].split()),(48*48,1)))
          #  testing_results.append(int(row[0]))
    #training_data = zip(training_inputs, training_results)
    #validation_data = zip(validation_inputs, validation_results)
    #testing_data = zip(testing_inputs, testing_results)
    print len(training_inputs)
    print len(training_inputs[0])
    print len(validation_inputs)
    print len(validation_data)
    print len(test_inputs)
    print len(test_data)
    return (training_data, validation_data, test_data)    


def vectorized_result(j):
    """Return a 7-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert an emotion
    into a corresponding desired output from the neural network."""
    e = np.zeros((7, 1))
    e[j] = 1.0
    return e                   
#Training, PublicTest, PrivateTest