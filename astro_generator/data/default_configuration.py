from astro_generator.constants.spectral_classes import SpectralClass
from astro_generator.utils.probability import Probability

# region SOLAR SYSTEM
DEFAULT_STAR_COUNT_PROBABILITY = Probability.create(
    {
        "weights": [666, 200, 100, 30, 3, 1],
        "values": [1, 2, 3, 4, 5, 6]
    }
)
# endregion

# region STAR
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
# endregion