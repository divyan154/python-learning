def generate_chai():
    count = 1
    while True:
        yield f"Count {count}"
        count += 1


user1 = generate_chai()

for _ in range(10):
    print(next(user1))



