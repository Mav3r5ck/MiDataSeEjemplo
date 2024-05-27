import matplotlib.pyplot as plt
columna_de_interes = 'Uso de memoria (%)'
plt.hist(df[columna_de_interes], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Histograma de ' + columna_de_interes)
plt.show()
