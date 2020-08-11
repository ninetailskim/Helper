import paddle
import paddle.fluid as fluid
from paddle.fluid.dygraph import Linear
import pandas as pd
import numpy as np
import matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
import math
batch_size = 10
epoch = 50
lambdaES = 1000
def draw_train_acc(w0, w1, w2, w3, w4, w5, w6):
    title="SGD"
    plt.title(title, fontsize=24)
    plt.xlabel("lambda", fontsize=14)
    plt.ylabel("wn", fontsize=14)
    plt.plot(w0, w1, color='green', label='1')
    plt.plot(w0, w2, color='red', label='70')
    plt.plot(w0, w3, color='yellow', label='140')
    plt.plot(w0, w4, color='blue', label='210')
    plt.plot(w0, w5, color='black', label='280')
    plt.plot(w0, w6, color='pink', label='350')
    plt.legend()
    plt.grid()
    plt.show()

class MyLinear(fluid.Layer):
    def __init__(self):
        super(MyLinear, self).__init__()
        self.fc = Linear(501,1)

    def forward(self, x):
        res = self.fc(x)
        return res

def readfile(filename):
    data = []
    filecsv = pd.read_csv(filename)
    for i in range(150):
        data.append(filecsv.loc[i].tolist())
    return data
    
alldata = readfile('data.csv')

# print(alldata)

def Train_data_reader(alldata):
    def reader():
        for data in alldata:
            yield data
    return reader

shuffle_data = fluid.io.shuffle(Train_data_reader(alldata), 150)

train_reader = paddle.batch(shuffle_data,
                            batch_size=batch_size,
                            drop_last=True)

def checkNan(num):
    if math.isinf(num) or math.isnan(num):
        return False
    else:
        return True

lambdaE = 1
w1 = []
w2 = []
w3 = []
w4 = []
w5 = []
w6 = []
w0 = []

for i in range(lambdaES):
    lambdaE = i
    w0.append(lambdaE)
    w1.append(0)
    w2.append(0)
    w3.append(0)
    w4.append(0)
    w5.append(0)
    w6.append(0)
    print(lambdaE)
    with fluid.dygraph.guard():
        fc = MyLinear()
        opt=fluid.optimizer.SGDOptimizer(learning_rate=0.0001, parameter_list=fc.parameters())
        breakFlag = False

        for e in range(epoch):
            if breakFlag:
                break
            for x in train_reader():
                # print(x)
                # print(x[0])
                my = []
                mx = []
                for xy in x:
                    # print(xy)
                    my.append([xy[0]])
                    t = xy[1:]
                    t.append(1)
                    mx.append(t)
                ix = fluid.dygraph.to_variable(np.array(mx,dtype=np.float32))
                iy = fluid.dygraph.to_variable(np.array(my,dtype=np.float32))
                # print(ix.shape)
                res_y = fc(ix)

                loss1 = fluid.layers.mean(fluid.layers.reduce_sum(fluid.layers.pow(res_y - iy, 2)))
                loss = loss1 + lambdaE * fluid.layers.reduce_sum(fluid.layers.abs(fc.fc.weight.detach()))

                loss.backward()
                opt.minimize(loss)    #优化器对象的minimize方法对参数进行更新 
                fc.clear_gradients()
                ffwn = fc.fc.weight.numpy()

                if checkNan(ffwn[1,0]):
                    w1[len(w1) - 1] = ffwn[1,0]
                if checkNan(ffwn[70,0]):
                    w2[len(w2) - 1] = ffwn[70,0]
                if checkNan(ffwn[140,0]):
                    w3[len(w3) - 1] = ffwn[140,0]
                if checkNan(ffwn[210,0]):
                    w4[len(w4) - 1] = ffwn[210,0]
                if checkNan(ffwn[280,0]):
                    w5[len(w5) - 1] = ffwn[280,0]
                if checkNan(ffwn[350,0]):
                    w6[len(w6) - 1] = ffwn[350,0]
                else:
                    breakFlag = True
                    break
        
        draw_train_acc(w0, w1, w2, w3, w4, w5, w6)

