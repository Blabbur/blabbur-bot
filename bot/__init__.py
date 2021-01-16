from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from bot.schema import Mutation, Query

endpoint = HTTPEndpoint("http://localhost:3200/")


class ApiException(Exception):
    pass


def do_op(op, token=None):
    headers = None
    if token is not None:
        headers = {"Authorization": token}
    json_response = endpoint(op, extra_headers=headers)
    if "errors" in json_response:
        raise ApiException(json_response["errors"])
    response = op + json_response
    return response


class User:
    DEFAULT_PASSWORD = "dumb_password"

    def __init__(self, token):
        self.token = token
        self.data = self.get_user_data()


    @staticmethod
    def signup(first, last, handle):
        op = Operation(Mutation)
        signup = op.signup(firstname=first,
                           lastname=last,
                           handle=handle,
                           email=handle + "@gmail.com",
                           password=User.DEFAULT_PASSWORD)
        signup.token()

        response = do_op(op)

        return User(response.signup.token)

    def get_user_data(self):
        op = Operation(Query)
        op.me()
        op.me.firstname()
        op.me.lastname()
        op.me.handle()
        response = do_op(op, token=self.token)
        return response.me

    def __repr__(self):
        return repr(self.data)

