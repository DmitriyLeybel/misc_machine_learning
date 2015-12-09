import numpy as np
import random
#Stoachstic gradient descent
def in_random_order(data):
    indexes = [i for i,_ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]


def minimize_stochastic(target_fn, gradient_fn,x, y, theta_0, alpha_0=0.01):
    data =zip(x,y)
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float('inf')
    iterations_no_improvement = 0

    while iterations_no_improvement < 100:
        value = sum( target_fn(x_i,y_i, theta) for x_i,y_i in data)

        if value < min_value:
            min_theta,min_value = theta, value
            iterations_no_improvement = 0
            alpha = alpha_0
        else:
            iterations_no_improvement += 1
            alpha *= .9

        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i,y_i, theta)
            theta = np.subtract(theta, np.multiply(alpha, gradient_i))

        return min_theta

