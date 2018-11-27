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