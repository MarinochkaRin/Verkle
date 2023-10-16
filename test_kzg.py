import kzg
import random
import string
from polynomial import evaluate_polynomial

def calculate_keys(data):
    keys = []
    for i in range(len(data)):
        key = bin(i).replace("0b", "")
        keys.append(key[:(len(data) // 2) + 1])
    return keys

def generate_strings(num_strings, data):
    
    string_length = 62*4
    
    for _ in range(num_strings):
        generated_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(string_length))
        data.append(generated_string)

if __name__=='__main__':
    print("run kzg proof test:")

    for i in range(2):
        setup_g1, s_g2 = kzg.trusted_setup()

        print('point')
        points, poly = kzg.encode_as_polynomial()


        print('poly')
        print(poly)

        # create kzg commitment to P(x) using public trusted_setup curve points
        C = kzg.commit(poly, setup_g1)
        print('2')
        print(C)
        # choose some point on P(x) to prove
        point = (1, evaluate_polynomial(poly,1))
        print(point)

        # create kzg proof
        pi = kzg.proof(poly, point, setup_g1)
        print('4')

        # verifier can verify proof that some (x,y) point is on P(x)
        # with only commitment C, proof pi, the point in question
        # and public trusted_setup curve points

        assert kzg.verify(C,pi,point,s_g2), "test fail: valid proof rejected"

        # evidence that proof only passes with the correct point
        wrong_point=(point[1], point[0])
        assert not kzg.verify(C,pi,wrong_point,s_g2), "test fail: uncaught invalid proof"

        print("SUCCESS!")
        i=i+1