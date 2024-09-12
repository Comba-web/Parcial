def verificar_multiplos(num1, num2):

  if num2 == 0 or num1 == 0:
      return "No es divisor de cero."

  if num1 % num2 == 0:
      return f"{num1} es múltiplo de {num2}"

  elif num2 % num1 == 0:
      return f"{num2} es múltiplo de {num1}"

  else:
      return "No son múltiplo ninguno del otro."

try:
  num1 = int(input("Escribe  el primer número: "))

  num2 = int(input("Escribe el segundo número: "))
  resultado = verificar_multiplos(num1, num2)
  
  print(resultado)

except ValueError:
  print("Por favor, escribe los números enteros válidos.")