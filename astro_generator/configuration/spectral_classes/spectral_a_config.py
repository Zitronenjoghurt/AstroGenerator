from astro_generator.utils.probability import Probability

DEFAULT_MASS_PROBABILITY = Probability.create(
    {"min": 1.4, "max": 2.1}
)

DEFAULT_TEMPERATURE_PROBABILITY = Probability.create(
    {"min": 7300.0, "max": 10000.0}
)

DEFAULT_BASE_ROTATION_SPEED_PROBABILITY = Probability.create(
    {"min": 50.0, "max": 225.0}
)