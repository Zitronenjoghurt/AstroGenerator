from astro_generator.utils.probability import Probability

DEFAULT_MASS_PROBABILITY = Probability.create(
    {"min": 1.04, "max": 1.4}
)

DEFAULT_TEMPERATURE_PROBABILITY = Probability.create(
    {"min": 6000, "max": 7300}
)