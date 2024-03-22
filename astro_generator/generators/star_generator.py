import math
import numpy as np
import random
from numbers import Number
from typing import Optional
from pint import Quantity
from astro_generator.constants.spectral_classes import SpectralClass
from astro_generator.constants.unit_registry import UNIT_REGISTRY, SOLAR_MASS, SOLAR_LUMINOSITY, SOLAR_RADIUS
from astro_generator.configuration import DEFAULT_SPECTRAL_CLASS_PROBABILITY, DEFAULT_MASS_PROBABILITY, DEFAULT_TEMPERATURE_PROBABILITY
from astro_generator.entities import Star
from astro_generator.utils.probability import Probability, ProbabilityGroup

class StarGenerator():
    def __init__(
        self,
        spectral_class_probability: Optional[Probability] = None,
        mass_probability: Optional[ProbabilityGroup] = None,
        surface_temperature_probability: Optional[ProbabilityGroup] = None
    ) -> None:
        self.spectral_class_probability = spectral_class_probability if isinstance(spectral_class_probability, Probability) else DEFAULT_SPECTRAL_CLASS_PROBABILITY
        self.mass_probability = mass_probability if isinstance(mass_probability, ProbabilityGroup) else DEFAULT_MASS_PROBABILITY
        self.surface_temperature_probability = surface_temperature_probability if isinstance(surface_temperature_probability, ProbabilityGroup) else DEFAULT_TEMPERATURE_PROBABILITY

        try:
            self.spectral_class_probability.validate(SpectralClass, 1, "spectral_class")
            self.mass_probability.validate(Number, 1, "mass")
            self.surface_temperature_probability.validate(Number, 1, "surface_temperature")
        except Exception as e:
            raise ValueError(f"An error occured while initializing StarGenerator: {e}")

    def generate(self) -> Star:
        spectral_class: SpectralClass = self.spectral_class_probability.generate()
        mass = self.mass_probability.generate(spectral_class.value, 0)                               # in solar masses
        surface_temperature = self.surface_temperature_probability.generate(spectral_class.value, 0) # in Kelvin

        # http://hyperphysics.phy-astr.gsu.edu/hbase/Astro/startime.html
        luminosity = mass ** 3.5          # mass-luminosity relationship => solar luminosity
        lifespan = 1e10 * (mass ** -2.5 ) # in years
        age = random.random() * lifespan  # in years

        # Radius using the Stefan-Boltzmann law
        luminosity_solar: Quantity = luminosity * SOLAR_LUMINOSITY
        luminosity_watt  = luminosity_solar.to(UNIT_REGISTRY.watt)
        temperature_kelv = surface_temperature * UNIT_REGISTRY.kelvin
        sigma            = UNIT_REGISTRY.stefan_boltzmann_constant
        radius_meter     = np.sqrt(luminosity_watt / (4 * math.pi * sigma * temperature_kelv ** 4))
        radius: Quantity = radius_meter.to(SOLAR_RADIUS) # type: ignore

        return Star(
            spectral_class=spectral_class,
            mass = mass * SOLAR_MASS,
            luminosity = luminosity_solar,
            lifespan = lifespan * UNIT_REGISTRY.year,
            age = age * UNIT_REGISTRY.year,
            surface_temperature = temperature_kelv,
            radius = radius
        )