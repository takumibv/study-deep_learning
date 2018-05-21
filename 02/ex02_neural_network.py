# coding:utf-8
# 3章 ニューラルネットワーク
# p.44 ステップ関数の実装(グラフ表示まで)


import numpy as np
import matplotlib.pylab as plt

def step(x):
    if x > 0:
        return 1
    else:
        return 0

def step_arr(x):
    return np.array(x > 0, dtype=np.int)

if __name__ == '__main__':
    # print step(-1)
    x = np.arange(-0.5, 0.5, 0.01)
    y = step_arr(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()