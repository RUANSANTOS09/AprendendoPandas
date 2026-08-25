import pandas as pd
import numpy as np

array = np.array([33.8, -3, 45.2, 30, 21, 10.4])
fahrenheit_conversion = (array * 9/5) + 32

extraindo = fahrenheit_conversion[0:3]

filtro = fahrenheit_conversion[fahrenheit_conversion > 90]
print(f'Temperaturas amiores que 90: {filtro}')