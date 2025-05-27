import matplotlib.pyplot as plt
import pandas as pd
import os

# Dataset-etiketter och resultatlistor
datasets = ['S', 'M', 'L']
dataset_labels = ['Liten', 'Mellan', 'Stor']
echarts_means = []
highcharts_means = []

# Läs in mätdata och beräkna medelvärden
for size in datasets:
    try:
        echart_path = f"echart_initial_mattider_{size}.txt"
        highchart_path = f"highcharts_initial_mattider_{size}.txt"

        if not os.path.isfile(echart_path) or not os.path.isfile(highchart_path):
            print(f"Saknar fil för {size}: '{echart_path}' eller '{highchart_path}'")
            echarts_means.append(None)
            highcharts_means.append(None)
            continue

        df_e = pd.read_csv(echart_path)
        df_h = pd.read_csv(highchart_path)

        mean_e = df_e['tid_ms'].mean()
        mean_h = df_h['tid_ms'].mean()

        echarts_means.append(mean_e)
        highcharts_means.append(mean_h)

        print(f"{size} datamängd – ECharts: {mean_e:.2f} ms, Highcharts: {mean_h:.2f} ms")

    except Exception as e:
        print(f"Fel vid inläsning av {size}: {e}")
        echarts_means.append(None)
        highcharts_means.append(None)

# Kontrollera om någon data saknas
if None in echarts_means or None in highcharts_means:
    print("Kunde inte skapa diagram – saknar fullständiga data.")
else:
    # Plotta linjediagram
    plt.figure(figsize=(10, 5))
    plt.plot(dataset_labels, highcharts_means, marker='o', label='Highcharts', color='yellowgreen')
    plt.plot(dataset_labels, echarts_means, marker='o', label='ECharts', color='steelblue')

    # Lägg till etiketter på varje punkt
    for i in range(len(dataset_labels)):
        plt.text(i, highcharts_means[i] + 0.3, f'{highcharts_means[i]:.1f} ms', ha='center', color='yellowgreen')
        plt.text(i, echarts_means[i] + 0.3, f'{echarts_means[i]:.1f} ms', ha='center', color='steelblue')

    # Diagraminställningar
    plt.title('Genomsnittlig initial renderingstid\nECharts vs Highcharts')
    plt.xlabel('Datamängd')
    plt.ylabel('Tid (ms)')
    plt.ylim(0, 25)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
