import matplotlib.pyplot as plt


disease = ['Dental Care', 'Hypertension', 'HighCholesterol', 'Overweight', 'Arthritis', 'GenericProblem', 'SinusInfection']
performance_rf = [0.49, 0.49, 0.49, 0.53, 0.58, 0.64, 0.65]
performance_rf_no_age_gender = [0.5, 0.49, 0.5, 0.54, 0.59, 0.63, 0.64]
performance_rf_no_law_protected_vars = [0.5, 0.5, 0.49, 0.53, 0.59, 0.63, 0.65]


plt.plot(disease, performance_rf, marker='o', markersize=10, color='deepskyblue', linewidth=2, label='RF All Variables')
plt.plot(disease, performance_rf_no_age_gender, marker='^', color='darkviolet', markersize=10, linewidth=2, label='RF No Age and Gender')
plt.plot(disease, performance_rf_no_law_protected_vars, marker='v', color='salmon', markersize=10, linewidth=2, label='RF No Law Protected Variables')
plt.xlabel('Disease')
plt.ylabel('F1 score')
plt.title('Most common diseases separate classifier performance with RF')
plt.legend(fancybox=True)
plt.show()


performance_knn = [0.50, 0.49, 0.5, 0.54, 0.59, 0.64, 0.67]
performance_knn_no_age_gender = [0.5, 0.49, 0.5, 0.54, 0.59, 0.64, 0.67]
performance_knn_no_law_protected_vars = [0.5, 0.49, 0.5, 0.54, 0.59, 0.64, 0.67]

plt.plot(disease, performance_knn, marker='o', markersize=10, color='deepskyblue', linewidth=2, label='KNN All Variables')
plt.plot(disease, performance_knn_no_age_gender, marker='^', color='darkviolet', markersize=10, linewidth=2, label='KNN No Age and Gender')
plt.plot(disease, performance_knn_no_law_protected_vars, marker='v', color='salmon', markersize=10, linewidth=2, label='KNN No Law Protected Variables')
plt.xlabel('Disease')
plt.ylabel('F1 score')
plt.title('Most common diseases separate classifier performance with KNN')
plt.legend(fancybox=True)
plt.show()


disease = ['Dental Care', 'Hypertension', 'HighCholesterol', 'Overweight', 'Arthritis', 'GenericProblem', 'SinusInfection']
performance_rf = [0.49, 0.49, 0.49, 0.53, 0.58, 0.64, 0.65]
performance_rf_no_age_corr_vars = [0.52, 0.49, 0.51, 0.51, 0.58, 0.63, 0.65]

plt.plot(disease, performance_rf, marker='o', markersize=10, color='deepskyblue', linewidth=2, label='RF All Variables')
plt.plot(disease, performance_rf_no_age_corr_vars, marker='^', color='darkviolet', markersize=10, linewidth=2, label='RF No Age and Age\'s Correlated Variables ')
plt.xlabel('Disease')
plt.ylabel('F1 score')
plt.title('Most common diseases separate classifier performance with RF')
plt.legend(fancybox=True)
plt.show()