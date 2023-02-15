from math import pi, sqrt


def get_square_circle(radius: float) -> float:
    return pi * radius**2


for r in range(1, 11):
    s = get_square_circle(r)
    print(f'Radius = {r}, square = {s:.2f}')


def get_square_equation_roots(a: float, b: float, c: float)-> tuple[float]:
    d = b**2 - 4 * a * c
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)

    return (x1, x2)


