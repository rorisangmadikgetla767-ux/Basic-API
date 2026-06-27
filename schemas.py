from pydantic import BaseModel, EmailStr

# Request Schemas (data coming in)
# This is what we can expect when someone hits POST/auth/register , They must send an email and a password nothing else 
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Response schemas (data going out)

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    
# What we send back after a successful registration
class TokenResponse(BaseModel):
    access_token: str
    token_type: str
# Request schemas = what the client sends to you
#Response schemas = what you send back to the client