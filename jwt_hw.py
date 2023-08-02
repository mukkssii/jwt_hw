import jwt
import datetime

from jwt import ExpiredSignatureError


def encode_token(payload_dict: dict):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
        'iat': datetime.datetime.utcnow(),
    }
    payload.update(payload_dict)
    encode_jwt = jwt.encode(
        payload=payload,
        key='secret',
        algorithm='HS256',
    )
    return encode_jwt


def decode_token(token_jwt: str):
    try:
        decoded = jwt.decode(
            token_jwt,
            'secret',
            algorithms=['HS256'],
        )
    except Exception:
        return 'kaput'
    return decoded


info_dictionary = {
    'name': 'Donald',
    'last_name': 'Obama',
    'age': 999,
    'address': 'deribasovska 2068',
}

token = encode_token(payload_dict=info_dictionary)
res = decode_token(token)
print(res)
