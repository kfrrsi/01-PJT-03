import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for _ in range(1, T+1):
    a = input()
    mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

    for k in mirror:
        a.replace
