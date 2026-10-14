n1, n2, n3 = map(int,input().split())

array = []

array.append(n1)
array.append(n2)
array.append(n3)
array.sort()

print(f'{array[1]} O segundo maior valor')