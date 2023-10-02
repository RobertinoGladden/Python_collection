import random
MIN = 1
MAX = 6
num = int(input('number of rolling : '))
total = 0
accum = {}

for i in range(1, num + 1):
    print('Rolling the dices...')
    print('The values are...')
    dice1 = random.randint(MIN,MAX)
    print('dice1 = ', dice1)
    dice2 = random.randint(MIN,MAX)
    print('dice2 = ', dice2)
    total = dice1 + dice2

    print('Accumulation value =', total)
    
    if total in accum:
        accum[total] += 1
    else:
        accum[total] = 1

print('Accumulation counts:')
for accValue, count in accum.items():
    print(f'{accValue}: {count} times')

hiAccum = max(accum.keys())
lowAccum = min(accum.keys())

print('Highest accumulation value:', hiAccum)
print('Lowest accumulation value:', lowAccum)