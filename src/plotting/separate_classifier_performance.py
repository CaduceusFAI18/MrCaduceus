import matplotlib.pyplot as plt


disease = ['Dental Care', 'Hypertension', 'HighCholesterol', 'Overweight', 'Arthritis', 'GenericProblem', 'SinusInfection']
performance_knn = [0.50, 0.49, 0.5, 0.54, 0.59, 0.64, 0.67]
performance_rf = [0.5, 0.52, 0.51, 0.52, 0.59, 0.63, 0.65]

performance_rf_tree_based_fs = [0.49, 0.49, 0.51, 0.57, 0.65, 0.70, 0.71]
performance_rf_lsvc_fs = [0.52, 0.51, 0.50, 0.59, 0.65, 0.70, 0.71]


plt.plot( disease, performance_knn, marker='o', markerfacecolor='blue', markersize=10, color='cyan', linewidth=4, label='KNN')
plt.plot( disease, performance_rf, marker='^', color='darkviolet', markersize=10, linewidth=2, label='Random Forest')
plt.xlabel('Diease')
plt.ylabel('F1 score')
plt.title('Most common dieases separate classifer performance')
plt.legend(fancybox=True)
plt.show()


plt.plot( disease, performance_rf, marker='o', markerfacecolor='blue', markersize=10, color='cyan', linewidth=4, label='RF')
plt.plot( disease, performance_rf_tree_based_fs, marker='^', color='darkviolet', markersize=10, linewidth=2, label='RF with Tree-based feature selection')
plt.plot( disease, performance_rf_lsvc_fs, marker='^', color='salmon', markersize=10, linewidth=2, label='RF with linear SVC')
plt.xlabel('Diease')
plt.ylabel('F1 score')
plt.title('Most common dieases separate classifer performance')
plt.legend(fancybox=True)
plt.show()

# plt.plot(performance_rf, marker='o', )

# model_most_common = ['Random Forest(max_depth = 50)', 'KNN(neighbor = 5)', 'Neural Network']
# performance_most_common = [0.30, 0.29, 0.57]
# error_most_common = [0.03, 0.06, 0.05]

# plt.rcParams.update({'font.size': 16})
# plt.xlabel('Model')
# plt.ylabel('F1 score')
# plt.errorbar(model, performance, error, linestyle='None', marker='^')
# plt.title('Models\' performance')
# plt.plot()
# plt.show()



# plt.xlabel('Model')
# plt.ylabel('F1 score')
# plt.errorbar(model_most_common, performance_most_common, error_most_common, linestyle='None', marker='^')
# plt.title('Models\' performance for most common disease')
# plt.plot()
# plt.show()