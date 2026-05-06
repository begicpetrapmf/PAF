from program import simulacija
import numpy as np
import matplotlib.pyplot as plt

# Magnetno polje
B = np.array([0, 0, 1])
E = np.array([0, 0, 0])
v0 = [1, 1, 1]   
r0 = [0, 0, 0]
traj = simulacija(q=1, m=1, E=E, B=B, r0=r0, v0=v0)
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.plot(traj[:,0], traj[:,1], traj[:,2])
ax.set_title("Heliks (samo B polje)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Elektron i pozitron
traj_e = simulacija(q=-1, m=1, E=E, B=B, r0=r0, v0=v0)
traj_p = simulacija(q=+1, m=1, E=E, B=B, r0=r0, v0=v0)
ax2 = fig.add_subplot(122)
ax2.plot(traj_e[:,0], traj_e[:,1], color="blue", label="elektron (q<0)")
ax2.plot(traj_p[:,0], traj_p[:,1], color="red", label="pozitron (q>0)")

step = 200
for i in range(0, len(traj_e)-1, step):
    ax2.arrow(traj_e[i,0], traj_e[i,1],
              traj_e[i+1,0] - traj_e[i,0],
              traj_e[i+1,1] - traj_e[i,1],
              color="blue", head_width=0.1, length_includes_head=True)

for i in range(0, len(traj_p)-1, step):
    ax2.arrow(traj_p[i,0], traj_p[i,1],
              traj_p[i+1,0] - traj_p[i,0],
              traj_p[i+1,1] - traj_p[i,1],
              color="red", head_width=0.1, length_includes_head=True)

ax2.set_title("Elektron vs pozitron (smjer rotacije)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.legend()

# Razlicite komb. poljā
slucajevi = [
    ("Samo B", np.array([0,0,0]), np.array([0,0,1])),
    ("Samo E", np.array([1,0,0]), np.array([0,0,0])),
    ("E ⟂ B", np.array([1,0,0]), np.array([0,0,1])),
    ("E || B", np.array([0,0,1]), np.array([0,0,1]))
]

fig2, axs = plt.subplots(2, 2, figsize=(10,8))

for i, (naziv, E, B) in enumerate(slucajevi):
    ax = axs[i//2, i%2]
    traj_e = simulacija(q=-1, m=1, E=E, B=B, r0=r0, v0=v0)
    traj_p = simulacija(q=+1, m=1, E=E, B=B, r0=r0, v0=v0)
    ax.plot(traj_e[:,0], traj_e[:,1], color="blue", label="e⁻")
    ax.plot(traj_p[:,0], traj_p[:,1], color="red", label="e⁺")
    ax.legend()
    ax.set_title(naziv)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

plt.tight_layout()
plt.show()

# Dodatno: 3D za elektron i pozitron
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')
traj_e = simulacija(q=-1, m=1, E=np.array([0,0,0]), B=np.array([0,0,1]), r0=[0,0,0], v0=[1,1,1])
traj_p = simulacija(q=+1, m=1, E=np.array([0,0,0]), B=np.array([0,0,1]), r0=[0,0,0], v0=[1,1,1])
ax3.plot(traj_e[:,0], traj_e[:,1], traj_e[:,2], color="blue", label="elektron")
ax3.plot(traj_p[:,0], traj_p[:,1], traj_p[:,2], color="red", label="pozitron")
ax3.set_title("3D heliks: elektron vs pozitron")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.set_zlabel("z")
ax3.legend()
plt.show()