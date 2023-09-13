def _main() -> None:
  cadena = input()
  fraseArreglo = cadena.split("lo que")
  print(" lo que ".join(input().split(" lo que ")[::-1]))
  pass