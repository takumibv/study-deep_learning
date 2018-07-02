# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def ReLU(x):
    return np.maximum(0, x)


def tanh(x):
    return np.tanh(x)


input_data = np.random.randn(1000, 100)  # 1000個のデータ
node_num = 100  # 各隠れ層のノード（ニューロン）の数
hidden_layer_size = 5  # 隠れ層が5層
activations = {}  # ここにアクティベーションの結果を格納する

x = input_data

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i - 1]

    # batch normalization => ここではそんなに変わらない
    m = len(x)
    ipsilon = 10e-7
    mu_b = np.average(x, axis=1)
    # gamma_2_b = np.sum(np.power(x-mu_b.reshape(1000, 1), 2), axis=1) / m
    gamma_2_b = np.var(x, axis=1)
    x_new = (x - mu_b.reshape(1000, 1)) / np.sqrt(gamma_2_b.reshape(1000, 1) + ipsilon)
    x = x_new

    # 初期値の値をいろいろ変えて実験しよう！
    w = np.random.randn(node_num, node_num) * 1
    # w = np.random.randn(node_num, node_num) * 0.01
    # w = np.random.randn(node_num, node_num) * np.sqrt(1.0 / node_num) # 「Xavierの初期値」
    # w = np.random.randn(node_num, node_num) * np.sqrt(2.0 / node_num)  # 「Heの初期値」

    a = np.dot(x, w)

    # 活性化関数の種類も変えて実験しよう！
    z = sigmoid(a)
    # z = ReLU(a)
    # z = tanh(a)

    activations[i] = z

# ヒストグラムを描画
for i, a in activations.items():
    plt.subplot(1, len(activations), i + 1)
    plt.title(str(i + 1) + "-layer")
    if i != 0: plt.yticks([], [])
    # plt.xlim(0.1, 1)
    # plt.ylim(0, 7000)
    plt.hist(a.flatten(), 30, range=(0, 1))
plt.show()
