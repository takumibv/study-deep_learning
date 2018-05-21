# coding:utf-8
# 正規方程式

import numpy as np
import re

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


    for train_num in range(len(full_text_arr)):
        if train_num < 2 :
            continue
        if train_num % 20:
            continue

        train_data = []
        test_data = []
        for i, data in enumerate(table_data):
            if i < train_num :
                train_data.append(data)
            else:
                test_data.append(data)

        ###
        # train phase
        ###
        X_train = np.matrix(train_data)
        X_train = np.double(X_train[:])

        Y = X_train[:, 0]
        X_train = np.delete(X_train, 0, 1)
        X_train = np.insert(X_train, 0, 1, axis=1)

        w = np.linalg.pinv(X_train.T * X_train) * X_train.T * Y # pinv: 擬逆行列.
        w_len = np.linalg.norm(w)

        # print w

        ###
        # test phase
        ###

        X_test = np.matrix(test_data)
        X_test = np.double(X_test[:])

        y_label = X_test[:, 0]

        X_test = np.delete(X_test, 0, 1)
        X_test = np.insert(X_test, 0, 1, axis=1)

        y_test = X_test * w

        result = (y_label == np.round(y_test)).T

        success = len(np.where(result == True)[0])
        rate = int(float(success) / (result.size) * 100)

        # print str(success) + "/" + str(result.size)
        # print "正解率：" + str(float(success)/(result.size) * 100) + " %"
        print("%4d |" % train_num + rate*"=" + (100 - rate)*" " + "|" + str(rate) +"%")
    # print np.double(X[:])
