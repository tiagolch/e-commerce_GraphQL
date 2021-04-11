# import graphene
# from graphql_auth import mutations
# from graphql_auth.schema import UserQuery, MeQuery
#
#
# class AuthMutation(graphene.ObjectType):
#    register = mutations.Register.Field()
#    verify_account = mutations.VerifyAccount.Field()
#    token_auth = mutations.ObtainJSONWebToken.Field()
#    update_account = mutations.UpdateAccount.Field()
#    resend_activation_email = mutations.ResendActivationEmail.Field()
#    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
#    password_reset = mutations.PasswordReset.Field()
#    password_change = mutations.PasswordChange.Field()
#
#
# class Query(UserQuery, MeQuery, graphene.ObjectType):
#     pass
#
#
# class Mutation(AuthMutation, graphene.ObjectType):
#    pass
#
#
# schema = graphene.Schema(query=Query, mutation=Mutation)

import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import User


class UserNode(DjangoObjectType):
   class Meta:
      model = User
      filter_fields = ['name']
      interfaces = (relay.Node,)


class Query(graphene.ObjectType):
   user = relay.Node.Field(UserNode)
   all_users = DjangoFilterConnectionField(UserNode)
