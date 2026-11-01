from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from fuzzy_c_means import fuzzy_c_means



image = Image.open("milky-way-nvg.jpg")
print(image.size)
print(image.mode)

image_small = image.resize((128, 128))
image_array = np.array(image_small)

pixels = image_array.flatten()

U, centers = fuzzy_c_means(pixels, c=2)

U_array = np.array(U)
heatmaps = U_array.reshape((128,128,2))

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(image_array, cmap="gray")
axes[0].set_title("Image originale")

im1 = axes[1].imshow(heatmaps[:, :, 0], cmap="hot", vmin=0, vmax=1)
axes[1].set_title("Cluster 1")
fig.colorbar(im1, ax=axes[1])

im2 = axes[2].imshow(heatmaps[:, :, 1], cmap="hot", vmin=0, vmax=1)
axes[2].set_title("Cluster 2")
fig.colorbar(im2, ax=axes[2])

for ax in axes:
    ax.axis("off")

plt.tight_layout()
plt.savefig("segmentation_fcm_grayscale.png", dpi=300, bbox_inches="tight")
plt.show()

print("Centres :", centers)
print("Nombre de pixels :", len(U))
print("Premier pixel :", U[0])
print(image_array.shape)
print(pixels.shape)
 