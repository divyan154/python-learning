# yeild can also used to send value to generators 

def bucket_list():
    print("Which places would you like to visit??")
    place = yield
    while True:
        print(f"{place} added to bucket list")
        place = yield


places = bucket_list()
next(places)

places.send("Hokkaido")
places.send("okinawa")
places.send("paris")
places.send("Tokyo")
