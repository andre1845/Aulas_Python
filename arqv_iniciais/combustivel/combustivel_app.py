gasolina = float(input ("Gasolina ?"))
etanol = float(input ("Etanol ?"))
etanol_comparado = ((0.7) * gasolina)
print("Abasteça com:")
print("etanol") if(etanol < etanol_comparado) else print("gasolina")
valor_relativo = (etanol *100)/gasolina
print (f"O etanol está custando {valor_relativo:.2f}% da gasolina")