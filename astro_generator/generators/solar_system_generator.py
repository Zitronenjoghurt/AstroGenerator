from typing import Optional
from astro_generator.entities import SolarSystem
from astro_generator.utils.probability import Probability

DEFAULT_STAR_COUNT_PROBABILITY = Probability.create(
    {
        "weights": [666, 200, 100, 30, 3, 1],
        "values": [1, 2, 3, 4, 5, 6]
    }
)

class SolarSystemGenerator():
    def __init__(
        self,
        star_count_probability: Optional[Probability] = None
    ) -> None:
        self.star_count_probability = star_count_probability if isinstance(star_count_probability, Probability) else DEFAULT_STAR_COUNT_PROBABILITY

        try:
            self.star_count_probability.validate(int, 1, "star_count")
        except Exception as e:
            raise ValueError(f"An error occured while initializing SolarSystemGenerator: {e}")

    def generate(self) -> SolarSystem:
        return SolarSystem([])