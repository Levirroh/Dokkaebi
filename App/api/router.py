from fastapi import APIRouter

from App.api.endpoints import agent_ep, system_ep


api_router = APIRouter()

# Aqui você registra os módulos
# api_router.include_router(system_ep.router, prefix="/system", tags=["System"])
api_router.include_router(agent_ep.router, prefix="/agents", tags=["Agents"])