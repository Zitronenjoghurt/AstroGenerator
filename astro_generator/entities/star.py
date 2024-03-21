from pint import Quantity
from astro_generator.constants.spectral_classes import SpectralClass
from astro_generator.constants.unit_registry import UNIT_REGISTRY, SOLAR_LUMINOSITY, SOLAR_MASS, SOLAR_RADIUS, METALLICITY, KM_PER_SEC
from astro_generator.utils.validator import validate_unit, validate_of_type

class Star():
    def __init__(
        self,
        spectral_class: SpectralClass,
        #luminosity: Quantity,
        mass: Quantity,
        #radius: Quantity,
        #age: Quantity,
        #rotation_speed: Quantity,
        #metallicity: Quantity
    ) -> None:
        """A class representing properties of a star

        Args:
            spectral_class (SpectralClass): A short code summarizing the ionization state
            luminosity (Quantity): Total amount of electromagnetic energy emitted per unit of time
            mass (Quantity): Total mass
            radius (Quantity): Average radius
            age (Quantity): How old the star is
            rotation_speed (Quantity): How fast the star is spinning arount its rotational axis
            metallicity (Quantity): Abundance of elements heavier than hydrogen and helium inside the star

        Raises:
            ValueError: On invalid initialization values.
        """
        try:
            validate_of_type(spectral_class, SpectralClass, "spectral_class")
            #validate_unit(luminosity, SOLAR_LUMINOSITY, "luminosity", "SOLAR_LUMINOSITY")
            validate_unit(mass, SOLAR_MASS, "mass", "SOLAR_MASS")
            #validate_unit(radius, SOLAR_RADIUS, "radius", "SOLAR_RADIUS")
            #validate_unit(age, UNIT_REGISTRY.year, "age", "UNIT_REGISTRY.year")
            #validate_unit(rotation_speed, KM_PER_SEC, "rotation_speed", "KM_PER_SEC")
            #validate_unit(metallicity, METALLICITY, "metallicity", "METALLICITY")
        except Exception as e:
            raise ValueError(f"An error occured while initializing star: {e}")
        
        self.spectral_class = spectral_class
        #self.luminosity = luminosity
        self.mass = mass
        #self.radius = radius
        #self.age = age
        #self.rotation_speed = rotation_speed
        #self.metallicity = metallicity