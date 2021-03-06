from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja ver: '))
a = radians(angulo)
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sin(a)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos(a)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tan(a)))

