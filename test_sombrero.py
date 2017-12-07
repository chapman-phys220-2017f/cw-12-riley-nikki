#!/usr/bin/env python3
# Name: Riley Kendall
# Student ID: 2267883
# Email: kenda106@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 12

import numpy as np # Numeric python
import matplotlib.pyplot as plt # Used to plot in python
import nose #enables testing with nosetests3
import sombrero as s #imports code

#Newton's Test #1 : testing x output
def test_Newton1():
    """test_Newton1()
    Tests for the correct x output when Newton code is used.
    """
    a=0
    b=5
    dt=1
    x_initial=0 #initial values are both 0
    y_initial=0
    nu=0 #no nu
    F=0 #no force
    t,x,y=s.Newton(a,b,dt,x_initial,y_initial, nu, F)
    answer = x[4]
    desired = 0.0
    np.testing.assert_almost_equal(answer,desired,0.001)

#Newton's Test #2 : testing y output
def test_Newton2():
    """test_Newton2()
    Tests for the correct y output when Newton code is used
    """
    a=0
    b=5
    dt=1
    x_initial=0 #initial values are both 0
    y_initial=0
    nu=0 #no nu
    F=0 #no force
    t,x,y=s.Newton(a,b,dt,x_initial,y_initial, nu, F)
    answer = y[4]
    desired = 0.0
    np.testing.assert_almost_equal(answer,desired,0.001)

