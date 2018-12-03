from cryptography.fernet import Fernet
import sys

#key = sys.argv[1].encode('utf8')
key = b'jAwkb31NFUkcPQ1TpP6aMyIh1VQSdbwemuxGIStzQRs='
fernet = Fernet(key)

token = fernet.encrypt(b"secret")
print(token)
decrypt = fernet.decrypt(token)
print(decrypt)