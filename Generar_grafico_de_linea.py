import matplotlib.pyplot as plt
x = 'Marca de tiempo'
y = 'Uso de memoria (%)'
plt.plot(df[x], df[y], label='Serie 1')
plt.xlabel('Tiempo')
plt.ylabel('Y')
plt.title('Grafico de Dispercion')
plt.show()
