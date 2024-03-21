from typing import Optional
from astro_generator.configuration import DEFAULT_STAR_COUNT_PROBABILITY
from astro_generator.entities import SolarSystem
from astro_generator.generators.star_generator import StarGenerator
from astro_generator.utils.probability import Probability

class SolarSystemGenerator():
    def __init__(
        self,
        star_count_probability: Optional[Probability] = None,
        star_generator: Optional[StarGenerator] = None
    ) -> None:
        self.star_count_probability = star_count_probability if isinstance(star_count_probability, Probability) else DEFAULT_STAR_COUNT_PROBABILITY
        self.star_generator = star_generator if isinstance(star_generator, StarGenerator) else StarGenerator()

        try:
            self.star_count_probability.validate(int, 1, "star_count")
        except Exception as e:
            raise ValueError(f"An error occured while initializing SolarSystemGenerator: {e}")

    def generate(self) -> SolarSystem:
        star_count = self.star_count_probability.generate()
        stars = []
        for _ in range(star_count):
            star = self.star_generator.generate()
            stars.append(star)

        return SolarSystem(
            stars=stars
        )