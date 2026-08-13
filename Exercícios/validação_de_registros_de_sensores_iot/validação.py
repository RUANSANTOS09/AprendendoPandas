import numpy as np


# Temperaturas dos sensores da cidade de São Paulo no verão (Dezembro até Março) e no inverno (Junho e Setembro)
# Maior tempreatura já registrada na cidade de São Paulo = 37,8°C
# Menor tempreatura já registrada na cidade de São Paulo = -2,1°C
# temperatura media de são paulo no verão = 21°C a 23°C
# temperatura media de são paulo no inverno = 15°C a 17°C
temperatures_sensors = np.array([[-30, 34, 20, 45],
                                 [-100, 450, 10, 20],
                                 [23, 22, 540, 120],
                                 [20, 25, 29, 12],
                                 [5, 9, -2.0, 20],
                                 [20, 999, 20, 10]])

# Passo 1. Identificar temperaturas suspeitas
suspicious_temperatures = temperatures_sensors[(temperatures_sensors >= 37.8) | (temperatures_sensors <= -2.1)]
print(suspicious_temperatures)

# Passo 2. Tratar essas leituras sem perder a estrutura original da matriz (rastreabilidade de qual sensor e qual leitura gerou o dado ruim).
treating_temperatures = (temperatures_sensors < 37.8) & (temperatures_sensors > -2.1)
treated_temperatures = np.where(treating_temperatures, temperatures_sensors, np.nan)
print(treated_temperatures)

# Passo 3. Calcular a temperatura média confiável de cada sensor, desconsiderando os dados inválidos.
media = np.nanmean(treated_temperatures, axis=0)
print(f'Media de cada sensor {media}')
