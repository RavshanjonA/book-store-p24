from functools import wraps

from django.shortcuts import get_object_or_404

from book.models import BookGenre


def is_owner_permission(f):
    @wraps(f)
    def wrapped(self, *args, **f_kwargs):
            reqeust_user= args[1].context.user
            genre = get_object_or_404(BookGenre, id = f_kwargs.get('id'))
            if genre.owner!=reqeust_user:
                raise Exception("You don't have permission for this action")
            return f(self, *args, **f_kwargs)
    return wrapped