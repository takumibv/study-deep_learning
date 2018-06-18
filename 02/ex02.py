
import numpy as np

if __name__ == '__main__':
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    # C = np.array([[9, 6], [1, 5]])
    # D = np.array([[4, 6], [7, 3]])

    C = np.array([])
    aa = np.dot(A, B, C)
    print(aa)
    print(C)

    # X = np.array([1.0, 0.5])
    # W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    # B1 = np.array([0.1, 0.2, 0.3])
    # print(W1.shape)  # (2, 3)
    # print(X.shape)  # (2,)
    # print(B1.shape)  # (3,)
    #
    # A1 = np.dot(X, W1) + B1
    # # Z1 = sigmoid(A1)