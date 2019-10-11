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

        if type(self) == "InternationalMelonOrder" and self.qty < 10:
            total = total + 3

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


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = "government"

    def __init__(self, species, qty, passed_inspection = False):
        super().__init__(species, qty)
        self.passed_inspection = passed_inspection

    def marked_inspection(self):
        if self.passed_inspection == False:
            self.passed_inspection = True
        return self.passed_inspection
