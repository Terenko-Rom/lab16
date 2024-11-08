import math
x_start = -2
x_end = 8
step = 0.1
with open("graph_data.txt", "w") as file:
    file.write("x\ty\n")
    x = x_start
    while x <= x_end:
        y = math.cos(x) + 6 * x
        file.write(f"{x:.2f}\t{y:.2f}\n")
        x += step
print("Дані для графіка збережені у файлі 'graph_data.txt'")