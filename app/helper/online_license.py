import sys
from app import config
import time
from keygen_licensing_tools import validate_license_key_online, ValidationError

def is_valid():
    try:
        out = validate_license_key_online(
            account_id="abf30c52-0059-4d37-ae05-639b7bc1a78c", key=config['Key']
        )

        if out.code == 'VALID':
            return True
    except ValidationError as e:
        print(f"Error: Invalid license ({e.code}). Exiting.")
        time.sleep(50)
        sys.exit(1)
