from peewee import CharField, FloatField, ForeignKeyField, IntegerField

from src.infrastructure.shared.repository.peewee.base_model import BaseModel
from src.infrastructure.order.repository.peewee.order_model import OrderModel
from src.infrastructure.product.repository.peewee.product_model import ProductModel


class OrderItemModel(BaseModel):
    id = CharField(primary_key=True)
    order = ForeignKeyField(OrderModel, field='id', backref="order", db_column="order_id")
    product = ForeignKeyField(ProductModel, field='id', backref="product", db_column="product_id")
    quantity = IntegerField(null=False)
    name = CharField(null=False)
    price = FloatField(null=False)

    order_id: str
    product_id: str

    class Meta:
        db_table = 'order_item'