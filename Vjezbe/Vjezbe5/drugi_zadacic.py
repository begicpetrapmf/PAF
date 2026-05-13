def iteracije(N):
    x = 5.0
    for i in range(N):
        x += 1/3
    for i in range(N):
        x -= 1/3
    return x

print(iteracije(200))
print(iteracije(2000))
print(iteracije(20000))