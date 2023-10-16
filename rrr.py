
import random
import string
import hashlib
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

#Entering X and Y values
def lag(x, y):


    '''x =np.array([8.5, 10, 12], float)
    y =  list(np.cos((np.pi / 4) * x)*x)'''

    print('x=',x)
    print('y=',y)

    poly = lagrange(x, y)

    #Equation coefficients
    print('coef=',Polynomial(poly).coef)

    #Enter the point at which you want to calculate
    z = float(input('Enter the point at which you want to calculate:'))
    print("The value of polynomial: ","%.3f"%poly(z))

    #Plot 
    step = 0.1
    x_list = np.arange(x[0], x[-1]+0.1, step).tolist()
    y_list = poly(x_list)
    fig = figure(figsize=(8, 8), dpi=75)
    font1 = {'color':'blue','size':15}
    plt.scatter(x,y, marker='*', c='purple', s=250)
    plt.plot(x_list, y_list, 'b-')
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Function', fontsize=12)
    plt.title('Lagrange Interpolation Method', fontdict=font1, loc='left')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend(['Interpolation', 'Data'], loc ="lower right")
    plt.show()

def generate_strings(num_strings, data):
    string_length = 8
    
    for _ in range(num_strings):
        generated_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(string_length))
        data.append(generated_string)

def calculate_keys(data):
    keys = []
    for i in range(len(data)):
        key = bin(i).replace("0b", "")
        keys.append(key[:(len(data) // 2) + 1])
    return keys

def hash_data(point):
    hashed_data = hashlib.sha256((point).encode()).hexdigest()
    return hashed_data



def connect_to_points(keys, data):
  points = []
  for i in range(4):
    key = keys[i]
    data = data[i]
    point = (key, data)
    points.append(point)
  return points

if __name__ == '__main__':

    num_strings = int(input("Введіть кількість рядків (яка є степенем 2): "))
    data = []  # Масив для зберігання рядків
    generate_strings(num_strings, data)
    keys = calculate_keys(data)
    hashed_data = {}
    l = 2774231777737235353
    #
    print("дані", data)
    print("ключі", keys)
    points = []
    for i in range(len(data)):
        key = keys[i]
        dat = data[i]
        point = (key, dat)
        points.append(point)
    print(points)
    for point in points:
        print(hash(point)%l)