from typing import List
from ninja import Router, Form
from posts.models import Post

from posts.scheme import PostOutSchema, PostInputSchema, ErrorSchema

router = Router()

@router.post("/list/", response=List[PostOutSchema])
def list_posts(request):
    qs = Post.objects.order_by("id")
    return list(qs)


@router.post("/create/", response={"200": PostOutSchema, "400": ErrorSchema})
def create_post(request, data: Form[PostInputSchema]):
    pass
