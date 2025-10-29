import random


class Leg:
    """
    Leg class - Represents one leg of the robotic dog

    Students should implement movement and control logic for each leg.
    """

    def __init__(self, leg_id, position):
        """
        Initialize a leg

        Args:
            leg_id (int): Unique identifier for this leg (1-4)
            position (str): Position of the leg ("front-left", "front-right", "back-left", "back-right")
        """
        self.id = leg_id
        self.position = position
        self.status = "active"
        self._angle = 0

    def move(self, angle):
        """
        Move the leg to a specific angle

        Args:
            angle (float): The angle to move the leg to
        """
        self._angle = angle

    def reset(self):
        """Reset the leg to its default position"""
        self._angle = 0

    def __str__(self):
        """String representation of the leg"""
        return f"Leg {self.id} ({self.position}) at angle {self._angle}°"


# ====== INHERITANCE EXAMPLE 1 ======
class AdvancedLeg(Leg):
    """
    AdvancedLeg class - Inherits from Leg and adds advanced movement features.
    Demonstrates inheritance and polymorphism.
    """

    def move(self, angle):
        """
        Override the base move() method with smoother motion.
        """
        print(f"[AdvancedLeg] Moving {self.position} smoothly to angle {angle}°")
        super().move(angle)

    def jump(self):
        """
        Makes the leg perform a jump-like motion.
        """
        print(f"[AdvancedLeg] {self.position} leg is jumping!")
        self._angle = 45  # temporary lifted angle
        self.reset()


class Sensor:
    """
    Sensor class - Represents sensors on the robotic dog
    """

    def __init__(self, sensor_type):
        """
        Initialize a sensor

        Args:
            sensor_type (str): Type of sensor ("ultrasonic", "IMU", "camera", etc.)
        """
        self.sensor_type = sensor_type
        self.reading = 0

    def read_data(self):
        """Read data from the sensor"""
        self.reading = random.uniform(0, 100)
        return self.reading

    def calibrate(self):
        """Calibrate the sensor"""
        self.reading = 0


# ====== INHERITANCE EXAMPLE 2 ======
class CameraSensor(Sensor):
    """
    CameraSensor class - Inherits from Sensor and adds image capture functionality.
    Demonstrates inheritance and polymorphism.
    """

    def read_data(self):
        """
        Override to simulate visual data (instead of numeric readings)
        """
        self.reading = f"Image captured at resolution 640x480"
        return self.reading

    def capture_image(self):
        """
        Simulates taking a photo.
        """
        print("[CameraSensor] Capturing image... Done!")


