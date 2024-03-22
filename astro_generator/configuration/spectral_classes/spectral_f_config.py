from astro_generator.utils.probability import Probability

DEFAULT_MASS_PROBABILITY = Probability.create(
    {"min": 1.04, "max": 1.4}
)

DEFAULT_TEMPERATURE_PROBABILITY = Probability.create(
    {"min": 6000.0, "max": 7300.0}
)

DEFAULT_BASE_ROTATION_SPEED_PROBABILITY = Probability.create(
    {"min": 30.0, "max": 150.0}
)