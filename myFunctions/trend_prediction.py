import matplotlib.pyplot as plt
def predicted_plot(df,lookback,prediction_input,predicted_value,prediction_date,title):
    plt.plot(df['Date'][-1*lookback:],prediction_input)
    plt.plot(prediction_date,predicted_value,marker="*")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Stock Value (in Rupees)")
    plt.show()