"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__ (self, species, qty, shipped=False): 
        self.species = species 
        self.qty = qty
        self.shipped = shipped


    def get_total(self):
        """Calculate price, including tax."""
        if self.species == "Christmas melon":
            base_price = 7.5
        else:
            base_price = 5
        
        total = (1 + self.tax) * self.qty * base_price 

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17


    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code


    def get_additional_fee(self, qty):
        
        if qty < 10: 
            flat_fee = 3
        else:
            flat_fee = 0

        return flat_fee


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
