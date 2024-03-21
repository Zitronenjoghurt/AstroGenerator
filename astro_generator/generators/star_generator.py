from numbers import Number
from typing import Optional
from astro_generator.constants.spectral_classes import SpectralClass
from astro_generator.constants.unit_registry import SOLAR_MASS
from astro_generator.configuration import DEFAULT_SPECTRAL_CLASS_PROBABILITY, DEFAULT_MASS_PROBABILITY
from astro_generator.entities import Star
from astro_generator.utils.probability import Probability, ProbabilityGroup

class StarGenerator():
    def __init__(
        self,
        spectral_class_probability: Optional[Probability] = None,
        mass_probability: Optional[ProbabilityGroup] = None
    ) -> None:
        self.spectral_class_probability = spectral_class_probability if isinstance(spectral_class_probability, Probability) else DEFAULT_SPECTRAL_CLASS_PROBABILITY
        self.mass_probability = mass_probability if isinstance(mass_probability, ProbabilityGroup) else DEFAULT_MASS_PROBABILITY

        try:
            self.spectral_class_probability.validate(SpectralClass, 1, "spectral_class")
            self.mass_probability.validate(Number, 1, "mass")
        except Exception as e:
            raise ValueError(f"An error occured while initializing SolarSystemGenerator: {e}")

    def generate(self) -> Star:
        spectral_class: SpectralClass = self.spectral_class_probability.generate()
        mass = self.mass_probability.generate(spectral_class.value, 0)

        return Star(
            spectral_class=spectral_class,
            mass = mass * SOLAR_MASS
        )