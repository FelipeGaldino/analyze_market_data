import pandas as pd
from decimal import Decimal

folder_csv = "~/Work/DATA_CSV/realtime_data/candles_real_time/"

data = pd.read_csv(f"{folder_csv}pips_30/3_realtime_candles_EURUSD_30.csv")

qnt_buy  = 0
qnt_sell = 0

seq_buy  = 0
sv_seq_b = []

seq_sell  = 0
sv_seq_s = []


for i in range(len(data)-1):
    buy_ask_open  = round(Decimal(data.iloc[i]['ask'] * 1000),2)   # CURRENT OPEN
    buy_bid_close = round(Decimal(data.iloc[i+1]['bid'] * 1000),2) # NEXT
    
    sell_bid_open = round(Decimal(data.iloc[i]['bid'] * 1000),2) # CURRENT OPEN
    sell_ask_close = round(Decimal(data.iloc[i+1]['ask'] * 1000),2) # NEXT
    
    # 
    buy_pl  = buy_bid_close - buy_ask_open
    sell_pl = sell_bid_open - sell_ask_close
    
    if buy_pl > 0:
        qnt_buy+=1
        seq_buy+=1
        seq_sell=0

    if sell_pl > 0:
        qnt_sell+=1
        seq_sell+=1
        seq_buy=0
    sv_seq_b.append(seq_buy)
    sv_seq_s.append(seq_sell)
print("TOTAL ",len(data))
print(f"BUY {qnt_buy} Max {max(sv_seq_b)}")
print(f"SELL {qnt_sell} Max {max(sv_seq_s)}")
