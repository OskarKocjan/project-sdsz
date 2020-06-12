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



def plot_numcars_v(inflow, amount_of_inflow, fig, cars):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        v = data['avg_v']
        num_cars = data['number_of_cars']




    plt.figure(fig)
    plt.plot(num_cars, v, 'b.')
    plt.xlabel('Number of Cars')
    plt.ylabel('Average velocity (V)')
    plt.savefig('plots/V_num_cars_' + str(inflow) + '_' + str(amount_of_inflow) + '_' + str(fig) + '_' + str(cars))
    #plt.show()


def plot_t_numcars(inflow, amount_of_inflow, fig, cars):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        t = data['time']
        num_cars = data['number_of_cars']
        plt.figure(fig + 18)
        plt.plot(t, num_cars)
        plt.xlabel('Time (t)')
        plt.ylabel('Number of Cars')
        plt.savefig('plots/Num_cars_t_' + str(inflow) + '_' + str(amount_of_inflow) + '_' + str(fig) + '_' + str(cars))
        #plt.show()


def plot_t_v(inflow, amount_of_inflow, fig ,cars):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        t = data['time']
        v = data['avg_v']
        vmax = data['avg_vmax']


        plt.figure(fig + 36)
        plt.plot(t, v, t, vmax)
        plt.xlabel('Time (t)')
        plt.ylabel('Velocity (V)')
        plt.legend(('V', 'V_max'))
        plt.savefig('plots/V_t_' + str(inflow) + '_' + str(amount_of_inflow) + '_' + str(fig) + '_' + str(cars))
        #plt.show()


def plot_inflow(filharmonia_list, idziego_list, poczta_list, slowackiego_list, bagatela_list, inflow, amount_of_inflow, fig, cars):
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)
        time = data['time'][len(data['time']) - 1]

    time = int(time)
    t = arange(0, time, time/len(filharmonia_list))
    t = list(t)



    plt.figure(fig + 54)
    plt.plot(t, filharmonia_list, t, idziego_list, t, poczta_list, t, slowackiego_list, t, bagatela_list)
    plt.xlabel('Time (t)')
    plt.ylabel('Outflow')
    plt.legend(('Filharmonia', 'Idziego', 'Poczta', 'Słowackiego', 'Bagatela'))
    plt.savefig('plots/Inflow_t_' + str(inflow) + '_' + str(amount_of_inflow)+ '_' + str(fig) + '_' + str(cars))
    #plt.show()



def making_final_data():
    data = {}
    data['simulation_number'] = []
    data['starting_num_cars'] = []
    data['final_num_cars'] = []
    data['starting_v'] = []
    data['end_v'] = []
    data['procent'] = []
    data['min_outflow'] = []
    data['max_outflow'] = []
    data['v_min'] = []
    data['v_max'] = []
    with open('final_data.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)




def final_data_append(sim_number, start_cars, outflow):

    out_max = 0
    out_min = 1000

    for flow in outflow:
        for i in range(len(flow) - 1):
            first = flow[i]
            second = flow[i + 1]
            number = second - first
            if number > out_max:
                out_max = number
            if number < out_min:
                out_min = number


    with open('data.json', 'r') as infile:
        data1 = json.load(infile)
        final_cars = data1['number_of_cars'][len(data1['number_of_cars']) - 1]
        start_v = data1['avg_v'][10]
        end_v = data1['avg_v'][len(data1['avg_v']) - 1]
        procent = sum(data1['diffrence_v_vmax']) / len(data1['diffrence_v_vmax'])
        vmin = min(data1['avg_v'])
        vmax = max(data1['avg_v'])





    with open('final_data.json', 'r') as outfile:
        data2 = json.load(outfile)
        data2['simulation_number'].append(sim_number)
        data2['starting_num_cars'].append(start_cars)
        data2['final_num_cars'].append(final_cars)
        data2['starting_v'].append(start_v)
        data2['end_v'].append(end_v)
        data2['procent'].append(procent)
        data2['min_outflow'].append(out_min)
        data2['max_outflow'].append(out_max)
        data2['v_min'].append(vmin)
        data2['v_max'].append(vmax)

    with open('final_data.json', 'w') as outfile:
        json.dump(data2, outfile, indent=2)