from typing import Tuple, Union

from . import models


# Register your services here
def add_user(tg_id: int, username: str) -> Tuple[models.User, bool]:
    return models.User.objects.get_or_create(
        tg_id=tg_id, username=username
    )
