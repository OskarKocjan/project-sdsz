from Car import Car
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import json




def average_v(cars):

    sum_v = 0
    sum_vmax = 0
    length = len(cars)

    for i in range(length):
        v = cars[i].get_v()
        if(v == 0):
            pass
        else:
            v = 30 + (v*10)

        vmax = cars[i].get_vmax()
        vmax = 30 + (vmax*10)

        sum_v += v
        sum_vmax += vmax

    avg_v = sum_v / length
    avg_vmax = sum_vmax / length

    diffrence_procent = (avg_v / avg_vmax) * 100

    return avg_v, avg_vmax, diffrence_procent


def animate(i, ax1):

    xs = []
    ys1 = []
    ys2 = []

    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        ys1 = data['avg_v']
        ys2 = data['avg_vmax']
        xs = data['iteration']
    ax1.clear()
    ax1.plot(xs, ys1)


def making_file_statistic():
    data = {}
    data['avg_v'] = []
    data['avg_vmax'] = []
    data['iteration'] = []
    data['diffrence_v_vmax'] = []

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)



def append_data(avg_v, avg_vmax, diffrence_v_vmax, i):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        data['avg_v'].append(avg_v)
        data['avg_vmax'].append(avg_vmax)
        data['iteration'].append(i)
        data['diffrence_v_vmax'].append(diffrence_v_vmax)
        
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)




def add_stats(cars, i):

    avg_v, avg_vmax, diffrence_v_vmax = average_v(cars)
    append_data(avg_v, avg_vmax, diffrence_v_vmax, i)



def run_stats():
    style.use('fivethirtyeight')
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ani = animation.FuncAnimation(fig, animate, interval=1000, fargs = (ax1, ) )
    plt.show()




