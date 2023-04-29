import geopy.distance

def cord(cord1, cord2):
    return geopy.distance.geodesic(cord1, cord2).km

def time_to_bus(bus_speed, bus_cord=(0, 0), bus_stop_cord=(0, 0)): 
    # bus_cord=(Широта, Долгота) | bus_cord=(47.274130, 39.718310), bus_stop_cord=(47.294600, 39.713650) == 2км
    if bus_speed == 0:
        bus_speed = 10
    distance = round(cord(bus_cord, bus_stop_cord), 4)
    time_hour = round(distance/bus_speed, 1)
    time_min = round((distance/bus_speed)*60)
    return time_hour, time_min

if __name__ == '__main__':
    print(time_to_bus(50, (12,12), (13,13)))