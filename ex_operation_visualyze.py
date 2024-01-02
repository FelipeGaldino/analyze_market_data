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
# prices       = [100, 105, 95, 110, 102, 108, 97, 112, 98, 105, 91, 104]
# entry_points = [1,   3,  6,  8, 10, 16, 22, 32, 42]
# exit_points  = [90,  3, 90,  8, 90, 90, 22, 90, 90]

data   = pd.read_csv("summary_market.csv")
prices = data["bid"]

# index entry exit points
entry_points = [1,   3,  6,  8, 10, 16, 22, 32, 42]
exit_points  = [90,  3, 90,  8, 90, 90, 22, 90, 90]

plot_trades(prices, entry_points, exit_points)
