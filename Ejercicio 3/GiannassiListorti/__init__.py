import random
import math
from os import system, name

BUSY = 1
Q_LIMIT = 100
IDLE = 0
model = {
    "next_event_type": 0,
    "num_custs_delayed": 0,
    "num_delays_required": 0,
    "num_events": 0,
    "num_in_q": 0,
    "server_status": 0,
    "area_num_in_q": 0.0,
    "area_server_status": 0.0,
    "mean_interarrival": 0.0,
    "mean_service": 0.0,
    "time": 0.0,
    "time_arrival": [] * (Q_LIMIT + 1),
    "time_last_event": 0.0,
    "time_next_event": [] * 3,
    "total_of_delays": 0.0
}


def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def initialize():
    model["time"] = 0.0
    model["server_status"] = IDLE
    model["num_in_q"] = 0
    model["time_last_event"] = 0.0
    model["num_custs_delayed"] = 0
    model["total_of_delays"] = 0.0
    model["area_num_in_q"] = 0.0
    model["area_server_status"] = 0.0
    model["time_next_event"].insert(0, float(model["time"]+expon(model["mean_interarrival"])))
    model["time_next_event"].insert(1, float(1e+30))


def timing():
    model["min_time_next_event"] = 1.0E29
    model["next_event_type"] = 0
    for i in range(1, model["num_events"]):
        if (model["time_next_event"][i] < model["min_time_next_event"]):
            model["min_time_next_event"] = model["time_next_event"][i]
            model["next_event_type"] = i
    if (model["next_event_type"] == 0):
        print("Event list empty at time "+str(model["time"]))
    model["time"] = model["min_time_next_event"]


def update_time_avg_stats():
    model["time_since_last_event"] = model["time"]-model["time_last_event"]
    model["time_last_event"] = model["time"]
    model["area_num_in_q"] = model["area_num_in_q"] + model["num_in_q"] * model["time_since_last_event"]
    model["area_server_status"] = model["area_server_status"] + model["server_status"] * model["time_since_last_event"]


def expon(mean):
    u = random.random()
    return -mean * math.log(u)


def arrive():
    model["time_next_event"][0] = model["time"] + expon(model["mean_interarrival"])
    if(model["server_status"] == BUSY):
        model["num_in_q"] += 1
        if(model["num_in_q"] > Q_LIMIT):
            print("Overflow of the array time_arrival at time: "+str(model["time"]))
        model["time_arrival"][model["num_in_q"]] = model["time"]
    else:
        model["delay"] = 0.0
        model["total_of_delays"] += model["delay"]
        model["num_custs_delayed"] += 1
        model["server_status"] = BUSY
        model["time_next_event"][1] = model["time"]+expon(model["mean_service"])


def depart():
    if(model["num_in_q"] == 0):
        model["server_status"] = IDLE
        model["time_next_event"][1] = 1.0E30
    else:
        model["num_in_q"] = model["num_in_q"] - 1
        model["delay"] = model["time"] - model["time_arrival"][0]
        model["total_of_delays"] += model["delay"]
        model["num_custs_delayed"] += 1
        model["time_next_event"][2] = model["time"] + expon(model["mean_service"])
        for i in range(1, model["num_in_q"]):
            model["time_arrival"][i] = model["time_arrival"][i + 1]


def report():
    print("Average delay in queue "+str(model["total_of_delays"]/model["num_cust_delayed"]))
    print("Average number in queue"+str(model["area_num_in_q"]/model["time"]))
    print("Server utilization "+str(model["area_server_status"]/model["time"]))
    print("Time simulation ended "+str(model["time"]))


if __name__ == "__main__":
    clearScreen()
    num_events = 2
    model["mean_interarrival"] = float(
        abs(int(input("Mean Interarrival time(Minutes): "))))
    model["mean_service"] = float(abs((int(input("Mean Service Time(Minutes): ")))))
    model["num_delays_required"] = abs(int(input("Number of Customers: ")))
    initialize()
    while model["num_custs_delayed"] < model["num_delays_required"]:
        timing()
        update_time_avg_stats()
        if model["next_event_type"] == 1:
            arrive()
        elif model["next_event_type"] == 2:
            depart()
    report()
