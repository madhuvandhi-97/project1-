"""pattern1"""
for z in range(1,6):
    for a in range(1,z+1):
        print(a, end="")
    print("\r")
print("\r")

"""pattern2"""
k=1
for z in range(1,6):
    for a in range(1,z+1):
        print(k, end="")
        k+=1
    print("\r")
print("\r")

"""pattern3"""
for z in range(1,6):
    for a in range(1,z+1):
        print('*', end="")
    print("\r")
print("\r")

"""pattern4"""
for z in range(6,0,-1):
    for a in range(1,z):
        print(a, end="")
    print("\r")
print("\r")

"""pattern5"""
for z in range(1,6):
    for a in range(1,z+1):
        print(a, end="")
    print("\r")
for z in range(6,0,-1):
    for a in range(1,z+1):
        print(a, end="")
    print("\r")