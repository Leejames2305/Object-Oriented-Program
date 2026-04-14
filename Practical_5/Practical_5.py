# ===== 5.1 =====
# import glob

# files = glob.glob('Practical_5/A5a-inputs/*.csv')
# print(files)


# ===== 5.2 =====
# import pandas as pd

# df = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0],  
#                   [7.0, 3.2, 1], [6.4, 3.2, 1],  
#                   [5.9, 3.0, 2]], 
#                 columns=['length', 'width', 'species'])
# print(df)

# import matplotlib
# import matplotlib.pyplot as plt
# # matplotlib.use('TkAgg')

# ax1 = df.plot.scatter(x='length', y='width', c='red')
# ax1.plot(df['length'], df['width'], c='blue')

# plt.show()


# ===== Exercise A5a =====
# import glob
# import pandas as pd
# import matplotlib.pyplot as plt

# files = glob.glob('Practical_5/A5a-inputs/*.csv')
# files.sort(reverse=True)  # Sort in reverse order to match colours with files

# # 3 rows and 3 columns, 2nd and 5th are empty
# # Total of 4 csv, each with different colours [black, orange, brown, blue]
# # All share the same x and y axis limits and alignments

# colours = ['black', 'orange', 'brown', 'blue']
# positions = [1, 3, 6, 4]  # 321, 323, 326, 324 subplot positions

# for i, file in enumerate(files):
#     ax = plt.subplot(3, 2, positions[i])
#     df = pd.read_csv(file)
#     ax.plot(df['yx'], df['xy'], '*', markersize=3, c=colours[i])
#     ax.grid()
#     ax.set_xticks([60, 80, 100])
#     ax.set_yticks([50, 75, 100])

# plt.tight_layout()
# plt.show()


# ===== Exercise A5b =====
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = 'Practical_5/A5b-input.txt'

# Plot using polyfit() and poly1d()
# Dimensions be 10 x 8
# Blue dot are original data points, red line with dot is linear fit first 12 points
# Black line is linear fit all 20 points, yellow line is polynomial fit
# The files contain 4 column: X0, Y0, X1, Y1
# XO Y0 in one plot, X1 Y1 in another plot

df = pd.read_csv(file, skipinitialspace=True)

# Assign variables from the loaded dataframe
x0, y0 = df['X0'], df['Y0']
x1, y1 = df['X1'], df['Y1']

# First plot
plt.figure(figsize=(10, 8))
plt.plot(x0, y0, 'bo', label='Data Points')

linearModel12 = np.poly1d(np.polyfit(x0[:12], y0[:12], 1))
polyline = np.linspace(min(x0[:12]), max(x0[:12]), 100)
plt.plot(polyline, linearModel12(polyline), color='red', label='Linear Fit (First 12 Points)')

linearModelAll = np.poly1d(np.polyfit(x0, y0, 1))
polylilne = np.linspace(min(x0), max(x0), 100)
plt.plot(polylilne, linearModelAll(polylilne), color='black', label='Linear Fit (All Points)')

polyModel = np.poly1d(np.polyfit(x0, y0, 3))  # 3rd degree polynomial fit
plt.plot(x0, polyModel(x0), color='yellow', label='Polynomial Fit (All Points)')

plt.title('X0 vs Y0')
plt.xlabel('X0')
plt.ylabel('Y0')
plt.legend()
plt.grid()

# Second plot
plt.figure(figsize=(10, 8))
plt.plot(x1, y1, 'bo', label='Data Points')

linearModel12 = np.poly1d(np.polyfit(x1[:12], y1[:12], 1))
polyline = np.linspace(min(x1[:12]), max(x1[:12]), 100)
plt.plot(polyline, linearModel12(polyline), color='red', label='Linear Fit (First 12 Points)')

linearModelAll = np.poly1d(np.polyfit(x1, y1, 1))
polylilne = np.linspace(min(x1), max(x1), 100)
plt.plot(polylilne, linearModelAll(polylilne), color='black', label='Linear Fit (All Points)')

polyModel = np.poly1d(np.polyfit(x1, y1, 3))  # 3rd degree polynomial fit
plt.plot(x1, polyModel(x1), color='yellow', label='Polynomial Fit (All Points)')

plt.title('X1 vs Y1')
plt.xlabel('X1')
plt.ylabel('Y1')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()