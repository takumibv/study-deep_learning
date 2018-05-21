# coding: utf-8
import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

# 2章 パーセプトロン
# 
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp > 0:
        return 1
    else:
        return 0

def OR_def(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x * w) + b
    if tmp >= 0:
        return 1
    else:
        return 0

def AND(x1, x2):
    return NAND(NAND(x1, x2), NAND(x1, x2))

def OR(x1, x2):
    return NAND(NAND(x1, x1), NAND(x2, x2))

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = NAND(NAND(x1, x1), NAND(x2, x2))
    s3 = NAND(s1, s2)
    return NAND(s3, s3)

if __name__ == '__main__':
    print("NAND")
    print(NAND(0, 0))
