# coding:utf-8
import sys, os
sys.path.append(os.getcwd()) # import先を実行ディレクトリからの参照にする.
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)