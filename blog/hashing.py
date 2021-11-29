from passlib.context import CryptContext
pass_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hash():
    def bcrypt(password: str):
        passw_hash = pass_cxt.hash(password)
        return passw_hash