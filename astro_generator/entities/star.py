from pint import Quantity
from astro_generator.constants.spectral_classes import SpectralClass
from astro_generator.constants.unit_registry import SOLAR_LUMINOSITY, SOLAR_MASS, SOLAR_RADIUS
from astro_generator.utils.validator import validate_unit, validate_of_type

class Star():
    def __init__(
        self,
        spectral_class: SpectralClass,
        luminosity: Quantity,
        mass: Quantity,
        radius: Quantity
    ) -> None:
        try:
            validate_of_type(spectral_class, SpectralClass, "spectral_class")
            validate_unit(luminosity, SOLAR_LUMINOSITY, "luminosity", "SOLAR_LUMINOSITY")
            validate_unit(mass, SOLAR_MASS, "mass", "SOLAR_MASS")
            validate_unit(radius, SOLAR_RADIUS, "radius", "SOLAR_RADIUS")
        except Exception as e:
            raise ValueError(f"An error occured while initializing star: {e}")
        self.spectral_class = spectral_class
        self.luminosity = luminosity