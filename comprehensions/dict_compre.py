tea_prices_inr = {"Masala Chai":40,"Lemon Tea":60,"Green Tea":"80"}

tea_prices_yen = {tea:price*2 for tea,price in tea_prices_inr.items()}

print(tea_prices_yen)