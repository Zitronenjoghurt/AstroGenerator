from typing import Optional
from astro_generator.constants.spectral_classes import SpectralClass
from astro_generator.data import DEFAULT_SPECTRAL_CLASS_PROBABILITY
from astro_generator.entities import Star
from astro_generator.utils.probability import Probability

class StarGenerator():
    def __init__(
        self,
        spectral_class_probability: Optional[Probability] = None
    ) -> None:
        self.spectral_class_probability = spectral_class_probability if isinstance(spectral_class_probability, Probability) else DEFAULT_SPECTRAL_CLASS_PROBABILITY

        try:
            self.spectral_class_probability.validate(SpectralClass, 1, "spectral_class")
        except Exception as e:
            raise ValueError(f"An error occured while initializing SolarSystemGenerator: {e}")

    def generate(self) -> Star:
        spectral_class = self.spectral_class_probability.generate()

        return Star(
            spectral_class=spectral_class
        )