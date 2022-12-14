import math

d1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды (ярды)"))
d2 = float(input("Введите кратчайшее расстояние от утопающего до берега (футы)"))
h = float(input("Введите боковое смещение между спасателем и утопающим (ярды)"))
v_sand = float(input("Введите скорость движения спасателя по песку (мили в час)"))
n = float(input("Введите коэффициент замедления спасателя при движении в воде"))
theta1 = float(input("Введите направление движения спасателя по песку (градусы)"))

d1 = d1 * 3
h = h * 3
v_sand = v_sand * 5280 / 3600
theta1 = theta1 * math.pi / 180

L1 = d1 / math.cos(theta1)
x = L1 * math.sin(theta1)
L2 = math.sqrt((h - x) ** 2 + d2 ** 2)
t = L1 / v_sand + L2 / (v_sand / n)

print("Cпасатель достигнет утопающего через: " + str(round(t, 1)) + " cекунд.")
