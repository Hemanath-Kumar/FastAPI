from fastapi.routing import APIRouter
from schemas.main_page_schemas import MainPageRequestBodySchema, MainPageResponseBodySchema

# router=APIRouter(prefix="/user")
router=APIRouter(prefix="/user")

@router.get("/")
def home():
    return {"message":"Welcome to FastAPI"}


example=[  
            {"Name":"jack"},
            {"Name":"Leo"},
            {"Name":"Lisa"}
        ]


@router.get("/{user_id}",response_model=MainPageResponseBodySchema)
def user(user_id: int):
    if 0 <= user_id < len(example):
        return example[user_id]
    return {"error": "User not found"}


@router.post("/",response_model=MainPageResponseBodySchema)
def create_user(user: MainPageRequestBodySchema):
    example.append(user.dict())
    print(example)
    return user