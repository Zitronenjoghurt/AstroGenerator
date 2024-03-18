from enum import Enum

class SpectralClass(Enum):
    """
    Enum for stellar spectral classes.

    These classes are based on the temperature and characteristics of the star's outer envelope, following the Morgan-Keenan (MK) system. 
    
    The classes range from O (hot, blue stars) to M (cool, red stars), with O being the hottest and M the coolest.

    Attributes:
        O: Represents the hottest and most massive blue stars with strong ionized helium lines.
        B: Less hot than O stars, known for neutral helium lines and the beginning of hydrogen lines.
        A: White stars with strong hydrogen lines and weaker metal lines.
        F: Cooler than A stars, with stronger metal lines.
        G: Similar to the Sun, with even stronger metal lines and the presence of calcium.
        K: Cooler than G stars, with prominent metallic lines and molecular bands.
        M: The coolest stars, characterized by a dominance of molecular bands, especially titanium oxide.
    """
    O = "O"
    B = "B"
    A = "A"
    F = "F"
    G = "G"
    K = "K"
    M = "M"