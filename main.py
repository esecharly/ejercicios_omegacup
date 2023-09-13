def _main() -> None:
  n = int(input())
  m = input().split(" ")
  p = int(input())

  pares = []
  impares = []
  if p == 0:
    for i in m:
      if i % 2 == 0:
        pares.append(i)
        print("".join(pares))

  if p == 1:
    for i in m:
      if i % 2 == 0:
        pares.append(i)
        print("".join(impares))
  pass

_main()