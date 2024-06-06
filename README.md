# RSA-Encryption


 دعوني أشرح الكود للمبتدئين:

إنشاء مفاتيح RSA:
نستخدم مكتبة rsa في Python لإنشاء مفاتيح عامة وخاصة.
السطر التالي ينشئ مفاتيح بطول 2048 بت:
Python

public_key, private_key = rsa.newkeys(2048)
AI-generated code. Review and use carefully. More info on FAQ.
يُفضل استخدام مفاتيح طويلة لزيادة الأمان.
تشفير وفك تشفير الرسالة:
نفترض أن لدينا رسالة نريد تشفيرها وفك تشفيرها.
الرسالة المُشفرة تُنشأ باستخدام المفتاح العام:
Python

message = "follow esefkh740_ insta"
encrypted_message = rsa.encrypt(message.encode(), public_key)
AI-generated code. Review and use carefully. More info on FAQ.
يمكن فك التشفير باستخدام المفتاح الخاص:
Python

decrypted_message = rsa.decrypt(encrypted_message, private_key)
AI-generated code. Review and use carefully. More info on FAQ.
النتائج:
ستظهر الرسالة المشفرة والرسالة المفككة في النتائج.
يجب أن تكون لديك المفتاح الخاص لفك التشفير.
ملاحظة: يُفضل عدم استخدام هذا النوع من التشفير لتشفير كميات كبيرة من البيانات. يُستخدم عادةً لتبادل المفاتيح وتأمين الاتصالات الآمنة.
