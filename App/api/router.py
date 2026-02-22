from fastapi import APIRouter

from App.api.endpoints import agent_ep, auth_ep, brain_ep, master_ep, system_ep


api_router = APIRouter()

# Aqui você registra os módulos
api_router.include_router(system_ep.router, prefix="/system", tags=["System"])
api_router.include_router(auth_ep.router, prefix="/auth", tags=["Auth"])
api_router.include_router(brain_ep.router, prefix="/brain", tags=["Brain"])
api_router.include_router(master_ep.router, prefix="/master", tags=["Master"])
api_router.include_router(agent_ep.router, prefix="/agents", tags=["Agents"])