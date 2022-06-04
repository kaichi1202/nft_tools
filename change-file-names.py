import os

count = int(input('Your file count: '))
digit = int(input('Digit: '))

for i in reversed(range(count)):
  print(str(i) + ' to ' + str(i + 1))
  os.rename('./images/' + str(i).zfill(digit) + '.png', './images/' + str(i + 1).zfill(digit) + '.png')
  os.rename('./json/' + str(i), './json/' + str(i + 1))

print('Done!')
