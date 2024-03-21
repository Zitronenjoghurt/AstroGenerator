from astro_generator.utils.probability import Probability

DEFAULT_STAR_COUNT_PROBABILITY = Probability.create(
    {
        "weights": [666, 200, 100, 30, 3, 1],
        "values": [1, 2, 3, 4, 5, 6]
    }
)