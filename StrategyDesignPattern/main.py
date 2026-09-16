from winter_discount import WinterDiscount
from discount_service import DiscountService
from diwali_discount import DiwaliDiscount
from holi_discount import HoliDiscount


holi = HoliDiscount()
diwali = DiwaliDiscount()

ds = DiscountService(holi)
ds.process()

ds.set_strategy(diwali)
ds.process()

ds.set_strategy(WinterDiscount())
ds.process()
