import os
from dotenv import load_dotenv
from app.db.connection import SessionLocal
from app.db.models import User, UserRole
from app.auth.utils import hash_password

#Load environment variables
load_dotenv()

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

db = SessionLocal()
try:
    existing_admin = db.query(User).filter(User.email == ADMIN_EMAIL).first()

    if not existing_admin:
        admin_user = User(
            name="Admin",
            email=ADMIN_EMAIL,
            password_hash=hash_password(ADMIN_PASSWORD),
            role=UserRole.admin
        )
        db.add(admin_user)
        db.commit()
        print(f"Admin user ({ADMIN_EMAIL}) created successfully!")
    else:
        print(f"Admin ({ADMIN_EMAIL}) already exists. Skipping creation.")
except Exception as e:
    db.rollback()
    print("Admin user check note (ignoring):", e)
finally:
    db.close()

