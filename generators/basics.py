# dont uses memory --> generators
def get_travel_list():
    yield "Hokkaido"
    yield "Okinawa"
    yield "Tokyo"

travel = get_travel_list()

# for place in travel:
#     print(place)



def get_travel_list_func():
    return ["Hokkaido","Okinawa","Tokyo"]

# print(travel) #not yet executed
# print(travel) #not yet executed
# print(travel) #not yet executed


print(next(travel))
print(next(travel))
print(next(travel))
# print(next(travel))

