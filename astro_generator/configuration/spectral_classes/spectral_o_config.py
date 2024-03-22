from astro_generator.utils.probability import Probability

DEFAULT_MASS_PROBABILITY = Probability.create(
    {"min": 16, "max": 100}
)

DEFAULT_TEMPERATURE_PROBABILITY = Probability.create(
    {"min": 33000, "max": 60000}
)