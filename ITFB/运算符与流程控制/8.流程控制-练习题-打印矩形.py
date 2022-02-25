# 格列换色
num = 1
while num <= 100:

    if num //10 % 2 == 0:
        print('★', end=" ")
    else:
        print('✰', end=" ")

    if num % 10 == 0:
        print('')

    num += 1
# 隔行换色
