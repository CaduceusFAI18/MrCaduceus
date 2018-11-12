import matplotlib.pyplot as plt


model = ['OneVsRest(RBF)', 'Random Forest(max_depth = 100)', 'KNN(neighbor = 5)', 'Neural Network']
performance = [0.02, 0.21, 0.20, 0.54]
error = [0.09, 0.03, 0.03, 0.05]


model_most_common = ['Random Forest(max_depth = 50)', 'KNN(neighbor = 5)', 'Neural Network']
performance_most_common = [0.30, 0.29, 0.57]
error_most_common = [0.03, 0.06, 0.05]

plt.rcParams.update({'font.size': 16})
plt.xlabel('Model')
plt.ylabel('F1 score')
plt.errorbar(model, performance, error, linestyle='None', marker='^')
plt.title('Models\' performance')
plt.plot()
plt.show()



plt.xlabel('Model')
plt.ylabel('F1 score')
plt.errorbar(model_most_common, performance_most_common, error_most_common, linestyle='None', marker='^')
plt.title('Models\' performance for most common disease')
plt.plot()
plt.show()