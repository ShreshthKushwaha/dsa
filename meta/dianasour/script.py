#You will be supplied with two data files in CSV format .
#The first file contains statistics about various dinosaurs. The second file contains additional data.
#Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
#Where g = 9.8 m/s^2 (gravitational constant)

#Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
#Do not print any other information.





import os
import csv
from math import sqrt

def calculate_speed(leg_length, stride_length):
    g = 9.8  # m/s^2 (gravitational constant)
    return ((stride_length / leg_length) - 1) * sqrt(leg_length * g)

def read_csv1(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row['NAME']] = {
                'leg_length': float(row.get('LEG_LENGTH')),
                'diet': row.get('DIET')
            }
    return data
def read_csv2(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row['NAME']] = {
                'stride_length': float(row.get('STRIDE_LENGTH')),
                'stance': row.get('STANCE')
            }
    return data


script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, 'dataset2.csv')

dataset2 = read_csv2(file_path)
print (dataset2)

print ("------------------------------")

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, 'dataset1.csv')

dataset1 = read_csv1(file_path)

for k in dataset1:
    if k in dataset2:
        for key in dataset2[k]:
            dataset1[k][key]=dataset2[k][key]

      

res = []
print (dataset1)

for e in dataset1:

    if e in dataset1 and 'stance' in dataset1[e] and dataset1[e]['stance']=='bipedal':
        res.append((calculate_speed(dataset1[e]['leg_length'],dataset1[e]['stride_length']),e))
res.sort(reverse=True)
print (res)        




