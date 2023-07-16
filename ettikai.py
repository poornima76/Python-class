import pandas as pd
import sys
import math
import numpy as np
df = pd.read_csv('test_scores.csv')

def gradient_descent(x,y):
    m_curr = b_curr = 0
    n = len(x)
    iterations = 1000
    learning_rate = 0.001
    cost_prev = 0
    for i in range(iterations):
        y_pred = m_curr*x + b_curr
        cost = (1/n)*sum([val**2 for val in (y-y_pred)])

        md = -(2/n)*sum(x*(m_curr*x-b_curr))
        bd = -(2/n)*sum((m_curr*x-b_curr))
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost,cost_prev, rel_tol=1e-20):
            break
        cost_prev = cost
        print ("m {}, b {}, cost {}, iteration {}".format(m_curr,b_curr,cost, i))   
x,y = np.array(df.math), np.array(df.cs)
gradient_descent(x,y)