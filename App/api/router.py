from fastapi import APIRouter

from api.endpoints import agent_ep, auth_ep, brain_ep, master_ep, system_ep


api_router = APIRouter()

# Aqui você registra os módulos
api_router.include_router(system_ep.router, tags=["System"])
api_router.include_router(auth_ep.router, tags=["Auth"])
api_router.include_router(brain_ep.router, tags=["Brain"])
api_router.include_router(master_ep.router, tags=["Master"])
api_router.include_router(agent_ep.router, tags=["Agents"])