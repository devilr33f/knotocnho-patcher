import sys
from base64 import b64decode

# @note: keys & endpoints are base64 encoded & reversed to avoid finding the repository by code search

BINARY_PATH = sys.argv[1]
NEW_LICENSE_URL = sys.argv[2].encode()
NEW_PUBLIC_KEY = b64decode('==gCt0SLt0SWFtEIDlETCVFUgQkTF1SLt0SLKIUQRFERJFFdKITavg2LUJkd28WNuFlWDdXN6RmRid0S3c0UwVFSDtWQaVnMlFjcSljZHZVUyYjdZR1SKxUWMl0bYx2VXd0S0ljCLlUUuRUbap0LCNXWuFHOzUWeWFGTW9yRlREN1o3K6dmcvdXe2dGd5dDNxRDUk9SZJF2TrNHVGRXb0c1dONka3oQYxQUNWR3cXJkezIHNzFGWuticvhlNzQ2UQxGZ3lFcrc3KC1US1gjV5J2YV50R3FHcq5USMNGNNdFMVNXa1QTMKYnSOlUYNRGeCN1SkJDcXJmTKl2LptUSpBFaLtSdBlUZxhHUjZVd3UHdLtydy0kRyJTO6hVbVhWeHFnQ4ETMOtiC3QUYhRlN59mYslXM5dmNi9EeqlDWDBzd2pmZ1omeFlUWTRTVpV3Rx52bHl0diZmTxNUe0cUdGdWNBZkQLp2LypgQOtSMmh1a2Z2KUZGUrdHUTVVT1FURRF0QLd2QClUSNFEORF0QPFUQGVUUBJEM3lzRptGaxt2ZC5UQqlkQJlUTK0SLt0SLZV0SgMUSMJUVQBiTJdURC1SLt0SL'[::-1])

ORIGINAL_PUBLIC_KEY = b64decode('==gCt0SLt0SWFtEIDlETCVFUgQkTF1SLt0SLKIUQRFERJFFcKYGd2RXQxU0Y4g0LWtEczInTXFHbz50UyN3ZR9yNzV3S4VzbmhEMV12SYRXMQxETiZTRDBTelZUaxgzYnJVZvFkC3xWdN9UVOdGUDNja5c0biFzLWJmYo92UGNFTPRDdFZUV2sUaYJHb0gGW1l3SrFUYwF1U0F2cBJUMYllVoFjRTpQY5UHZillWjRTYpl2ZCFTcxMUT3dmUWJzb2cDZVZUNo9UUuxUQldkN1o0aPFzdMJmNqJDWlNEUGVXWwhDWmpXSKoFVN5mZjlWWRlHdK5EeCl3UZRGS4pnNUFldld1d4djeyxUcal3Z6RlSaJXaBV3bRtkV3V1aHRkZTxUN2VUVXFjCEdHbrd3cp92U0czc0UlVqlmMFlXN3MnMxJkSjhFaQVTc3VHdZhTVaFUc1pmQhVWayxESVZ1SGpXc3k2UyUXc5ogVPB1UnRWbqx2MRxUSBt0VDNUQvFURRF0QLd2QClUSNFEORF0QPFUQGVUUBJEM3lzRptGaxt2ZC5UQqlkQJlUTK0SLt0SLZV0SgMUSMJUVQBiTJdURC1SLt0SL'[::-1])
ORIGINAL_LICENSE_URL = b64decode('==gM21SeltWL5ZWayVmdts2bv5GajR3bu9SawF2LlZWYj5ybs9yL6MHc0RHa'[::-1])

with open(BINARY_PATH, 'rb') as f:
  content = f.read()

if not ORIGINAL_PUBLIC_KEY in content:
  print('[!] Public key not found!')
  exit(1)

content = content.replace(ORIGINAL_PUBLIC_KEY, NEW_PUBLIC_KEY)
content = content.replace(ORIGINAL_LICENSE_URL, NEW_LICENSE_URL)

with open(BINARY_PATH, 'wb') as f:
  f.write(content)

print('[!] Done!')
