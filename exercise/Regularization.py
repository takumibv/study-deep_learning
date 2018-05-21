# coding:utf-8
# 正則化

import numpy as np
import re

TRAIN_NUM = 3000

if __name__ == '__main__':
    file_name = "dataset/data1.txt"
    full_text = open(file_name).read()
    full_text_arr = full_text.split('\n')
    table_head = []
    table_data = []

    for i, line in enumerate(full_text_arr):
        data = re.split(r'\t', line.rstrip('\r'))
        for j, d in enumerate(data):
            data[j] = d.replace(" ", "0")
        if i == 0:
            table_head = data
        else:
            table_data.append(data)

    # train_data, test_data 振り分け
    train_data = []
    test_data = []
    for i, data in enumerate(table_data):
        if i < TRAIN_NUM:
            train_data.append(data)
        else:
            test_data.append(data)

    # X_train, Y 振り分け
    X_train = np.matrix(train_data)
    X_train = np.double(X_train[:])

    Y = X_train[:, 0]
    X_train = np.delete(X_train, 0, 1)
    X_train = np.insert(X_train, 0, 1, axis=1)

    w = np.linalg.pinv(X_train.T * X_train) * X_train.T * Y  # pinv: 擬逆行列.
    w_len = np.linalg.norm(w)