import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

end_data = datetime.now().strftime('%Y-%m-%d')

bb = yf.Ticker('BBAS3.SA')
data_bb = bb.history(
    start='2020-01-01',
    end=end_data
)

data_bb['Close'].plot()
plt.savefig('bb.png')
