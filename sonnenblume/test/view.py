from fastapi import APIRouter

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def check_health():
    return {"health_check": "ok"}
