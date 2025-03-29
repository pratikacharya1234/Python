from bumblebee import Keyboard

# Initialize the Keyboard controller with default parameters:
#   - typing_speed: 100 (default percentage of ideal speed)
#   - consistency: 95 (default consistency percentage, affecting delay variability)
#   - typo_rate: 5 (default typo frequency percentage)
keyboard = Keyboard()

# Adjust typing speed.
# The typing speed is provided as a percentage relative to the original Bumblebee typing speed.
# Acceptable types: int or float.
keyboard.set_speed(new_speed=40)  # Increase the typing speed to 400%

# Adjust typo rate.
# The new typo rate must be a value between 0 and 100 (int or float).
keyboard.set_typo_rate(3)  # Set typo rate to 3%

# Adjust consistency.
# A higher consistency (0-100) increases typing speed with less delay variability.
keyboard.set_consistency(99)  # Set consistency to 99%

# Type a sample text.
text = "Bumblebee is great."
keyboard.type(text)  # 'text' must be a string.