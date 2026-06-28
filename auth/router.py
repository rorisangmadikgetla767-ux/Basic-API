from fastapi import APIRouter, HTTPException, status
from database import get_connection
from schemas import UserRegister, UserLogin, UserResponse, TokenResponse
from auth.utils import hash_password, verify_password, create_access_token

router = APIRouter
@router.post("/register", response_model=UserResponse)
def register(user: UserRegister):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        hashed = hash_password(user.password)
        cursor.execute(
           "INSERT INTO users(email, hashed_password) VALUES (%s, %s) RETURNING id, email, is_active",
           (user.email, hashed)
        )
        new_user = cursor.fetchone()
        conn.commit()
        return {
            "id": new_user[0],
            "email": new_user[1],
            "is_active": new_user[2]
        }
    except Exception as e:
        conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    finally:
        cursor.close()
        conn.close()
@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT email, hashed_password FROM users WHERE email = %s",
                       (user.email,)
        )
        db_user = cursor.fetchone()
        
        if db_user is None or not verify_password(user.password, db_user[1]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        token = create_access_token(data={"sub": db_user[0]})
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    finally:
        cursor.close()
        conn.close()
