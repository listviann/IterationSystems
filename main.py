import sys
from sympy.abc import x, y
from sympy import cos, symbols, diff, sin


# вариант 9
# f(x,y) = cos(y-1) + y = 0.7
# g(x,y) = siny + 2x = 2


def f_dy(y_n, expression):
    x, y = symbols('x y')
    part_derivative_y = diff(expression, y).subs(y, y_n)
    return part_derivative_y


def g_dy(y_n, expression):
    x, y = symbols('x, y')
    part_derivative_y = diff(expression, y).subs(y, y_n)
    return part_derivative_y


def f_dx(x_n, expression):
    x, y = symbols('x y')
    part_derivative_x = diff(expression, x).subs(x, x_n)
    return part_derivative_x


def g_dx(x_n, expression):
    x, y = symbols('x y')
    part_derivative_x = diff(expression, x).subs(x, x_n)
    return part_derivative_x


def a_n(f, g, fdy, gdy, x_n, y_n):
    a = f.subs(x, x_n).subs(y, y_n) * gdy - g.subs(x, x_n).subs(y, y_n) * fdy
    return a


def b_n(f, g, fdx, gdx, x_n, y_n):
    b = fdx * g.subs(x, x_n).subs(y, y_n) - f.subs(x, x_n).subs(y, y_n) * gdx
    return b


def j_n(fdy, gdy, fdx, gdx):
    j = fdx * gdy - fdy * gdx
    return j


def main_formula(xn, yn, a__n, b__n, j__n):
    if j__n == 0:
        sys.exit(1)

    print(f"xn = {xn} \nyn = {yn}")
    e = 0.005

    xn1 = xn - (a__n / j__n)
    yn1 = yn - (b__n / j__n)

    print(f"xn+1 = {xn1}\nyn+1={yn1}\n")
    if (abs(xn1 - xn) <= e) and (abs(yn1 - yn) <= e):
        return [xn1, yn1]
    return main_formula(xn1, yn1, a__n, b__n, j__n)


x0 = 1
y0 = 0.1

expression_y = cos(y - 1) + y - 0.7
expression_x = sin(y) + 2 * x - 2

derivative_f_y = f_dy(y0, expression_y)
derivative_g_y = g_dy(y0, expression_x)
derivative_f_x = f_dx(x0, expression_y)
derivative_g_x = g_dx(x0, expression_x)

an = a_n(expression_y, expression_x, derivative_f_y, derivative_g_y, x0, y0)
bn = b_n(expression_y, expression_x, derivative_f_x, derivative_g_x, x0, y0)
jn = j_n(derivative_f_y, derivative_g_y, derivative_f_x, derivative_g_x)
result = main_formula(x0, y0, an, bn, jn)

print(f"результат: {result}")