class RoboticDog:
    """
    RoboticDog class - Main class representing the robotic dog

    ============================================================================
    STUDENT TODO: Implement the move() and find_ball() methods to navigate!
    ============================================================================
    """

    def __init__(self, name):
        """Initialize the robotic dog"""
        self.name = name
        self.legs = {}
        self.sensors = []
        self.battery_level = 100

        # Position attributes
        self.x = 100
        self.y = 300
        self.target_x = 100
        self.target_y = 100
        self.size = 20
        self.velocity_x = 0
        self.velocity_y = 0

    def add_leg(self, leg):
        """Add a leg to the robotic dog"""
        self.legs[leg.position] = leg

    def add_sensor(self, sensor):
        """Add a sensor to the robotic dog"""
        self.sensors.append(sensor)

    def move(self, dx, dy):
        """
        ========================================================================
        STUDENT TODO: Move the dog by updating target_x and target_y
        ========================================================================

        This method should update the dog's target position based on desired 
        movement. The game engine will handle collision detection and smooth 
        movement animation automatically.

        Args:
            dx (float): Desired change in x direction 
                        (positive = right, negative = left)
            dy (float): Desired change in y direction 
                        (positive = down, negative = up)

        Example usage:
            self.move(5, 0)    # Move 5 pixels to the right
            self.move(0, -3)   # Move 3 pixels up
            self.move(2, 2)    # Move diagonally down-right

        IMPORTANT: 
        - Simply update self.target_x and self.target_y
        - The game engine checks for collisions automatically
        - If you try to move into a wall, the movement will be blocked
        ========================================================================
        """
        # STUDENT IMPLEMENTATION HERE
        # Example starter code (you should keep or modify this):
        self.target_x += dx
        self.target_y += dy

    def find_ball(self, ball_pos, obstacle_data):
        """
        ========================================================================
        STUDENT TODO: Main pathfinding method - Navigate maze to reach the ball
        ========================================================================

        This method is called every frame. You should:
        1. Calculate the direction to the ball using ball_pos
        2. Decide on a movement strategy to avoid obstacles
        3. Call self.move(dx, dy) to update the target position

        Args:
            ball_pos (tuple): (x, y) position of the ball
            obstacle_data (list): List of obstacle dictionaries, each with:
                                  {'x': float, 'y': float, 
                                   'width': float, 'height': float}

        Available attributes:
            self.x, self.y: Current position of the dog
            self.target_x, self.target_y: Target position (where dog moves to)
            self.size: Size of the dog (20 pixels)

        Example obstacle_data structure:
        [
            {'x': 200, 'y': 40, 'width': 30, 'height': 200},
            {'x': 400, 'y': 160, 'width': 30, 'height': 200},
            ...
        ]

        STRATEGY HINTS:
        - Start simple: move directly toward the ball
        - Check if obstacles are in your path
        - If blocked, try moving around the obstacle
        - Consider checking obstacles within a certain distance
        - You can use obstacle_data to detect walls ahead

        IMPORTANT: 
        - The game engine handles collision detection automatically
        - If you try to move into a wall, the movement will be blocked
        - Your job is to make smart decisions about where to move
        - Think about how to detect when you're stuck and need to go around

        EXAMPLE: Simple direct movement (starter code):
        ========================================================================
        """
        # STUDENT IMPLEMENTATION HERE

        # Calculate direction to ball
        dx = ball_pos[0] - self.x
        dy = ball_pos[1] - self.y

        # Simple approach: move directly toward the ball
        # This works on simple mazes but struggles with complex ones!
        move_speed = 2

        if abs(dx) > 5:
            self.move(move_speed if dx > 0 else -move_speed, 0)
        if abs(dy) > 5:
            self.move(0, move_speed if dy > 0 else -move_speed)

        # TODO: Add obstacle avoidance logic!
        # 
        # HINTS for improvement:
        # 1. Loop through obstacle_data to find nearby obstacles
        # 2. Check if an obstacle is between you and the ball
        # 3. If blocked, decide to go up/down or left/right around it
        # 4. Consider using a simple algorithm like wall-following
        #
        # Example of checking if obstacle is nearby:
        # for obs in obstacle_data:
        #     # Calculate distance to obstacle
        #     obs_center_x = obs['x'] + obs['width'] / 2
        #     obs_center_y = obs['y'] + obs['height'] / 2
        #     distance_to_obs = ((obs_center_x - self.x)**2 + 
        #                        (obs_center_y - self.y)**2)**0.5
        #     
        #     if distance_to_obs < 100:  # If obstacle is close
        #         # Decide how to avoid it...
        #         pass

    def check_status(self):
        """Print the current status of the robotic dog"""
        print(f"\n{'=' * 50}")
        print(f"Robot: {self.name}")
        print(f"{'=' * 50}")
        print(f"Battery: {self.battery_level}%")
        print(f"Position: ({self.x}, {self.y})")
        print(f"Legs: {len(self.legs)}")
        print(f"Sensors: {len(self.sensors)}")
        print(f"{'=' * 50}\n")

    def recharge(self):
        """Recharge the battery to 100%"""
        self.battery_level = 100


if __name__ == "__main__":
    print("Testing RoboticDog implementation...")

    test_dog = RoboticDog("TestBot")

    # Add legs (showing inheritance)
    test_dog.add_leg(AdvancedLeg(1, "front-left"))
    test_dog.add_leg(Leg(2, "front-right"))
    test_dog.add_leg(Leg(3, "back-left"))
    test_dog.add_leg(AdvancedLeg(4, "back-right"))

    # Add sensors (including camera)
    test_dog.add_sensor(Sensor("ultrasonic"))
    test_dog.add_sensor(CameraSensor("camera"))

    test_dog.check_status()

    print("Testing movement...")
    test_dog.move(5, 0)
    print(f"New target position: ({test_dog.target_x}, {test_dog.target_y})")

    print("\nTesting leg behaviors...")
    for leg in test_dog.legs.values():
        leg.move(30)
        if isinstance(leg, AdvancedLeg):
            leg.jump()

    print("\nTesting sensors...")
    for sensor in test_dog.sensors:
        print(f"{sensor.sensor_type} reading: {sensor.read_data()}")

    print("\nTesting obstacle data format...")
    test_obstacles = [
        {'x': 200, 'y': 40, 'width': 30, 'height': 200},
        {'x': 400, 'y': 160, 'width': 30, 'height': 200}
    ]
    print(f"Sample obstacle: {test_obstacles[0]}")
    print(f"Obstacle at x={test_obstacles[0]['x']}, y={test_obstacles[0]['y']}")
    print(f"Size: {test_obstacles[0]['width']} x {test_obstacles[0]['height']}")

    print("\nImplementation test complete!")
    print("Run main.py to see your dog in action in the maze!")