import numpy as np
import matplotlib.pyplot as plt

# Generate data using the kinematics equations of motion
def generate_projectile_motion_data(time_steps=50, v0=0, theta=0):
    g = 9.81  # acceleration due to gravity
    theta_rad = np.radians(theta)

    t = np.linspace(0, 5, time_steps)
    x_values = v0 * np.cos(theta_rad) * t
    y_values = v0 * np.sin(theta_rad) * t - 0.5 * g * t ** 2

    projectile_motion_data = []

    # create a Python dict for storing data:
    projectile_data = {
        "initial_velocity": v0,
        "intial_angle": theta_rad,
        "x_values": x_values,
        "y_values": y_values
    }
    projectile_motion_data.append(projectile_data)
    return projectile_motion_data

# Generate batch data using the kinematics equations of motion
def generate_batch_projectile_motion_data(num_samples=100, time_steps=50):
    g = 9.81  # acceleration due to gravity

    velocities = np.random.uniform(5, 35, size=(num_samples, 1))
    angles = np.random.uniform(15, 75, size=(num_samples, 1))
    
    input_parameters = np.hstack([velocities, angles])
    
    batch_projectile_motion_data = []
    for v0, theta in input_parameters:
        theta_rad = np.radians(theta)
        t = np.linspace(0, 5, time_steps)
        x = v0 * np.cos(theta_rad) * t
        y = v0 * np.sin(theta_rad) * t - 0.5 * g * t ** 2
        projectile_data = {
            "initial_velocity": v0,
            "intial_angle": theta,
            "x_values": x,
            "y_values": y
        }
        batch_projectile_motion_data.append(projectile_data)
    
    return batch_projectile_motion_data

if __name__ == '__main__':
    projectile_motion_data = generate_batch_projectile_motion_data(num_samples=2, time_steps=50)
    print(projectile_motion_data)
