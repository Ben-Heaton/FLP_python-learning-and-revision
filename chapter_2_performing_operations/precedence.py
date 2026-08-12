a = 2
b = 4
c = 8

# Force addition before multiplication
print('\nDefault Order:\t', a, '*', c, '+', b, '=', a * c + b)
print('Forced Order:\t', a, '* (', c, '+', b, ') =', a * (c + b))

# Force subtraction before division
print('\nDefault Order:\t', c, '//', b, '-', a, '=', c // b - a)
print('Forced Order:\t', c, '// (', b, '-', a, ') =', c // (b - a))

# Force addition before modulo
print('\nDefault Order:\t', c, '%', a, '+', b, '=', c % a + b)
print('Forced Order:\t', c, '% (', a, '+', b, ') =', c % (a + b))

# Force addition before exponent operation
print('\nDefault Order:\t', c, '**', a, '+', b, '=', c ** a + b)
print('Forced Order:\t', c, '** (', a, '+', b, ') =', c ** (a + b))