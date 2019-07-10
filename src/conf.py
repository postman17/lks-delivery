from .vault import get_apikey

POST_API_RU: dict = {
    'url': 'http://post-api.ru/api/v2/ibc.php?c={city}&s={street}&apikey={apikey}',
    'apikey': get_apikey()
}
# 'ocxk6kh56340ouy5'
POSTPRICE_RU: dict = {
    'url': 'https://postprice.ru/engine/russia/api.php?from={index_from}&to={index_to}&mass={mass}&valuation={val}&vat={vat}',
    'mass': 100,  # Масса отправления, в граммах
    'val': 500,  # Объявленная ценность, в рублях
    'vat': 1  # НДС 20% (1 — с НДС, 0 — без НДС)
}
