import math

def main():
    lim = 100

    # 문1: 최대 공약수를 구하는 세 가지 알고리즘을 구현하여라.
    for i  in range(1, lim + 1):
        for j in range(1, lim + 1):
            result_1 = gcd_1(i, j) == math.gcd(i, j)
            result_2 = gcd_2(i, j) == math.gcd(i, j)
            result_3 = gcd_3(i, j) == math.gcd(i, j)

            if result_1 == False or result_2 == False or result_3 == False:
                print(f'계산된 최대 공약수가 다릅니다. ({i}, {j}: {result_1}, {result_2}, {result_3}')
                return
            
            # print(f'{i}, {j}:')
            # print(f'\t{result_1}')
            # print(f'\t{result_2}')
            # print(f'\t{result_2}')

    # 문2: 최소 공배수를 구하는 알고리즘을 구현하여라.
    for i  in range(1, lim + 1):
        for j in range(1, lim + 1):
            result = lcm(i, j) == math.lcm(i, j)

            if result == False:
                print(f'계산된 최소 공배수가 다릅니다. ({i}, {j}: {result})')
                return
            
            # print(f'{i}, {j}:')
            # print(f'\t{result}')

    print(f'완료: 범위({lim})')

# 문1: 최대 공약수를 구하는 세 가지 알고리즘을 구현하여라.
def gcd_1(a, b):
    alist = []
    blist = []

    for i in range(1, a + 1):
        if a % i == 0:
            alist.append(i)

    for i in range(1, b + 1):
        if b % i == 0:
            blist.append(i)

    for i in reversed(alist):
        if i in blist:
            return i

def gcd_2(a, b):
    alist = []

    for i in range(1, a + 1):
        if a % i == 0:
            alist.append(i)

    for i in reversed(alist):
        if b % i == 0:
            return i

def gcd_3(a, b):
    i = a if a > b else b
    j = a if a < b else b

    return gcd_3_rec(i, j)

def gcd_3_rec(a, b):
    if b == 0:
        return a
    return gcd_3_rec(b, a % b)

# 문2: 최소 공배수를 구하는 알고리즘을 구현하여라.
def lcm(a, b):
    gcd_ = gcd_3(a, b)
    i = a / gcd_
    j = b / gcd_

    return gcd_ * i * j

if __name__ == '__main__':
    main()