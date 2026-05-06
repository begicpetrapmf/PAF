import numpy as np
import matplotlib.pyplot as plt

def simulacija(q, m, E, B, r0, v0, dt=0.01, t_max=20, plot=False):
    r = np.array(r0, dtype=float)
    v = np.array(v0, dtype=float)
    steps = int(t_max / dt)
    trajectory = []

    for _ in range(steps):
        trajectory.append(r.copy())
        F = q * (E + np.cross(v, B))
        v = v + (F / m) * dt
        r = r + v * dt
    trajectory = np.array(trajectory)

    if plot:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2])
        ax.set_title("Putanja nabijene čestice")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.show()
    return trajectory


if __name__ == "__main__":
    traj=simulacija(
        q=1,
        m=1,
        E=np.array([0, 0, 0]),
        B=np.array([0, 0, 1]),
        r0=[0, 0, 0],
        v0=[1, 0, 1],
        plot=True
    )