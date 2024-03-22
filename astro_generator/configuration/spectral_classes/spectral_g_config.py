from astro_generator.utils.probability import Probability

DEFAULT_MASS_PROBABILITY = Probability.create(
    {"min": 0.8, "max": 1.04}
)

DEFAULT_TEMPERATURE_PROBABILITY = Probability.create(
    {"min": 5300.0, "max": 6000.0}
)

DEFAULT_BASE_ROTATION_SPEED_PROBABILITY = Probability.create(
    {"min": 15.0, "max": 30.0}
)