
def prediction_plot(y_test, test_predict):
      len_prediction=[x for x in range(len(y_test))]
      plt.figure(figsize=(8,4))
      plt.plot(len_prediction, y_test, marker='.', label="actual")
      plt.plot(len_prediction, test_predict, 'r', label="prediction")
      plt.tight_layout()
      plt.subplots_adjust(left=0.07)
      plt.ylabel('Stock Value', size=15)
      plt.xlabel('Prediction number', size=15)
      plt.legend(fontsize=15)
      plt.show()