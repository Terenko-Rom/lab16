data = []
with open("data.txt", "r") as file:
    for line in file:
        row = list(map(int, line.split()))
        data.extend(row)
frequency = {}
for value in data:
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1
with open("histogram_data.txt", "w") as file:
    file.write("Значення\tЧастота\n")
    for value, count in sorted(frequency.items()):
        file.write(f"{value}\t{count}\n")
print("Гістограма частот збережена у файлі 'histogram_data.txt'")
