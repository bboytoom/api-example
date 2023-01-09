import functools
from src.models.User import User
from src.models.Information import Information


def parameters_user(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        uuid = kwargs.get('user_uuid', None)

        if uuid is None:
            return func(self, uuid)

        user_uuid = User.query.filter_by(uuid=uuid).first_or_404()
        return func(self, user_uuid)

    wrapper.__name__ = func.__name__

    return wrapper


def parameters_user_information(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        user_uuid = Information.query \
            .filter_by(user_uuid=kwargs.get('user_uuid', None)) \
            .first_or_404()

        return func(self, user_uuid)

    wrapper.__name__ = func.__name__

    return wrapper
