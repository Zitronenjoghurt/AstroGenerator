from astro_generator.utils.probability import Probability

DEFAULT_MASS_PROBABILITY = Probability.create(
    {"min": 0.08, "max": 0.45}
)

DEFAULT_TEMPERATURE_PROBABILITY = Probability.create(
    {"min": 2300, "max": 3900}
)