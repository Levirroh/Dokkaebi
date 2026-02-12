from fastapi import APIRouter
from api.v1.endpoints import system, user, agent 

api_router = APIRouter()

# Aqui você registra os módulos
api_router.include_router(system.router, prefix="/system", tags=["System"])
# api_router.include_router(user.router, prefix="/users", tags=["Users"])
# api_router.include_router(agent.router, prefix="/agents", tags=["Agents"])