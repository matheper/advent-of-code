"""
--- Day 13: Shuttle Search ---


Your ferry can make it safely to a nearby port, but it won't get much further. When you call to book another ship, you discover that no ships embark from that port to your vacation island. You'll need to get from the port to the nearest airport.

Fortunately, a shuttle bus service is available to bring you from the sea port to the airport! Each bus has an ID number that also indicates how often the bus leaves for the airport.

Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed reference point in the past. At timestamp 0, every bus simultaneously departed from the sea port. After that, each bus travels to the airport, then various other locations, and finally returns to the sea port to repeat its journey forever.

The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the sea port at timestamps 0, 5, 10, 15, and so on. The bus with ID 11 departs at 0, 11, 22, 33, and so on. If you are there when the bus departs, you can ride that bus to the airport!

Your notes (your puzzle input) consist of two lines. The first line is your estimate of the earliest timestamp you could depart on a bus. The second line lists the bus IDs that are in service according to the shuttle company; entries that show x must be out of service, so you decide to ignore them.

To save time once you arrive, your goal is to figure out the earliest bus you can take to the airport. (There will be exactly one such bus.)

For example, suppose you have the following notes:

939
7,13,x,x,59,x,31,19
Here, the earliest timestamp you could depart is 939, and the bus IDs in service are 7, 13, 59, 31, and 19. Near timestamp 939, these bus IDs depart at the times marked D:

time   bus 7   bus 13  bus 59  bus 31  bus 19
929      .       .       .       .       .
930      .       .       .       D       .
931      D       .       .       .       D
932      .       .       .       .       .
933      .       .       .       .       .
934      .       .       .       .       .
935      .       .       .       .       .
936      .       D       .       .       .
937      .       .       .       .       .
938      D       .       .       .       .
939      .       .       .       .       .
940      .       .       .       .       .
941      .       .       .       .       .
942      .       .       .       .       .
943      .       .       .       .       .
944      .       .       D       .       .
945      D       .       .       .       .
946      .       .       .       .       .
947      .       .       .       .       .
948      .       .       .       .       .
949      .       D       .       .       .
The earliest bus you could take is bus ID 59. It doesn't depart until timestamp 944, so you would need to wait 944 - 939 = 5 minutes before it departs. Multiplying the bus ID by the number of minutes you'd need to wait gives 295.

What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?


https://adventofcode.com/2020/day/13
"""

def plan_bus_trip(arriving_time, bus_list):
    bus_in_operation = [b for b in bus_list if b != 0]
    waiting_time = 0
    while True:
        for bus_id in bus_in_operation:
            if (arriving_time + waiting_time) % bus_id == 0:
                return bus_id * waiting_time
        waiting_time += 1


def find_ordered_departour_naive(bus_list):
    bus_map = {bus: index for index, bus in enumerate(bus_list)}
    bus_map.pop(0)
    longest_trip = max(bus_map.keys())
    longest_index = bus_map[longest_trip]
    timestamp = 0
    ordered_departour = False
    while not ordered_departour:
        timestamp += longest_trip
        ordered_departour = True
        for bus, index in bus_map.items():
            if (timestamp + (index - longest_index)) % bus != 0:
                ordered_departour = False
                break
        if ordered_departour:
            return timestamp - longest_index


def find_ordered_departour_improved(bus_list):
    bus_map = {bus: index for index, bus in enumerate(bus_list)}
    bus_map.pop(0)
    timestamp = 1
    offset = 1
    for bus, index in bus_map.items():
        while (timestamp + index) % bus != 0:
            timestamp += offset
        offset *= bus
    return timestamp


def main():
    with open('inputs/day_13.txt') as input_file:
        timestamp = int(input_file.readline())
        bus_list = [int(i) for i in input_file.readline().replace('x','0').split(',')]

    print(plan_bus_trip(timestamp, bus_list))
    # print(find_ordered_departour_naive(bus_list))
    print(find_ordered_departour_improved(bus_list))


if __name__ == '__main__':
    main()