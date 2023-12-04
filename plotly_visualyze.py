import pandas as pd 

import os 
import plotly.graph_objects as go
import os

def plot_chart(chart_equity,sma,cl,name_chart):
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=chart_equity, mode='lines', name=name_chart))
    fig.add_trace(go.Scatter(y=sma, mode='lines', name=name_chart))
    fig.add_trace(go.Scatter(y=cl, mode='lines', name=name_chart, line={'dash': 'dash', 'color': 'green'}))
    fig.update_layout(
        #title=f"Backtest : Only IA | Period {chart_datetime[0]} a {chart_datetime[-1]}",
        xaxis_title="Data",
        yaxis_title="Investment",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )

    )


    fig.show()
    
folder_csv = "~/Work/DATA_CSV/realtime_data/candles_real_time/"
data = pd.read_csv(f"{folder_csv}pips_30/1_realtime_candles_EURUSD_30.csv")
all_bid = data["bid"]
sma = data['bid'].rolling(8).mean()
sma12 = data['bid'].rolling(12).mean()


cl = []

t = 8
if t % 4 == 0:
    print("Divisivel")
for i in range(len(all_bid)):
    if i % 4 == 0:
        cl.append(sma12[i])
    else:
        cl.append(None)

print(cl)
    

plot_chart(all_bid,sma,cl,"RSI")

