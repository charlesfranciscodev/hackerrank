#!/bin/python3

# Linear regression via Gradient Descent

import sys
from numpy import *


# find the last point before hitting max battery time
def find_index(points, max_battery_time):
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        if (y == max_battery_time):
            return i
    return 0


# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))


def step_gradient(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]


def runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, points, learning_rate)
    return b, m


original_points = genfromtxt("trainingdata.txt", delimiter=",")
sorted_points = array((original_points[original_points[:, 1].argsort()]))
max_battery_time = 8
slice_index = find_index(sorted_points, max_battery_time)
max_x = sorted_points[slice_index - 1][0]
points = sorted_points[0:slice_index]
learning_rate = 0.01
initial_b = 0  # initial y-intercept guess
initial_m = 0  # initial slope guess
num_iterations = 2000
b, m = runner(points, initial_b, initial_m, learning_rate, num_iterations)

# read input
charge_time = float(input().strip())
discharge_time = 0
if (charge_time <= max_x):
    # y = mx + b
    discharge_time = m * charge_time + b
else:
    discharge_time = max_battery_time
print(round(discharge_time, 2))
