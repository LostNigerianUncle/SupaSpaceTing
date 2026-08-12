import numpy as np
from os import name
from physics import euler_step # type: ignore
from constants import MU_EARTH, R_EARTH # type: ignore

def circular_orbit_velocity(altitude):
    """
    Calculate the circular orbit velocity at a given altitude above Earth's surface.

    Parameters:
    altitude (float): Altitude above Earth's surface in meters.

    Returns:
    float: Circular orbit velocity in meters per second.
    """
    r = R_EARTH + altitude  # Total distance from Earth's center
    return np.sqrt(MU_EARTH / r)

def run_simulation(initial_altitude, time_step, total_time):
    """
    Run a simulation of a satellite in circular orbit around Earth.

    Parameters:
    initial_altitude (float): Initial altitude above Earth's surface in meters.
    time_step (float): Time step for the simulation in seconds.
    total_time (float): Total simulation time in seconds.

    Returns:
    list: List of positions and velocities at each time step.
    """
    # Initial conditions
    r = R_EARTH + initial_altitude  # Total distance from Earth's center
    v = circular_orbit_velocity(initial_altitude)  # Circular orbit velocity

    # Initialize position and velocity vectors
    position = np.array([r, 0])  # Start at (r, 0)
    velocity = np.array([0, v])   # Velocity perpendicular to position

    results = []

    for t in np.arange(0, total_time, time_step):
        results.append((position.copy(), velocity.copy()))
        position, velocity = euler_step(position, velocity, time_step)

    return results

if name == "__main__":
    # Example usage
    initial_altitude = 400e3  # 400 km above Earth's surface
    time_step = 10.0          # 10 seconds
    total_time = 3600.0       # 1 hour

    simulation_results = run_simulation(initial_altitude, time_step, total_time)

    for pos, vel in simulation_results:
        print(f"Position: {pos}, Velocity: {vel}")