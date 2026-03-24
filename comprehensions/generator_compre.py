# generators are way to save memory (stream values one by one)

total_sales = [10, 20, 6, 8 , 5, 16]

sum_sales = sum(sale for sale in total_sales)

print((sum_sales))