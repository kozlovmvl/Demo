from django.contrib.admin.views.decorators import staff_member_required
from ninja import NinjaAPI

from users.barrier import TokenBarrier

api = NinjaAPI(auth=TokenBarrier(), docs_decorator=staff_member_required)

api.add_router("/posts/", "posts.api.router")
api.add_router("/users/", "users.api.router")
