import math
def calculate_ackerman_angle(wheelbase, track, turn_radius):
    """
    Calculate the Ackerman steering angles for the inner and outer wheels.

    Parameters:
    wheelbase (float): The distance between the front and rear wheels.
    track (float): The width of the vehicle (distance between the left and right wheels).
    turn_radius (float): The radius of the turning circle.

    Returns:
    tuple: A tuple containing the inner and outer wheel angles in degrees.
    """

    # The angle of the inside wheel is determined by the intersection of lines from
    # the rear axle and the center of the turn radius to the extended lines of the front axle
    # This is a simplification and does not account for dynamic effects such as slip angle

    # Calculate the angle for the inner wheel (Ackerman principle)
    inner_angle_rad = math.atan(wheelbase / (turn_radius - (track / 2)))
    # Calculate the angle for the outer wheel
    outer_angle_rad = math.atan(wheelbase / (turn_radius + (track / 2)))

    # Convert radians to degrees for output
    inner_angle_deg = math.degrees(inner_angle_rad)
    outer_angle_deg = math.degrees(outer_angle_rad)

    return inner_angle_deg, outer_angle_deg

# Example usage:
if __name__ == "__main__":
    wheelbase = 2.5  # Example wheelbase in meters
    track = 1.5  # Example track width in meters
    turn_radius = 6  # Example turn radius in meters

    inner_angle, outer_angle = calculate_ackerman_angle(wheelbase, track, turn_radius)
    print(f"Inner Wheel Angle: {inner_angle:.2f} degrees")
    print(f"Outer Wheel Angle: {outer_angle:.2f} degrees")
