from matplotlib import pyplot as plt
from functools import partial as p
import random
import scipy.spatial.distance as d

def sum_of_squares(x):
    return sum(xi ** 2 for xi in v)


def difference_quotient(f,x,h):
    return (f(x+h) - f(x))/h


def square(x):
    return x * x


def derivative(x):
    return 2 * x

derivative_estimate = p(difference_quotient, square, h=.00001)
x = range(-10,10)
# plt.scatter(x, [derivative(y) for y in x])
# plt.scatter(x, [derivative_estimate(y) for y in x])
# plt.legend(loc=9)
# plt.show()

#ith partial dq
def partial_difference_quotient(f,v,i,h):
    w = [vj + (h if j == i else 0)
         for j, v_j in enumerate(v)]

    return (f(w)-f(v))/h

def estimate_gradient(f, v, h=.00001):
    return [partial_difference_quotient(f,v,i,h)
            for i, _ in enumerate(v)]

def step(v, direction, step_size):
    return [vi +step_size * directioni
            for vi,directioni in zip(v,direction)]

def sum_of_squares_gradient(v):
    return [2 * vi for vi in v]

v = [random.randint(-10,10) for i in range(3)]
tolerance = .00001

# Finds the 3D array that approaches 0,0,0
while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -.01)
    if d.euclidean(next_v, v) < tolerance:
        break
    v = next_v

step_sizes =[10**x for x in range(-5,3)]
def safe(f):
    def safe_f(*args, **kwargs):
        try:
            return f(*args,**kwargs)
        except:
            return float('inf')
    return safe_f

'''Want to minimize target function, with gradient function. Target function contains something like errors as a function
of its parameters
'''
# theta_0 as starting vals
def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=.000001):
    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta,gradient,-step_size)
                       for step_size in step_sizes]
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next,value





