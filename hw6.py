for i in range(1, 10):
    for j in range(2, 6):  # 2단부터 5단까지
        print(f"{j} x {i} = {i * j:2}", end="\t")
    print()  # 한 줄 띄우기

print()  # 한 줄 띄우기

for i in range(1, 10):
    for j in range(6, 10):  # 6단부터 9단까지
        print(f"{j} x {i} = {i * j:2}", end="\t")
    print()  # 한 줄 띄우기
