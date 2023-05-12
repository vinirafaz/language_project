from fastapi import APIRouter

from routes import auth, customer, notes

router = APIRouter()

router.include_router(auth.auth)
router.include_router(customer.customer)
router.include_router(notes.notes)
