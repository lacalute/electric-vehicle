# import necessary libraries
import csv
import matplotlib.pyplot as plt
# import the web-server code
from map import *

# open the csv file
with open('el.csv') as f:
    reader = csv.reader(f)
    x = list(reader)
    # a variable with titles
    titles = x[0]
    # delete the titles
    x.pop(0)
print(titles)

# indexes of csv file
# 3 - state
# 2 - city
# 6 - brand of car
# 7 - model of car
# 5 - year of car
# 14 - the vehicle location

# the loop, which collect the list of states and list of cities for each state
states = []
cities = []
for collect_states in x:
    if collect_states[3] not in states:
        cities.append(dict({'state': collect_states[3], 'cities': []}))
        states.append(collect_states[3])
    elif collect_states[3] in states:
        for ff in cities:
            if ff['state'] == collect_states[3] and collect_states[2] not in ff['cities']:
                ff['cities'].append(collect_states[2])

# the main func, which collect the necessary data for visualization (st - state, ct - city)
def collect(st, ct):
    global d
    states = [] # the list with states
    cars = [] # the list with cars model 
    data = [] # the main list with dictionaries, filled with data about each model of car
    # the data dict has this structure:
    
    # [{'model': str(*model), 'points': [*points], 'times': int(*times)}]
    # model = the full name of car model (full_car)
    # points = the coordinats with location of car (as a list)
    # times = the number, which show how much times car is there in that states and in that city

    # the main loop, which do all things above
    for coll_s in x:
        full_car = f'{coll_s[6]} {coll_s[7]} {coll_s[5]}' # the full name of car model
        if coll_s[3] == st and coll_s[2] == ct:
            print(coll_s)
            # if model of car haven't been in list yet, then creating a new dict object
            if full_car not in cars:
                data.append(dict({'model': full_car, 'points': coll_s[14], 'times': 0})) # fill the data list
                cars.append(full_car) # fill the list with cars models
            # but if model is repearing, then we change the var +1
            elif full_car in cars:
                for g in data:
                    if g['model'] == full_car:
                        g['times'] = g['times'] + 1
    # after collect the data, we need to sort them and delete non-necessary data
    data_sorted = sorted(data, key=lambda item: item['times'])
    for test in data_sorted:
        print(test)
    for w in data_sorted:
        # all cars models, which are repeating 0 times - just deleting 
        if w['times'] == 0:
            data.remove(w)
    # the d list is final data
    d = []
    labels = []
    # use [-5:] is giving the list with the most populate models of cars
    for cl in data_sorted[-5:]:
        d.append(cl['times'])
        labels.append(cl['model'])

    # the func, which create a diagram
    def plotting():
        plt.style.use('ggplot')
        plt.title(f'How much electric cars in {st}, {ct}')
        plt.barh(labels, d)
        plt.show()
    plotting()
# the main loop of program
status = True
while status:
    try:
        print("1 - Diagramm\n2 - The map of vehicles locations")
        choice = int(input("Choose the option -> "))
        # create a diagram
        if choice == 1:
            print(states)
            ask_state = str(input("Type the state -> "))
            if ask_state in states:
                for print_cities in cities:
                    if print_cities['state'] == ask_state:
                        print(print_cities['cities'])
                        break
                ask_city = str(input("Type the city -> "))
                for test_city in cities:
                    if test_city['state'] == ask_state:
                        if ask_city in test_city['cities']:
                            collect(ask_state, ask_city)
                            status = False
                        else:
                            print('Type another data')
            else:
                print("Type another state")
        # create a map with markers
        if choice == 2:
            print("This option is developing right now. Sorry :)")
            status = False
        else:
            print("Wrong option, please choose option again")
    except ValueError:
        print("Wrong data type, please type again")

# Program by Lacalute !!!