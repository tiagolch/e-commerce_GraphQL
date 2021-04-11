import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from products.models import Products
from .models import Orders, Order_products


class OrderNode(DjangoObjectType):
    class Meta:
        model = Orders
        filter_fields = ['customer_id']
        interfaces = (relay.Node,)


class OrderProductsNode(DjangoObjectType):
    class Meta:
        model = Order_products
        filter_fields = {
            'product': ['exact'],
            'order_id': ['exact'],
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    order = relay.Node.Field(OrderNode)
    all_orders = DjangoFilterConnectionField(OrderNode)

    orderProduct = relay.Node.Field(OrderProductsNode)
    all_orderProducts = DjangoFilterConnectionField(OrderProductsNode)