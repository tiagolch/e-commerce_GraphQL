import graphene
import customers.schema
import orders.schema
import products.schema


class Query(customers.schema.Query,
            orders.schema.Query,
            products.schema.Query,
            graphene.ObjectType
            ):
    pass


schema = graphene.Schema(query=Query)
