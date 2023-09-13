def _main() -> None:
  n = int(input())
  lista = []
  for i in range(n):
    i = int(input())
    lista.append(i)
  lista.sort(reverse = True)
  resultado = 0
  for j in range(n-1):
    resultado = resultado + lista[j]
  print(resultado)
  pass

if __name__ == '__main__':
  _main()