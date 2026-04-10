def calculate_price(item,quantity):
    try:
        price = {"masala":20}[item]
        if(type(quantity) != int):
            raise ValueError("Quantity should be a integer")

        totalPrice = price * quantity
        print(f"Price is {totalPrice}")

    except KeyError:
        print(f"We dont servce this chai")
    except ValueError as e:
        print(f"Error , {e}" )


calculate_price("Ginger",2)
calculate_price("masala","two")