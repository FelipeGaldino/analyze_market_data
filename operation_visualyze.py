import matplotlib.pyplot as plt
import pandas as pd

def plot_trades(prices, entry_points, exit_points):

    plt.plot(prices, label='Preços de Bid', color='blue')
    print(entry_points)
    plt.scatter(entry_points, [prices[i] for i in entry_points], marker='^', color='green', label='Entrada')
    plt.scatter(exit_points, [prices[i] for i in exit_points], marker='v', color='red', label='Saída')

    # Adiciona linhas tracejadas ligando pontos de entrada e saída
    for entry, exit in zip(entry_points, exit_points):
        plt.plot([entry, exit], [prices[entry], prices[exit]], linestyle='--', color='black')

    plt.title('Entradas e Saídas de Trades')
    plt.xlabel('Tempo')
    plt.ylabel('Preços de Bid')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso
#prices = [100, 105, 95, 110, 102, 108, 97, 112, 98, 105, 91, 104]

folder_csv = "~/Work/DATA_CSV/realtime_data/candles_real_time/"
data = pd.read_csv(f"{folder_csv}pips_30/1_realtime_candles_EURUSD_30.csv")
prices = data["bid"]

# index entry exit points
entry_points = [1, 3,  6,  8, 10, 16, 22, 32, 42, 52, 100, 150]
exit_points  = [4, 8, 10, 25, 50, 65, 65, 65, 65, 65, 200, 250]

# TEst LOOP
result = [prices[i] for i in entry_points]

res = []
for i in range(len(entry_points)):
    entry = entry_points[i]
    res.append(prices[entry])
print("Original : ",result)
print("Next     ; ",res)

plot_trades(prices, entry_points, exit_points)
