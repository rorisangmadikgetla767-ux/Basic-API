from fastapi import APIRouter, Depends, HTTPException, status
from database import get_connection
from auth.dependencies import get_current_user

router = APIRouter()

@router.get("/me")
def get_me(current_user: str = Depends(get_current_user)):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "SELECT id, email, is_active, created_at FROM users WHERE email = %s",
            (current_user,)
        )
        user = cursor.fetchone()
        
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return {
            "id": user[0],
            "email": user[1],
            "is_active": user[2],
            "created_at": str(user[3])
        }
    finally:
        cursor.close()
        conn.close()