import numpy
import datetime
import plotly.offline as py
import plotly.graph_objs as go 
import pandas_datareader as web

start = datetime.datetime (2014,1,1)
end =datetime.datetime(2020,9,23)

FB = web.DataReader('FB','yahoo',start,end)
TW = web.DataReader('TWTR','yahoo',start,end)
AAPL = web.DataReader('AAPL','yahoo',start,end)

print(FB)



trace = go.Ohlc(
    x=FB.index[:],
    open=FB['Open'],
    high=FB['High'],
    low=FB['Low'],
    close=FB['Close'],
    name='FB',
    increasing=dict(line=dict(color='green')),
    decreasing=dict(line=dict(color='red')),
)

trace2 = go.Ohlc(
    x=TW.index[:],
    open=TW['Open'],
    high=TW['High'],
    low=TW['Low'],
    close=TW['Close'],
    name='TW',
    increasing=dict(line=dict(color='purple')),
    decreasing=dict(line=dict(color='black')),
)

trace3 = go.Ohlc(
    x=AAPL.index[:],
    open=AAPL['Open'],
    high=AAPL['High'],
    low=AAPL['Low'],
    close=AAPL['Close'],
    name='AAPL',
    increasing=dict(line=dict(color='yellow')),
    decreasing=dict(line=dict(color='red')),
)

data = [trace, trace2, trace3]
layout= {
    'title': 'Facebook vs Twitter vs Apple',
    'yaxis': {'title':'Price per stock'}
}

fig = dict(data=data, layout=layout)
py.plot(fig, filename='techsticjs.html')





def hello():
    print('hello mate')


hello()
