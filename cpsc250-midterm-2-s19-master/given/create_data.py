import math

"""
Methods used to generate data files, provided here to allow for testing after reading files
 
"""


def make_csv_data(nsteps):
    iv=[]
    x=[]
    y=[]
    for i in range(0,nsteps):
        iv.append(i)
        x.append(2.0*math.pi*i/nsteps)
        y.append(math.cos(x[i]))

    return iv,x,y


def make_binary_data(nsteps):
    x=[]
    y=[]
    iv=[]
    for i in range(0,nsteps):
        iv.append(i)
        x.append(6.0*math.pi*i/nsteps)
        y.append(math.sin(x[i])*math.cos(x[i]))

    return x,y,iv


def make_sample_binary_data(nsteps):
    x=[]
    y=[]


    for i in range(0, nsteps):
        x.append(i)
        y.append(i ** 3)

    return x,y
