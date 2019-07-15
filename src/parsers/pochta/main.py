from .cost_calculation import CostCalculation
from .street_to_postal_index import StreetToPostalIndex

from src.conf import POST_API_RU, POSTPRICE_RU


class MailParser:  # TODO road to component
    def street_to_index(self, city: str, street: str):
        return StreetToPostalIndex.output(
            POST_API_RU, city, street
        )

    def cost_calculation(self, index_from: int, index_to: int):
        POSTPRICE_RU['index_from'] = index_from
        POSTPRICE_RU['index_to'] = index_to
        return CostCalculation.output(POSTPRICE_RU)

    @staticmethod
    def get_price(from_city: str, from_street: str, to_city: str, to_street: str):
        index_from = MailParser().street_to_index(from_city, from_street)
        index_to = MailParser().street_to_index(to_city, to_street)
        cost = MailParser().cost_calculation(index_from, index_to)
        return cost
