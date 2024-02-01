from fastapi import APIRouter
from src.adapter.spi.api.router.health_check_router import router as HealthCheck
from src.adapter.spi.api.router.auth_router import router as AuthRouter
from src.adapter.spi.api.router.customer_router import router as CustomerRouter
from src.adapter.spi.api.router.product_router import router as ProducRouter
from src.adapter.spi.api.router.order_router import router as OrderRouter


api_router = APIRouter()
api_router.include_router(HealthCheck, prefix='/health', tags=["healthCheck"])
api_router.include_router(AuthRouter, prefix='/auth', tags=["auth"])
api_router.include_router(CustomerRouter, prefix='/customers', tags=["customers"])
api_router.include_router(ProducRouter, prefix='/products', tags=["products"])
api_router.include_router(OrderRouter, prefix='/orders', tags=["orders"])
