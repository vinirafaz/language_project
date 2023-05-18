from fastapi import APIRouter

from routes import auth, customer, notes

router = APIRouter(prefix="/api/v1")

router.include_router(auth.auth)
router.include_router(customer.customer)
router.include_router(notes.notes)
