import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
  "Temperatura": np.random.randint(15, 30, size=30),
  "Umidade": np.random.randint(40, 80, size=30),
})

correlacao = df["Temperatura"].corr(df["Umidade"])
print(f"Correlação entre Temperatura e Umidade: {correlacao:.2f}")

plt.figure(figsize=(8, 6))
sns.regplot( x = "Temperatura", y = "Umidade", data = df, color = 'pink', scatter_kws = {"s": 100}, line_kws = {"color": "yellow"})
plt.title("Gráfico de Disperção: Temperatura vs Umidade")
plt.xlabel("Temperatura ('c)")
plt.ylabel("Umidade (%)")
plt.grid(True)
plt.show()
