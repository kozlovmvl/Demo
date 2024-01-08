from ninja import Router, Form
from posts.models import Post

from posts.scheme import ListPostsResponse, PostOutSchema, PostInputSchema, ErrorSchema

router = Router()

@router.post("/list/", response=ListPostsResponse)
def list_posts(request):
    qs = Post.objects.order_by("id")
    return {"posts": qs}


@router.post("/create/", response={"200": PostOutSchema, "400": ErrorSchema})
def create_post(request, data: Form[PostInputSchema]):
    pass
