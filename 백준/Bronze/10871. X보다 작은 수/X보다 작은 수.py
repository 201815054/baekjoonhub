import sys 
N,X = map(int,sys.stdin.readline().rstrip().split())
A = list(map(int,sys.stdin.readline().rstrip().split()))
result = [str(x) for x in A if x<X]
print(" ".join(result))