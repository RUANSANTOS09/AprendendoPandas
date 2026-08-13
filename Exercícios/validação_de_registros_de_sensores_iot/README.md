# 🌡️ Validação de Registros de Sensores IoT — NumPy

> "Threshold de anomalia não nasce de um número aleatório — nasce do domínio do problema."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Filtering%20%26%20Where-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Simular uma etapa de **data quality** de uma pipeline real: sensores de temperatura registram leituras que precisam ser validadas antes de seguir para a próxima camada de dados (staging/silver). O threshold de anomalia não foi arbitrário — foi baseado nos recordes históricos reais de temperatura da cidade de São Paulo.

---

## 📐 Contexto de negócio

- Sensores medindo temperatura na cidade de São Paulo, em diferentes estações do ano.
- Maior temperatura já registrada na história de SP: **37,8°C**.
- Menor temperatura já registrada na história de SP: **-2,1°C**.
- Qualquer leitura fora desse intervalo real é fisicamente inconsistente com o histórico da cidade e é tratada como suspeita.

---

## 🧱 Pipeline do projeto

```
┌─────────────────────────────────┐
│  temperatures_sensors (6x4)        │  linhas = leituras | colunas = sensores
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│  Passo 1 — Detecção de anomalia    │
│                                     │
│  suspeitas = temps[(temps >= 37.8) │
│                    | (temps <= -2.1)]
└───────────────┬─────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│  Passo 2 — Tratamento (np.where)    │
│                                     │
│  válida = (temps < 37.8) &         │
│           (temps > -2.1)           │
│  treated = np.where(válida,        │
│                temps, np.nan)      │
└───────────────┬─────────────────────┘
                │  mantém shape (6,4) — rastreabilidade preservada
                ▼
┌─────────────────────────────────┐
│  Passo 3 — Agregação confiável      │
│                                     │
│  média por sensor =                │
│    np.nanmean(treated, axis=0)     │
└─────────────────────────────────┘
```

---

## 🔧 Etapas realizadas

- [x] Montagem da matriz de leituras com valores plausíveis e valores propositalmente inválidos
- [x] Identificação de leituras suspeitas via boolean masking puro (relatório para investigação)
- [x] Tratamento das leituras inválidas com `np.where()`, marcando-as como `np.nan` **sem perder a estrutura original** da matriz — preservando a rastreabilidade de qual sensor e qual leitura gerou o dado ruim
- [x] Cálculo da temperatura média confiável por sensor com `np.nanmean()`, ignorando os valores marcados como inválidos

---

## 💡 Conceitos praticados

| Conceito | Aplicação |
|---|---|
| Boolean masking puro (`array[condição]`) | Relatório de leituras suspeitas (array achatado, para investigação) |
| `np.where(condição, valor_original, substituto)` | Marcação de dado inválido preservando o shape original da matriz |
| `np.nan` como marcador de dado inválido | Alternativa à remoção de linhas/colunas, mantendo rastreabilidade |
| `np.nanmean()` | Agregação que ignora `nan` automaticamente, sem cálculo manual de exclusão |
| `axis=0` | Média por sensor (coluna), atravessando as leituras (linhas) |

---

## ⚠️ Ajuste de threshold durante o desenvolvimento

A primeira versão usava `<= -2` como critério de suspeita. Como o menor valor já registrado na história de SP é `-2,1°C`, esse critério classificaria incorretamente uma leitura real e válida (`-2.0°C`) como anômala. Ajustado para `<= -2.1`, alinhando o código ao dado histórico real, não a um valor arredondado arbitrário.

---

## 🗂️ Estrutura

```
validacao_sensores_iot_numpy/
└── validacao_sensores_iot.py
```

---

## 🚀 Próximos passos

Fechar o último bloco do curso de fundamentos de NumPy: random numbers.