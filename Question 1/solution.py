from operator import add
print reduce(add,[x for x in range(1,1000) if (x % 3 == 0 or x % 5 == 0)])
