import graphene
from django.db.models import Q
from graphene import ObjectType
from graphene_django import DjangoObjectType
from .models import Orders, Order_products


class OrderType(DjangoObjectType):
    class Meta:
        model = Orders


class Query(graphene.ObjectType):
    orders = graphene.List(
        OrderType,
        customer_id=graphene.Int(),
        created_at=graphene.DateTime,
        updated_at=graphene.DateTime
    )

    def resolve_orders(self, info, customer_id):
        all_orders = Orders.objects.all()
        if orders_id:
            filter = Q(customer_id__contains=customer_id)
            filtered = all_orders.filter(filter)
        return filtered


class addOrder(graphene.Mutation):
    addOrder = graphene.Field(OrderType)

    class Arguments:
        order_id = graphene.Int(required=True)

    def mutate(self, info, order_id, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Não esta logado!")

        order = Orders(
            order_id = order_id
        )
        order.save()

        return addOrder(addOrder=order)


class Order_productType(DjangoObjectType):
    class Meta:
        model = Order_products

# class Query(graphene.ObjectType):
#