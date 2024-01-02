import matplotlib.pyplot as plt
import pandas as pd

def plot_trades(prices, buy_open, buy_close, sell_open, sell_close, buy_tp, buy_sl, sell_tp, sell_sl):

    plt.plot(prices, label='Preços de Bid', color='lime')
    plt.scatter(buy_open, [prices[i] for i in buy_open], marker='^', color='green', label='Open Buy')
    plt.scatter(buy_close, [prices[i] for i in buy_close], marker='v', color='red', label='Close Buy')

    plt.scatter(sell_open, [prices[i] for i in sell_open], marker='^',  label='Open Sell')
    plt.scatter(sell_close, [prices[i] for i in sell_close], marker='v', label='Close Sell')
    
    plt.scatter(buy_tp, [prices[i] for i in buy_tp], marker='>', label='TP Buy')
    plt.scatter(buy_sl, [prices[i] for i in buy_sl], marker='>', label='SL Buy')

    plt.scatter(sell_tp, [prices[i] for i in sell_tp], marker='>', label='TP Sell')
    plt.scatter(sell_sl, [prices[i] for i in sell_sl], marker='>', label='SL Sell')

    # Adiciona linhas tracejadas ligando pontos de entrada e saída
    for entry, exit in zip(buy_open, buy_close):
        plt.plot([entry, exit], [prices[entry], prices[exit]], linestyle='--', color='black')

    for entry, exit in zip(sell_open, sell_close):
        plt.plot([entry, exit], [prices[entry], prices[exit]], linestyle='--', color='black')

    plt.title('Entradas e Saídas de Trades')
    plt.xlabel('Tempo')
    plt.ylabel('Preços de Bid')
    plt.legend()
    plt.grid(True)
    plt.show()

def convert_values(all_values):
    extract = []
    for i in range(len(all_values)):
        val = all_values[i]
        if val != "None":
            extract.append(int(val))
    return extract

# Get Prices
data   = pd.read_csv("summary_market.csv")
prices = data["bid"]

# Close
data   = pd.read_csv("summary_close.csv")
buy_open_ia   = data["open_buy"]
sell_open_ia  = data["open_sell"]
buy_close_ia  = data["close_buy_ia"]
sell_close_ia = data["close_sell_ia"]

buy_open_ia_n   = convert_values(buy_open_ia)
sell_open_ia_n  = convert_values(sell_open_ia)
buy_close_ia_n  = convert_values(buy_close_ia)
sell_close_ia_n = convert_values(sell_close_ia)

# Buy TP SL
data   = pd.read_csv("summary_tp_sl.csv")
buy_tp = data["open_buy_cl_tp"]
buy_sl = data["open_buy_cl_sl"]

buy_tp_n = convert_values(buy_tp)
buy_sl_n = convert_values(buy_sl)

# Sell TP SL
sell_tp = data["open_sell_cl_tp"]
sell_sl = data["open_sell_cl_sl"]

sell_tp_n = convert_values(sell_tp)
sell_sl_n = convert_values(sell_sl)

plot_trades(prices, buy_open_ia_n, buy_close_ia_n, sell_open_ia_n, sell_close_ia_n, buy_tp_n, buy_sl_n, sell_tp_n, sell_sl_n)
