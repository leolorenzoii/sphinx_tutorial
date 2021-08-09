"""A bicycle wheel is a wheel, most commonly a wire wheel, designed for a
bicycle"""

def roll(num):
    """Keep rolling the wheel `num` times!

    Parameters
    ----------
    num : int
        Number of times to roll the wheel

    Returns
    -------
    status : str
        Say how many times the wheel has been rolled!
    """
    return "Keep " + "rolling "*num + "wah!"
