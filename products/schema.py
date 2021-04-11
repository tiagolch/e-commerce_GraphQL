import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Products


class ProductNode(DjangoObjectType):
    class Meta:
        model = Products
        filter_fields = ['name', 'price']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    product = relay.Node.Field(ProductNode)
    all_products = DjangoFilterConnectionField(ProductNode)
