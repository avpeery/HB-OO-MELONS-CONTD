"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__ (self, species, qty): 
        self.species = species 
        self.qty = qty 


    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    shipped = False
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
"""An international (non-US) melon order."""
        
    shipped = False
    order_type = "international"
    tax = 0.17


    def__init__(self, country code):
        super().def__init__(self)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
