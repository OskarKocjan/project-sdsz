from Car import Car
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import json
from numpy import arange



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
    data['number_of_cars'] = []
    data['time'] = []

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)



def append_data(avg_v, avg_vmax, diffrence_v_vmax, i, number_cars, time):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        data['avg_v'].append(avg_v)
        data['avg_vmax'].append(avg_vmax)
        data['iteration'].append(i)
        data['diffrence_v_vmax'].append(diffrence_v_vmax)
        data['number_of_cars'].append(number_cars)
        data['time'].append(time)
        
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile,indent=2)




def add_stats(cars, i, time):

    avg_v, avg_vmax, diffrence_v_vmax = average_v(cars)
    append_data(avg_v, avg_vmax, diffrence_v_vmax, i, len(cars), time)



def run_stats():
    style.use('fivethirtyeight')
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ani = animation.FuncAnimation(fig, animate, interval=1000, fargs = (ax1, ) )
    plt.show()



def plot_numcars_v(inflow, amount_of_inflow):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        v = data['avg_v']
        num_cars = data['number_of_cars']

    plt.plot(num_cars, v, 'b.')
    plt.xlabel('Number of Cars')
    plt.ylabel('Average velocity (V)')
    plt.savefig('V_num_cars' + str(inflow) + '_' + str(amount_of_inflow))
    #plt.show()


def plot_t_numcars(inflow, amount_of_inflow):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        t = data['time']
        num_cars = data['number_of_cars']
        plt.plot(t, num_cars)
        plt.xlabel('Time (t)')
        plt.ylabel('Number of Cars')
        plt.savefig('Num_cars_t' + str(inflow) + '_' + str(amount_of_inflow))
        #plt.show()


def plot_t_v(inflow, amount_of_inflow):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        t = data['time']
        v = data['avg_v']
        vmax = data['avg_vmax']

        plt.xlabel('Time (t)')
        plt.ylabel('Velocity (V)')
        plt.plot(t, v, t, vmax)
        plt.savefig('V_t_' + str(inflow) + '_' + str(amount_of_inflow))
        #plt.show()


def plot_inflow(filharmonia_list, idziego_list, poczta_list, slowackiego_list, bagatela_list, inflow, amount_of_inflow):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        time = data['time'][len(data['time']) - 1]

    time = int(time)
    t = arange(0, time, time/len(filharmonia_list))
    t = list(t)


    plt.xlabel('Time (t)')
    plt.ylabel('Outflow')
    plt.plot(t, filharmonia_list, t, idziego_list, t, poczta_list, t, slowackiego_list, t, bagatela_list)
    plt.legend(('Filharmonia', 'Idziego', 'Poczta', 'Słowackiego', 'Bagatela'))
    plt.savefig('Inflow_t_' + str(inflow) + '_' + str(amount_of_inflow))
    #plt.show()