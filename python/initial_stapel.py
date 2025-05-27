import matplotlib.pyplot as plt
import pandas as pd

# Läs in båda filerna
df_high = pd.read_csv("highcharts_initial_mattider_L.txt")
df_echart = pd.read_csv("echart_initial_mattider_L.txt")

# Extrahera endast tider
tider_high = df_high['tid_ms']
tider_echart = df_echart['tid_ms']

# Räkna ut medelvärde och standardavvikelse
mean_high = tider_high.mean()
std_high = tider_high.std()

mean_echart = tider_echart.mean()
std_echart = tider_echart.std()

# Skapa data för staplarna
medelvärden = [mean_high, mean_echart]
standardavvikelser = [std_high, std_echart]
kategorier = ['Highcharts', 'ECharts']

# Skapa figuren och axeln
fig, ax = plt.subplots(figsize=(8, 6))

# Rita stapeldiagrammet
ax.bar(kategorier, medelvärden, yerr=standardavvikelser, capsize=10, color=['yellowgreen', 'steelblue'], edgecolor='black')

# Lägg till etiketter och titel
ax.set_ylabel('Tid (ms)')
ax.set_title('Initial renderingstid: Highcharts vs ECharts stort dataset\nMedelvärde med standardavvikelse')

# Visa grid för bättre läsbarhet
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
