n = int(input('Введите размер рандомного списка целых чисел n '))

from random import randint
line = [randint(-10, 10) for i in range(n)]
line = sorted(line)
print('\nПолученный список:', line)

x = int(input('\nКакое целое число найти? '))

p = 0
r = n - 1
ind = -1
while p <= r:
	q = (p+r) // 2
    if line[q] == x:
		ind = q
		break
	elif line[q] > x:
		r = q - 1
	else:
		p = q + 1

if ind < 0:
	print('Не найдено')
else:
	print('Число %d найдено\nЭто %d-й эелемент списка' % (x, q+1))
