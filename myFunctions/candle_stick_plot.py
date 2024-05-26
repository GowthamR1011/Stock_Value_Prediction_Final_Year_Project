import plotly.graph_objects as go

def plotCandleStick(df,title):
    fig = go.Figure(data=(go.Candlestick(x=df['Date'],open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'])))
    fig.update_layout(title = title)
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_xaxes(title_text = "Date")
    fig.update_yaxes(title_text="Amount in Rupees")
    fig.show()