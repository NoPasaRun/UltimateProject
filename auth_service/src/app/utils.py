import jwt
import pytz
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import User


def get_user_role(user: User) -> str:
    if user.is_superuser:
        return 'Admin'
    elif user.is_staff:
        return 'Moderator'
    elif user.groups.filter(name='Organizer').exists():
        return 'Organizer'
    else:
        return 'User'


def create_jwt_token(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_active': user.is_active,
        'date_joined': user.date_joined.isoformat(),
        'exp': datetime.now(tz=pytz.UTC) + timedelta(days=1),
        'iat': datetime.now(tz=pytz.UTC),
        'role': get_user_role(user)
    }

    token = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
    return token


def decode_jwt_token(token):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception('Token has expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')