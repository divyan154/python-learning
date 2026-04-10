def orderChai(type):
    try:
        print(f"Preparing {type} Chai")

        if(type == "unknown"):
            raise KeyError("We dont know this flavor") 

    except KeyError as e:
        print(f"Error : {e}")
    else:
        print(f"{type} Chai is completed")
    finally:
        print("Next customer pleeasee..")        
    

    
orderChai("Masala")
orderChai("unknown")

