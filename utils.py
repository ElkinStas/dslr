
import numpy as np

def log_loss(t, y):
    return np.sum((-t*np.log(y) - (1 - t) * (np.log(1 - y))), keepdims=True).flatten()

def diff_log_loss(t, y):
    return np.sum(-(t/y) -(t -1)/(1-y), keepdims=True)

def sigmoid(z):
    return 1./(1+np.exp(-z))

class Sorting_Hat:
    def __init__(self, n_inp, n_out, lr=0.1):
        self.shape = (n_inp, n_out) #залетают входящие и выходящие значения
        self.lr = lr #шаг обучения
        self.w = np.array([[0],[0],[0],[0],[0],[0]])
        self.b = 0
    def __call__(self, x, w,b): #вызов класса
        if len(x.shape) == 1: #если входящие значения одноразмерны - сменить размерность
            x = x.reshape(1, -1)
        self.inp = x #задаем входные значения
        self.w = w
        self.activations = sigmoid(x.astype(np.float64).dot(self.w) + self.b) #запуск функции с функцией активации
        return self.activations