from astro_generator.configuration.spectral_classes import MConfig, KConfig, GConfig, FConfig, AConfig, BConfig, OConfig
from astro_generator.constants.spectral_classes import SpectralClass
from astro_generator.utils.probability import Probability, ProbabilityGroup

# https://en.wikipedia.org/wiki/Stellar_classification
DEFAULT_SPECTRAL_CLASS_PROBABILITY = Probability.create(
    {
        "weights": [3, 12000, 61000, 300000, 760000, 1200000, 7600000],
        "values": [
            SpectralClass.O,
            SpectralClass.B,
            SpectralClass.A,
            SpectralClass.F,
            SpectralClass.G,
            SpectralClass.K,
            SpectralClass.M
        ]
    }
)

# In solar masses
DEFAULT_MASS_PROBABILITY = ProbabilityGroup(
    {
        "M": MConfig.DEFAULT_MASS_PROBABILITY,
        "K": KConfig.DEFAULT_MASS_PROBABILITY,
        "G": GConfig.DEFAULT_MASS_PROBABILITY,
        "F": FConfig.DEFAULT_MASS_PROBABILITY,
        "A": AConfig.DEFAULT_MASS_PROBABILITY,
        "B": BConfig.DEFAULT_MASS_PROBABILITY,
        "O": OConfig.DEFAULT_MASS_PROBABILITY
    }
)

# Surface temperature in Kelvin
DEFAULT_TEMPERATURE_PROBABILITY = ProbabilityGroup(
    {
        "M": MConfig.DEFAULT_TEMPERATURE_PROBABILITY,
        "K": KConfig.DEFAULT_TEMPERATURE_PROBABILITY,
        "G": GConfig.DEFAULT_TEMPERATURE_PROBABILITY,
        "F": FConfig.DEFAULT_TEMPERATURE_PROBABILITY,
        "A": AConfig.DEFAULT_TEMPERATURE_PROBABILITY,
        "B": BConfig.DEFAULT_TEMPERATURE_PROBABILITY,
        "O": OConfig.DEFAULT_TEMPERATURE_PROBABILITY
    }
)

# Base rotational speed in Km/s
DEFAULT_BASE_ROTATION_SPEED_PROBABILITY = ProbabilityGroup(
    {
        "M": MConfig.DEFAULT_BASE_ROTATION_SPEED_PROBABILITY,
        "K": KConfig.DEFAULT_BASE_ROTATION_SPEED_PROBABILITY,
        "G": GConfig.DEFAULT_BASE_ROTATION_SPEED_PROBABILITY,
        "F": FConfig.DEFAULT_BASE_ROTATION_SPEED_PROBABILITY,
        "A": AConfig.DEFAULT_BASE_ROTATION_SPEED_PROBABILITY,
        "B": BConfig.DEFAULT_BASE_ROTATION_SPEED_PROBABILITY,
        "O": OConfig.DEFAULT_BASE_ROTATION_SPEED_PROBABILITY
    }
)