import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

ratios = [0.374, 0.488, 0.441, 0.482, 0.451, 0.395, 0.329]
ratios_freq = pd.Series.from_array(ratios)

diseases = ['Arthritis', 'Dental Care', 'GenericProblem', 'HighCholesterol', 'Hypertension', 'Overweight', 'SinusInfection']

n_groups = 7

# means_men = (20, 35, 30, 35, 27)
ratios = [0.374, 0.488, 0.441, 0.482, 0.451, 0.395, 0.329]
ratios_classifier = [0.474, 0.448, 0.442, 0.447, 0.464, 0.465, 0.427]
# std_men = (2, 3, 4, 1, 2)
#
# means_women = (25, 32, 34, 20, 25)
# std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, ratios, bar_width,
                alpha=opacity, color='deepskyblue',
                error_kw=error_config,
                label='Original Data')

rects2 = ax.bar(index + bar_width, ratios_classifier, bar_width,
                alpha=opacity, color='darkviolet',
                error_kw=error_config,
                label='Random Forest Classifier Result')

ax.set_xlabel('Diseases')
ax.set_ylabel('Male Ratio')
ax.set_title('Ratio of men having the diseases')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Arthritis', 'Dental Care', 'GenericProblem', 'HighCholesterol', 'Hypertension', 'Overweight', 'SinusInfection'))
ax.legend()

fig.tight_layout()
plt.show()


#####



diseases = ['Arthritis', 'Dental Care', 'GenericProblem', 'HighCholesterol', 'Hypertension', 'Overweight', 'SinusInfection']

n_groups = 7

# means_men = (20, 35, 30, 35, 27)
ratios_young_ori = [0.014299332697807437, 0.11713520749665328, 0.05402425578831312, 0.026224982746721876, 0.03026227303295225, 0.09443099273607748, 0.0]
ratios_mid_ori = [0.3517635843660629, 0.4323962516733601, 0.39911797133406834, 0.38233264320220844, 0.37995965030262274, 0.4915254237288136, 0.4918793503480278]
ratios_old_ori = [0.6339370829361296, 0.4504685408299866, 0.5468577728776185, 0.5914423740510697, 0.589778076664425, 0.41404358353510895, 0.5081206496519721]

ratios_young_rf = [0.1725206611570248, 0.20981842636180228, 0.23076923076923078, 0.2158931082981716, 0.19786096256684493, 0.22194513715710723, 0.19270833333333334]
ratios_mid_rf = [0.3925619834710744, 0.38802958977807667, 0.37259615384615385, 0.38677918424753865, 0.38235294117647056, 0.3940149625935162, 0.40234375]
ratios_old_rf = [0.43491735537190085, 0.4021519838601211, 0.39663461538461536, 0.39732770745428975, 0.4197860962566845, 0.38403990024937656, 0.4049479166666667]
# std_men = (2, 3, 4, 1, 2)
#
# means_women = (25, 32, 34, 20, 25)
# std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, ratios_young_ori, bar_width,
                alpha=opacity, color='skyblue',
                error_kw=error_config,
                label='Original Data - Young Age')
rects1 = ax.bar(index, np.add(ratios_young_ori, ratios_mid_ori), bar_width,
                alpha=opacity, color='dodgerblue',
                error_kw=error_config,
                label='Original Data - Middle Age')
rects1 = ax.bar(index, np.full(len(ratios_young_ori), 1), bar_width,
                alpha=opacity, color='darkblue',
                error_kw=error_config,
                label='Original Data - Old Age')

rects2 = ax.bar(index + bar_width, ratios_young_rf, bar_width,
                alpha=opacity, color='violet',
                error_kw=error_config,
                label='RF Filter Variables - Young Age')
rects2 = ax.bar(index + bar_width, np.add(ratios_young_rf, ratios_mid_rf), bar_width,
                alpha=opacity, color='darkviolet',
                error_kw=error_config,
                label='RF Filter Variables - Middle Age')
rects2 = ax.bar(index + bar_width, np.full(len(ratios_young_rf), 1), bar_width,
                alpha=opacity, color='purple',
                error_kw=error_config,
                label='RF Filter Variables - Old Age')

ax.set_xlabel('Diseases')
ax.set_ylabel('Age Group Ratio')
ax.set_title('Ratio of age having the diseases')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Arthritis', 'Dental Care', 'GenericProblem', 'HighCholesterol', 'Hypertension', 'Overweight', 'SinusInfection'))
ax.legend()

fig.tight_layout()
plt.show()























# Plot the figure.
plt.figure(figsize=(12, 8))
ax = ratios_freq.plot(kind='bar')
ax.set_title('Male Ratio in most common disease')
ax.set_xlabel('Disease')
ax.set_ylabel('Ratio')
ax.set_xticklabels(diseases)

rects = ax.patches

# Make some labels.
ratios_str = [str(ratio) for ratio in ratios]
labels = ["label%d" % i for i in range(len(rects))]

for rect, ratio in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, ratio,
            ha='center', va='bottom')

plt.show()


# # Bring some raw data.
# frequencies = [6, 16, 75, 160, 244, 260, 145, 73, 16, 4, 1]
# # In my original code I create a series and run on that,
# # so for consistency I create a series from the list.
# freq_series = pd.Series.from_array(frequencies)
#
# x_labels = [108300.0, 110540.0, 112780.0, 115020.0, 117260.0, 119500.0,
#             121740.0, 123980.0, 126220.0, 128460.0, 130700.0]
#
# # Plot the figure.
# plt.figure(figsize=(12, 8))
# ax = freq_series.plot(kind='bar')
# ax.set_title('Amount Frequency')
# ax.set_xlabel('Amount ($)')
# ax.set_ylabel('Frequency')
# ax.set_xticklabels(x_labels)
#
# rects = ax.patches
#
# # Make some labels.
# labels = ["label%d" % i for i in range(len(rects))]
# print(labels)
#
# for rect, label in zip(rects, labels):
#     height = rect.get_height()
#     ax.text(rect.get_x() + rect.get_width() / 2, height + 5, label,
#             ha='center', va='bottom')
#
# plt.show()