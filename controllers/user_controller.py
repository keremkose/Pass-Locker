from fastapi.routing import APIRouter

router=APIRouter("/user") 

router.get("")
def get_user():
    pass