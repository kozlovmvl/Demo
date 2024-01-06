from ninja import File, Form, Router
from ninja.files import UploadedFile
from ninja.errors import AuthenticationError

from .models import User
from .scheme import LoginOutSchema, LoginInputSchema, UserProfileSchema, UserInputSchema

router = Router()

@router.post("/login/", response=LoginOutSchema, auth=None)
def login(request, data: LoginInputSchema):
    user = User.objects.get(username=data.username)
    if user.check_password(data.password):
        user.set_token()
        return 200, LoginOutSchema(token=user.token)
    raise AuthenticationError


@router.post("/@/", response=UserProfileSchema)
def get_user(request):
    return User.objects.get(id=request.auth["id"])


@router.post("/update/", response=UserProfileSchema)
def update_user(request, data: Form[UserInputSchema], photo: File[UploadedFile]):
    user = User.objects.get(id=request.auth["id"])
    for key, value in data.dict().items():
        if value is not None:
            setattr(user, key, value)
    if photo:
        user.photo = photo
    user.save()
    return user
    
