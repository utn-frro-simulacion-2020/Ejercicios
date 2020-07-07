import random
import math
from os import system, name


Q_LIMIT = 100
BUSY = 1
IDLE = 0
next_event_type = 0
num_custs_delayed = 0
num_delays_required = 0
num_events = 0
num_in_q = 0
server_status = 0
area_num_in_q = 0.0
area_server_status = 0.0
mean_interarrival = 0.0
mean_service = 0.0
time = 0.0
time_arrival = [] * (Q_LIMIT + 1)
time_last_event = 0.0
time_next_event = [] * 3
total_of_delays = 0.0

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def initialize():
    time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    time_next_event.insert(0, float(time+expon(mean_interarrival)))
    time_next_event.insert(1, float(1e+30))

def timing():
    global time
    min_time_next_event = 1.0E29
    next_event_type = 0
    for i in range(1, num_events):
        if (time_next_event[i] < min_time_next_event):
            min_time_next_event = time_next_event[i]
            next_event_type = i
    if (next_event_type == 0):
        print("Event list empty at time "+str(time))
    time = min_time_next_event

def update_time_avg_stats():
    global time_last_event
    global area_num_in_q
    global area_server_status
    time_since_last_event = time-time_last_event
    time_last_event = time
    area_num_in_q = area_num_in_q + num_in_q * time_since_last_event
    area_server_status = area_server_status + server_status * time_since_last_event

def expon(mean):
    u = random.random()
    return -mean * math.log(u)


def arrive():

    time_next_event[0] = time + expon(mean_interarrival)

    if(server_status == BUSY):
        num_in_q += 1
        if(num_in_q > Q_LIMIT):
            print("Overflow of the array time_arrival at time: "+str(time))

        time_arrival[num_in_q] = time

    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY
        time_next_event[1] = time+expon(mean_service)


def depart():
    if(num_in_q == 0):
        server_status = IDLE
        time_next_event[1] = 1.0E30
    else:
        num_in_q = num_in_q - 1
        delay = time - time_arrival[0]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = time + expon(mean_service)
        for i in range(1, num_in_q):
            time_arrival[i] = time_arrival[i + 1]


def report():
    print("Average delay in queue "+str(total_of_delays/num_cust_delayed))
    print("Average number in queue"+str(area_num_in_q/time))
    print("Server utilization "+str(area_server_status/time))
    print("Time simulation ended "+str(time))


if __name__ == "__main__":
    clearScreen()
    num_events = 2
    mean_interarrival = float(abs(int(input("Mean Interarrival time(Minutes): "))))
    mean_service = float(abs((int(input("Mean Service Time(Minutes): ")))))
    num_delays_required = abs(int(input("Number of Customers: ")))
    initialize()
    while num_custs_delayed<num_delays_required:
        timing()
        update_time_avg_stats()
        if next_event_type==1:
            arrive()
        elif next_event_type==2:
            depart()
    report()