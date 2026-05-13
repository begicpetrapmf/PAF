import statistics
brojevi = []
print("Unesite 10 brojeva:")

for i in range(10):
    broj = float(input(f"Unesite broj {i+1}: "))
    brojevi.append(broj)

sredina = statistics.mean(brojevi)
std_dev = statistics.stdev(brojevi)

print(f"Aritmeticka sredina = {sredina}")
print(f"Standardna devijacija = {std_dev}")