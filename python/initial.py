import matplotlib.pyplot as plt
import pandas as pd

# Läs in båda filerna
df_high = pd.read_csv("highcharts_initial_mattider_S.txt")
df_echart = pd.read_csv("echart_initial_mattider_S.txt")

# Extrahera endast tider
tider_high = df_high['tid_ms']
tider_echart = df_echart['tid_ms']

# Skapa X-axel
x_high = range(1, len(tider_high) + 1)
x_echart = range(1, len(tider_echart) + 1)

# Plotta linjediagram
plt.figure(figsize=(12, 5))
plt.plot(x_high, tider_high, linestyle='-', label='Highcharts', color='yellowgreen')
plt.plot(x_echart, tider_echart, linestyle='-', label='ECharts', color='steelblue')

# Lägg till medelvärdeslinjer
plt.axhline(tider_high.mean(), color='yellowgreen', linestyle='--', label=f'Highcharts Medel: {tider_high.mean():.1f} ms')
plt.axhline(tider_echart.mean(), color='steelblue', linestyle='--', label=f'ECharts Medel: {tider_echart.mean():.1f} ms')

# Inställningar
plt.title("Initial renderingstid: Highcharts vs ECharts litet dataset (2000 mätningar)")
plt.xlabel("Mätning")
plt.ylabel("Tid (ms)")
plt.grid(True)

# Y-axeln:
plt.ylim(0, 40)

# Legenden snyggt
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()
