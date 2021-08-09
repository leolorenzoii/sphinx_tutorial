"""A bicycle handlebar is the steering control for bicycles."""

def turn(direction):
    """Return a notification of the turning direction specified

    Parameters
    ----------
    direction : str
        The direction in which to turn the bicycle

    Returns
    -------
    turning_direction : str
        A notification of where the bicycle is currently turning
    """
    return f"The bicycle is being turned {direction}"
