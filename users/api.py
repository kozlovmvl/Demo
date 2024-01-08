import logging
from ninja import Form, Router
from ninja.errors import AuthenticationError

from .models import User, City
from .scheme import LoginOutSchema, LoginInputSchema, UserProfileSchema, UserInputSchema

logger = logging.getLogger("debug")
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
def update_user(request, data: Form[UserInputSchema]):
    user = User.objects.get(id=request.auth["id"])
    for key, value in data.dict().items():
        if value:
            match key:
                case "country":
                    setattr(user, key + "_id", value)
                case "city":
                    user.city.set(City.objects.filter(id__in=value))
                case _:
                    setattr(user, key, value)
    user.save()
    return user
    
