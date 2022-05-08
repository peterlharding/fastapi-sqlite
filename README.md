

* https://nitratine.net/blog/post/how-to-hash-passwords-in-python/


# Managing Passwords

```
import hashlib
import os

salt     = os.urandom(32) # Remember this
password = 'secret'

key = hashlib.pbkdf2_hmac(
    'sha256',                 # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt,                     # Provide the salt
    100000                    # It is recommended to use at least 100,000 iterations of SHA-256 
)
```

```
import hashlib
import os

salt = os.urandom(32) # Remember this
password = 'secret'

key = hashlib.pbkdf2_hmac(
    'sha256',                 # The hash digest algorithm for HMAC
    password.encode('utf-8'), # Convert the password to bytes
    salt,                     # Provide the salt
    100000,                   # It is recommended to use at least 100,000 iterations of SHA-256 
    dklen=128                 # Get a 128 byte key
)
```

```
import os
import hashlib

# Example generation
salt = os.urandom(32)
key  = hashlib.pbkdf2_hmac('sha256', 'secret'.encode('utf-8'), salt, 100000)

# Store them as:
hash = salt + key 

# Getting the values back out
salt_from_hash = hash[:32] # 32 is the length of the salt
key_from_hash  = hash[32:]
```

```
import hashlib

salt = b'...'  # Get the salt you stored for *this* user
key  = b'...'  # Get this users key calculated

password_to_check = 'secret' # The password provided by the user to check

# Use the exact same setup you used to generate the key, but this time put in the password to check
new_key = hashlib.pbkdf2_hmac(
    'sha256',
    password_to_check.encode('utf-8'), # Convert the password to bytes
    salt, 
    100000
)

if new_key == key:
    print('Password is correct')
else:
    print('Password is incorrect')

```

