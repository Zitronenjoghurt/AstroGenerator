from astro_generator.utils.probability import Probability

DEFAULT_MASS_PROBABILITY = Probability.create(
    {"min": 2.1, "max": 16}
)

DEFAULT_TEMPERATURE_PROBABILITY = Probability.create(
    {"min": 10000.0, "max": 33000.0}
)

DEFAULT_BASE_ROTATION_SPEED_PROBABILITY = Probability.create(
    {"min": 100.0, "max": 300.0}
)