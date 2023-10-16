
from addbls12381 import Scalar, Point
#from lagranzh import  lagrange

import addbls12381
import random
import string


class intData:
    def __init__(self, datablocks: list, exponent: int):
        # the number of children of parent node is 2 ** exponent. exponent is not checked
        self.exponent = exponent
        self.datablocks = datablocks

    def hashAllCurrNodes(self, nodes: list) -> list:
        return [addbls12381.hash_to_scalar(node) for node in nodes]

    def testData(self) -> Point:
        veclen = 16
        print("data in verkle tree",veclen)
        currnodes = self.datablocks
      
        nodehashes = self.hashAllCurrNodes(currnodes)

        for i in range(0, len(nodehashes), 16):
            coords = [(int(j + 1), int(hash)) for j, hash in enumerate(nodehashes[i:i + veclen])]
        #    poly = lagrange(coords)   # polynomial coefficients
            

        return coords#, poly   
        
def generate_strings(num_strings, data):
    string_length = 8
    
    for _ in range(num_strings):
        generated_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(string_length))
        data.append(generated_string)

def test():
    num_strings = 16
        
    data = []  # Масив для зберігання рядків
    generate_strings(num_strings, data)
    print("дані",data)


    verkledata = intData(data, 4)   
    #print (verkledata)
    coords = verkledata.testData()   # root commitment is a Point
    return coords#, poly

if __name__ == '__main__':
    # len(data) should be a power of 2 ** exponent...
    # source: https://www.random.org/strings/

    # num_strings = 2
        
    # data = []  # Масив для зберігання рядків
    # generate_strings(num_strings, data)
    # print("дані",data)


    # verkledata = intData(data, 1)   
    #print (verkledata)
    coords = test()   # root commitment is a Point
    print (coords)
    # print (poly)