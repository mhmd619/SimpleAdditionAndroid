مشروع Simple Addition لبناء Android APK باستخدام GitHub Actions

الصفحة الخاصة بمستودعك:
https://github.com/mhmd619/SimpleAdditionAndroid

1) افتح ملف ZIP وفك الضغط، ثم افتح مجلد SimpleAddition_GitHub_V6.
2) في مستودع GitHub اضغط uploading an existing file من صفحة Code إذا كان فارغاً.
3) ارفع محتويات المجلد وليس ملف ZIP، مع التأكد من رفع مجلد .github الخفي.
4) اضغط Commit changes.
5) افتح Actions > Build Simple Addition APK > Run workflow عند الحاجة.
6) عندما تظهر إشارة نجاح، افتح التشغيل ونزل SimpleAddition-APK من Artifacts.
7) فك ضغط Artifact للوصول إلى ملف .apk ثم انسخه إلى الهاتف وثبته.

إذا لم يتم رفع مجلد .github قم بإنشاء ملف على GitHub باسم:
.github/workflows/build-apk.yml
وانسخ نصه من الملف الموجود في هذا المشروع.

تذكير: هذه الحزمة تحتوي كود المشروع وليست APK جاهزاً.
إنشاء APK يتطلب نجاح عملية البناء على GitHub.
