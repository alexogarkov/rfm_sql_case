# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(F, M, R, segment)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
#df = dataset

df = dataset[
    (dataset['segment'] == 'Champions') |
    (dataset['segment'] == 'Loyal Customers') |
    (dataset['segment'] == 'Potential Loyalists') |
    (dataset['segment'] == 'New Customers')
]

# Define the 3D grid dimensions
grid_size = (3, 3, 3)
voxels = np.zeros(grid_size, dtype=bool)
colors = np.empty(grid_size, dtype=object)

# Define segment colors
segment_color_map = {
    'Champions': '#FFEE00',
    'Loyal Customers': '#B0D0E0',
    'Potential Loyalists': '#CD7F32',
    'New Customers': '#50C878'
}

# Fill voxel grid and assign colors
for _, row in df.iterrows():
    r, f, m, segm = row['R'], row['F'], row['M'], row['segment']
    voxels[r-1, f-1, m-1] = True  # Adjust for zero-based indexing
    colors[r-1, f-1, m-1] = segment_color_map[segm]

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection='3d')

ax.voxels(voxels, facecolors=colors, edgecolors=None, alpha=0.63, linewidth=0.1)

ax.view_init(elev=20, azim=160)

ax.set_xlabel('Recency (R)')
ax.set_ylabel('Frequency (F)')
ax.set_zlabel('Monetary (M)')
ax.set_xlim(0,3)
ax.set_ylim(0,3)
ax.set_xticks([0, 1, 2, 3])
ax.set_yticks([0, 1, 2, 3])
ax.set_zticks([0, 1, 2, 3])

legend_patches = [Patch(facecolor=color, label=segm) for segm, color in segment_color_map.items()]
ax.legend(handles=legend_patches, bbox_to_anchor=(1.05, 1))

plt.tight_layout()
plt.show()