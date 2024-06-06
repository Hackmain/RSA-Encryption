import rsa

# قم بإنشاء مفاتيح 2048 بت (أبطأ ولكن أكثر أمانا من مفاتيح 512 بت)
public_key, private_key = rsa.newkeys(2048)

# الرسالة التي نريد تشفيرها
message = "follow esefkh740_ insta"

# قم بتشفير الرسالة باستخدام المفتاح العام
encrypted_message = rsa.encrypt(message.encode(), public_key)

# يمكن فك التشفير باستخدام المفتاح الخاص
# (تذكر أنه يجب أن يكون لديك المفتاح الخاص لفك التشفير)
decrypted_message = rsa.decrypt(encrypted_message, private_key)

print("encrypted text is:", encrypted_message)
print("decrypted text is:", decrypted_message.decode())
print("private key is :", private_key)
