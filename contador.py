import time

resultado = 0
for i in range(1, 11):
    resultado += i
    print(f"Suma hasta {i}: {resultado}")

print("en ejecucion")
time.sleep(10)
