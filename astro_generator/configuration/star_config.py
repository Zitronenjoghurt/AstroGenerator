from astro_generator.constants.spectral_classes import SpectralClass
from astro_generator.utils.probability import Probability

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