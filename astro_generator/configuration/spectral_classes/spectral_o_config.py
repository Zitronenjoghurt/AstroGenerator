from astro_generator.utils.probability import Probability

DEFAULT_MASS_PROBABILITY = Probability.create(
    {"min": 16.0, "max": 100.0}
)

DEFAULT_TEMPERATURE_PROBABILITY = Probability.create(
    {"min": 33000.0, "max": 60000.0}
)

DEFAULT_BASE_ROTATION_SPEED_PROBABILITY = Probability.create(
    {"min": 300.0, "max": 500.0}
)