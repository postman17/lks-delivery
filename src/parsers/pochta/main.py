from .cost_calculation import CostCalculation
from .street_to_postal_index import StreetToPostalIndex

from ...conf import (
    POST_API_RU_URL, POST_API_RU_APIKEY, POSTPRICE_RU_URL,
    POSTPRICE_RU_MASS, POSTPRICE_RU_VALUATION, POSTPRICE_RU_VAT)


class MailParser:
    def _street_to_index(self, city, street):
        return StreetToPostalIndex.get_index(
            POST_API_RU_URL, POST_API_RU_APIKEY, city, street)

    def _cost_calculation(self, index_from, index_to):
        return CostCalculation.get_price(
            POSTPRICE_RU_URL, index_from, index_to, POSTPRICE_RU_MASS,
            POSTPRICE_RU_VALUATION, POSTPRICE_RU_VAT)

    @staticmethod
    def get_price(from_city, from_street, to_city, to_street):
        index_from = MailParser()._street_to_index(from_city, from_street)
        index_to = MailParser()._street_to_index(to_city, to_street)
        cost = MailParser()._cost_calculation(index_from, index_to)
        return cost
