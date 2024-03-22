from astro_generator.utils.probability import Probability

DEFAULT_MASS_PROBABILITY = Probability.create(
    {"min": 0.45, "max": 0.8}
)

DEFAULT_TEMPERATURE_PROBABILITY = Probability.create(
    {"min": 3900, "max": 5300}
)