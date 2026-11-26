from fastapi import APIRouter

router_users = APIRouter()

@router_users.post('/create')
def create_user():
    return 1111