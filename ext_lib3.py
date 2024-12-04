import requests
import numpy as np
import matplotlib.pyplot as plt

# Импорт произвольного изображения
response = requests.get('https://media.proglib.io/wp-uploads/2018/09/maxresdefault-1.jpg')

with open('1_image.jpg', 'wb') as file:
    file.write(response.content)

# Операции с массивами чисел
a = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
print(a>20)

# Графики синуса и косинуса
phi = np.linspace(0, 2. * np.pi, 100)
plt.plot(phi, np.sin(phi), label='sin(φ)')
plt.plot(phi, np.cos(phi), label='cos(φ)')
plt.legend()

plt.title('Графики синуса и косинуса')
plt.xlabel('φ (рад)')
plt.ylabel('Значение')

plt.show()