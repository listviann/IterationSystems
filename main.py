import sys
from sympy.abc import x, y
from sympy import cos, symbols, diff, sin


# вариант 9
# f(x,y) = y - x^2
# g(x,y) = x^2 + y^ 2 - 4

# вычисления частных производных
def f_dy(y_n, expression):
    x, y = symbols('x y')
    part_derivative_y = diff(expression, y).subs(y, y_n)
    return part_derivative_y


def g_dy(y_n, expression):
    x, y = symbols('x y')
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


# An
def a_n(f, g, fdy, gdy, x_n, y_n):
    a = f.subs(x, x_n).subs(y, y_n) * gdy - g.subs(x, x_n).subs(y, y_n) * fdy
    return a


# Bn
def b_n(f, g, fdx, gdx, x_n, y_n):
    b = fdx * g.subs(x, x_n).subs(y, y_n) - f.subs(x, x_n).subs(y, y_n) * gdx
    return b


# Jn
def j_n(fdy, gdy, fdx, gdx):
    j = (fdx * gdy) - (fdy * gdx)
    return j


# основные вычисления и формула
def main_formula(xn, yn, exx, exy):
    print(f"xn = {xn} \nyn = {yn}")
    fdy = f_dy(yn, exy)
    fdx = f_dx(xn, exy)
    gdy = g_dy(yn, exx)
    gdx = g_dx(xn, exx)

    an = a_n(exy, exy, fdy, gdy, xn, yn)
    bn = b_n(exy, exx, fdx, gdx, xn, yn)
    jn = j_n(fdy, gdy, fdx, gdx)

    if (jn == 0):
        sys.exit(1)

    # точность
    e = 0.0005

    # использование основной формулы для расчета
    xn1 = xn - (an / jn)
    yn1 = yn - (bn / jn)

    if (abs(xn1 - xn) <= e) and (abs(yn1 - yn) <= e):
        return [xn1, yn1]

    print(f"xn+1 = {xn1}\nyn+1 = {yn1}\n")
    return main_formula(xn1, yn1, exx, exy)


# x = 0.9561, y = 0.08791
# начальное приближение
x0 = 0.9526
y0 = 0.0791

# выражения в системе
# f(x,y)
expression_y = cos(y - 1) + y - 0.7
# g(x,y)
expression_x = sin(y) + 2 * x -2

# вызовы всех функций
result = main_formula(x0, y0, expression_x, expression_y)

print(f"результат: {result}")
