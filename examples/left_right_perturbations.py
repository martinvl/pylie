import numpy as np
import visgeom as vg
import matplotlib
import matplotlib.pyplot as plt
from pylie import SO3, SE3

# Define the pose of a camera.
T_w_c = SE3((SO3.from_roll_pitch_yaw(5*np.pi/4, 0, np.pi/2), np.array([[2, 2, 2]]).T))

# Perturbation.
xsi_vec = np.array([[2, 0, 0, 0, 0, 0]]).T

# Perform the perturbation on the right.
T_r = T_w_c @ SE3.Exp(xsi_vec)

# Perform the perturbation on the left.
T_l = SE3.Exp(xsi_vec) @ T_w_c

# Visualise the perturbations:
# Use Qt 5 backend in visualisation, use latex.
matplotlib.use('qt5agg')

# Create figure and axis.
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Plot frames.
to_right = np.hstack((T_w_c.translation, T_r.translation))
ax.plot(to_right[0, :], to_right[1, :], to_right[2, :], 'k:')
to_left = np.hstack((T_w_c.translation, T_l.translation))
ax.plot(to_left[0, :], to_left[1, :], to_left[2, :], 'k:')
vg.plot_pose(ax, SE3().to_tuple(), text='$\mathcal{F}_w$')
vg.plot_pose(ax, T_w_c.to_tuple(), text='$\mathcal{F}_c$')
vg.plot_pose(ax, T_r.to_tuple(), text='$\mathbf{T}_{wc} Exp(xi)$')
vg.plot_pose(ax, T_l.to_tuple(), text='$Exp(xi) \mathbf{T}_{wc}$')

# Show figure.
vg.plot.axis_equal(ax)
plt.show()
