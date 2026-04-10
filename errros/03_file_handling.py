# file = open("order.txt","w")

# try:
#     file.write("ありがとうございます")
# finally:
#     file.close()

with open("orders.txt","w") as f:
    f.write("こんにちは")
