from django.conf import settings
import jwt
from ninja.security import APIKeyHeader


class TokenBarrier(APIKeyHeader):
    param_name = "Authorization"

    def authenticate(self, request, token):
        if token:
            return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

