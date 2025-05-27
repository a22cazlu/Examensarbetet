import pandas as pd
import scipy.stats as stats

# Läser in datafilerna
df_high = pd.read_csv('highcharts_uppdatering_mattider_L.txt')
df_echart = pd.read_csv('echart_uppdatering_mattider_L.txt')

# Tar ut bara tid_ms kolumnen
highcharts = df_high['tid_ms']
echarts = df_echart['tid_ms']

# Kör one-way ANOVA
f_statistic, p_value = stats.f_oneway(highcharts, echarts)

# Skriver ut resultatet
print(f"F-statistik: {f_statistic:.2f}")
print(f"P-värde: {p_value:.4f}")

# Tolkning
if p_value < 0.05:
    print("Resultat: Statistiskt signifikant skillnad mellan grupperna (p < 0.05)")
else:
    print("Resultat: Ingen statistiskt signifikant skillnad mellan grupperna (p >= 0.05)")
