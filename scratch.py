import sys

N, M = map(int, sys.stdin.readline().split())
pokemon = [0]
pokemon_dict = dict()

for i in range(N):
  pokemon.append(sys.stdin.readline().strip())
  pokemon_dict[pokemon[-1]] = i + 1

for _ in range(M):
  q = sys.stdin.readline().strip()
  try:
    num_q = int(q)
    print(pokemon[num_q])
  except:
    print(pokemon_dict[q])