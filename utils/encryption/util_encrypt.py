import hashlib
from werkzeug.security import generate_password_hash,check_password_hash

'''

Unicode-objects must be encoded before hashing
在哈希之前，必须对unicode对象进行编码

'''

def getSha1(pwd):
    temp = hashlib.sha1(pwd.encode())
    return temp.hexdigest()

def getSaltSha1(pwd):
    temp=generate_password_hash(pwd, method='pbkdf2:sha1:1000', salt_length=6)
    return temp
def checkSaltSha1(pwhash,pwd):
    return check_password_hash(pwhash,pwd)
