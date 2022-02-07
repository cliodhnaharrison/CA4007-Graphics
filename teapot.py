from matplotlib import pyplot as plt
import numpy as np

teapot = np.load('teapot.npy')
ax = plt.axes(projection='3d')
ax.plot3D(teapot[:, 0],teapot[:, 1], teapot[:, 2], 'r.')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


# An intrinsics matrix containing a focal length of 1000 pixels and
# c = [cx, cy] = [0, 0].
# An orthonormal rotation matrix = I.
# A translation vector.
