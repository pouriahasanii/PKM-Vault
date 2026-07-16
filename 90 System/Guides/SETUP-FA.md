# راه‌اندازی کامل و مرحله‌به‌مرحله PKM-Vault

## هدف این راهنما

این راهنما Vault را از مرحله Clone تا اولین Capture، Daily Note و Commit راه‌اندازی می‌کند. هر مرحله یک «نقطه کنترل» دارد. اگر خروجی شما با نقطه کنترل متفاوت بود، ادامه ندهید و تصویر خطا یا صفحه تنظیمات را ارسال کنید.

## مرحله صفر: مواردی که فعلاً نباید اجرا شوند

تا پایان تست پایه، این موارد را فعال نکنید:

- Logseq روی Vault اصلی
- Telegram Bot
- اسکریپت مهاجرت Vault قدیمی
- Obsidian Git
- Syncthing
- اتوماسیون زمان‌بندی‌شده
- انتقال تمام PDFها و تصاویر قدیمی

## مرحله ۱: کنترل مسیر Repository

GitHub Desktop را باز کنید و Repository زیر را انتخاب کنید:

```text
pouriahasanii/PKM-Vault
```

روی **Show in Explorer** کلیک کنید. مسیر پیشنهادی:

```text
C:\PKM\PKM-Vault
```

فایل‌ها و پوشه‌های زیر باید مستقیماً در همین مسیر باشند:

```text
00 Inbox
10 Projects
20 Areas
30 Resources
40 Zettelkasten
50 Visual Lab
60 Journal
70 Maps of Content
80 Archive
90 System
assets
logseq
.obsidian
.gitignore
README.md
ARCHITECTURE.md
```

نباید این حالت را ببینید:

```text
C:\PKM\PKM-Vault\PKM-Vault-v2\00 Inbox
```

### نقطه کنترل ۱

در GitHub Desktop باید وضعیت `No local changes` دیده شود و مسیر Repository همان پوشه حاوی `00 Inbox` باشد.

## مرحله ۲: گرفتن بکاپ اولیه

قبل از اولین اجرا، پوشه Repository را در یک محل جدا ZIP کنید. فایل ZIP را داخل خود Repository نگذارید.

نمونه:

```text
C:\PKM-Backups\PKM-Vault-before-Obsidian.zip
```

## مرحله ۳: بازکردن Vault در Obsidian

1. Obsidian را اجرا کنید.
2. اگر صفحه انتخاب Vault باز شد، **Open folder as vault** را بزنید.
3. مسیر زیر را انتخاب کنید:

```text
C:\PKM\PKM-Vault
```

4. روی **Select Folder** کلیک کنید.
5. اگر درباره Trust سؤال شد، پس از بررسی مسیر آن را تأیید کنید.

### نقطه کنترل ۲

در File Explorer داخلی Obsidian باید پوشه‌های `00 Inbox` تا `90 System` را ببینید. اگر فقط یک پوشه `PKM-Vault-v2` دیده می‌شود، پوشه اشتباه را باز کرده‌اید.

## مرحله ۴: کنترل تنظیمات پایه Obsidian

مسیر زیر را باز کنید:

```text
Settings → Files and links
```

مقادیر باید چنین باشند:

```text
Default location for new notes: In the folder specified below
Folder to create new notes in: 00 Inbox
Default location for new attachments: In the folder specified below
Attachment folder path: assets
Automatically update internal links: Enabled
```

اگر مقادیر از فایل `.obsidian/app.json` بارگذاری شده باشند، فقط آن‌ها را کنترل کنید.

## مرحله ۵: فعال‌سازی Core Plugins

وارد شوید:

```text
Settings → Core plugins
```

این موارد را فعال کنید:

- Daily notes
- Templates
- Canvas
- Properties view
- Bookmarks
- Command palette
- File recovery

### تنظیم Templates

```text
Settings → Templates
Template folder location: 90 System/Templates
```

### تنظیم Daily Notes

```text
Settings → Daily notes
Date format: YYYY-MM-DD
New file location: 60 Journal/Daily
Template file location: 90 System/Templates/Daily Note
```

### نقطه کنترل ۳

هیچ کدام از مسیرها نباید قرمز یا با پیام `Folder not found` نمایش داده شوند.

## مرحله ۶: نصب Community Plugins

وارد شوید:

```text
Settings → Community plugins
```

در صورت نمایش Restricted Mode، فقط برای همین Vault شناخته‌شده آن را غیرفعال کنید. سپس افزونه‌ها را یکی‌یکی نصب و Enable کنید:

1. Dataview
2. Templater
3. QuickAdd
4. Excalidraw

فعلاً نصب نکنید:

- Obsidian Git
- افزونه‌های Sync دیگر
- افزونه‌های AI ناشناس
- مجموعه بزرگی از Theme و Plugin

## مرحله ۷: تنظیم Templater

```text
Settings → Templater
Template folder location: 90 System/Templates
```

گزینه اجرای JavaScript یا Shell Command را فعلاً فعال نکنید.

قالب‌ها:

```text
Daily Note.md
Permanent Note.md
Project.md
Universal Capture.md
```

### نقطه کنترل ۴

از Command Palette دستور زیر را پیدا کنید:

```text
Templater: Open Insert Template modal
```

و مطمئن شوید چهار قالب بالا نمایش داده می‌شوند.

## مرحله ۸: آزمایش Daily Note

از نوار کناری یا Command Palette دستور زیر را اجرا کنید:

```text
Daily notes: Open today's daily note
```

باید فایلی مانند این ساخته شود:

```text
60 Journal/Daily/2026-07-15.md
```

محتوای مورد انتظار:

- YAML Frontmatter
- عنوان تاریخ
- Focus
- Captures
- Decisions
- Review

### خطاهای رایج Daily Note

#### فایل بدون قالب ساخته شد

مسیر Template را دوباره کنترل کنید:

```text
90 System/Templates/Daily Note
```

#### تاریخ داخل متن تبدیل نشد

Core Templates و Templater را هم‌زمان بررسی کنید. برای Daily Note فعلی، Core Templates کافی است. Obsidian را یک‌بار بسته و باز کنید.

#### فایل در پوشه اشتباه ساخته شد

در Daily Notes، New file location را روی این مسیر قرار دهید:

```text
60 Journal/Daily
```

## مرحله ۹: آزمایش Universal Capture

1. روی `00 Inbox` راست‌کلیک کنید.
2. **New note** را بزنید.
3. نام نوت را وارد کنید:

```text
آزمایش اولین ورودی
```

4. قالب `Universal Capture` را با Templater وارد کنید.
5. عنوان و محتوا را کامل کنید.

نمونه:

```markdown
# آزمایش اولین ورودی

## Summary

این اولین Capture آزمایشی سیستم است.

## Content

هدف، بررسی مسیر Inbox و قالب است.

## References

## Related Notes
```

### نقطه کنترل ۵

فایل باید داخل `00 Inbox` باشد و Properties زیر را داشته باشد:

```text
type: capture
status: inbox
source: manual
summary_level: 0
```

## مرحله ۱۰: آزمایش Dataview

فایل زیر را باز کنید:

```text
00 Inbox/_Inbox Dashboard.md
```

پس از فعال‌شدن Dataview باید یک جدول نمایش داده شود و نوت آزمایشی را نشان دهد.

اگر به‌جای جدول فقط کد می‌بینید:

1. Dataview را Enable کنید.
2. حالت Reading View را امتحان کنید.
3. Obsidian را Reload کنید.

## مرحله ۱۱: آزمایش Visual Lab

این فایل را باز کنید:

```text
50 Visual Lab/Projects/EXAMPLE-PKM/01 Visual Index.md
```

دیاگرام Mermaid باید نمایش داده شود. سپس از فایل زیر به پروژه اصلی بروید:

```text
50 Visual Lab/Projects/EXAMPLE-PKM/00 Brief.md
```

لینک باید این فایل را باز کند:

```text
10 Projects/EXAMPLE-PKM - Example Project.md
```

### نقطه کنترل ۶

- Mermaid نمایش داده می‌شود.
- لینک پروژه باز می‌شود.
- فایل Decisions قابل دسترسی است.

## مرحله ۱۲: اجرای اعتبارسنجی Python

CMD را باز کنید:

```cmd
cd /d "C:\PKM\PKM-Vault"
py "90 System\Scripts\validate_vault.py"
```

خروجی مورد انتظار:

```text
Vault validation passed: 15 unique note IDs
```

پس از ایجاد نوت‌های جدید ممکن است عدد بزرگ‌تر شود. مهم این است که پیام Duplicate ID یا Token نمایش داده نشود.

اگر دستور `py` شناخته نشد، Python را از سایت رسمی نصب کنید و گزینه Add Python to PATH را فعال کنید.

## مرحله ۱۳: کنترل امنیت پیش از Commit

GitHub Desktop را باز کنید و تمام Changed Files را مرور کنید.

این فایل‌ها نباید دیده شوند:

```text
.env
API-TOKEN.md
*.log
*.sqlite
assets/*.pdf
assets/*.png
.obsidian/workspace.json
```

این فایل‌ها می‌توانند دیده شوند:

```text
.env.example
نوت‌های Markdown جدید
تنظیمات portable در .obsidian
Templates
Scripts
```

## مرحله ۱۴: اولین Commit آزمایشی

در GitHub Desktop:

```text
Summary: Test Obsidian vault setup
Description: Verify Daily Note, Universal Capture, Dataview and Visual Lab
```

سپس:

1. **Commit to main**
2. **Push origin**

### نقطه کنترل ۷

بعد از Push، GitHub Desktop باید `No local changes` نشان دهد. در سایت GitHub نیز Daily Note و Capture آزمایشی باید دیده شوند، ولی فایل‌های `assets` و `.env` نباید وجود داشته باشند.

## مرحله ۱۵: روتین روزانه پیشنهادی

### هنگام Capture

فقط ذخیره کنید:

```text
مطلب جدید → 00 Inbox → status: inbox
```

### مرور روزانه

حداکثر ۳ تا ۵ نوت را بررسی کنید:

```text
بی‌ارزش → حذف
فعلاً نامشخص → باقی‌ماندن در Inbox
وابسته به خروجی → اتصال/انتقال به Project
مسئولیت دائمی → Area
مرجع → Resource
بینش مستقل → Permanent Note
قدیمی → Archive
```

### پایان روز

1. Daily Note را تکمیل کنید.
2. GitHub Desktop را باز کنید.
3. Changed Files را مرور کنید.
4. Commit کوتاه و مشخص بسازید.
5. Push کنید.

## مرحله ۱۶: ساخت پروژه واقعی

1. قالب Project را در `10 Projects` اعمال کنید.
2. یک `project_id` کوتاه و یکتا انتخاب کنید:

```text
WEBSITE-01
PKM-02
CONTENT-03
```

3. پوشه متناظر بسازید:

```text
50 Visual Lab/Projects/WEBSITE-01
```

4. فایل‌های زیر را از مثال کپی و متناسب با پروژه ویرایش کنید:

```text
00 Brief.md
01 Visual Index.md
02 Decisions.md
```

5. همه فایل‌ها باید `project_id` یکسان داشته باشند.

## مرحله ۱۷: بکاپ فایل‌های Assets

چون `assets` وارد Git نمی‌شود، یک روش جدا لازم است. پیشنهاد اولیه:

```text
C:\PKM\PKM-Vault\assets
↓ بکاپ زمان‌بندی‌شده
OneDrive\PKM-Backups\assets
```

بکاپ را طوری تنظیم کنید که حذف اشتباه فوراً تنها نسخه فایل را از بین نبرد. ترجیحاً از ZIP تاریخ‌دار یا Version History استفاده کنید.

## مرحله ۱۸: مهاجرت Vault قدیمی — فعلاً فقط آزمایشی

پیش از مهاجرت واقعی، اسکریپت را روی یک کپی کوچک شامل ۵ تا ۱۰ فایل Markdown آزمایش کنید:

```cmd
cd /d "C:\PKM\PKM-Vault"
py "90 System\Scripts\migrate_notes.py" "C:\Path\To\Small-Test-Folder"
```

خروجی وارد این مسیر می‌شود:

```text
00 Inbox/Imports/YYYY-MM-DD
```

محدودیت نسخه فعلی:

- فقط Markdown منتقل می‌شود.
- Attachmentها منتقل نمی‌شوند.
- تشخیص تکراری فعلاً در batch همان روز انجام می‌شود.

بنابراین برای Vault اصلی تا آماده‌شدن نسخه اصلاح‌شده مهاجرت کامل انجام ندهید.

## مرحله ۱۹: Logseq — توقف کنترل‌شده

ساختار فعلی هنوز برای بازکردن مستقیم به‌عنوان Graph اصلی Logseq نهایی نشده است. Logseq ممکن است پوشه‌های `pages` و `journals` بسازد.

فعلاً:

1. Vault را در Logseq باز نکنید.
2. ابتدا Obsidian را حداقل یک هفته پایدار کنید.
3. برای Logseq یک Clone یا Branch آزمایشی بسازید.
4. بعد از اصلاح معماری Logseq، تست دوطرفه انجام دهید.

## چک‌لیست نهایی راه‌اندازی

- [ ] Repository در `C:\PKM\PKM-Vault` قرار دارد.
- [ ] Obsidian همان پوشه را به‌عنوان Vault باز کرده است.
- [ ] Daily Notes فعال و مسیر آن صحیح است.
- [ ] Templates فعال و مسیر آن صحیح است.
- [ ] Dataview، Templater، QuickAdd و Excalidraw فعال‌اند.
- [ ] Daily Note آزمایشی ساخته شده است.
- [ ] Universal Capture آزمایشی ساخته شده است.
- [ ] Inbox Dashboard نوت آزمایشی را نشان می‌دهد.
- [ ] Visual Lab و لینک پروژه سالم‌اند.
- [ ] `validate_vault.py` بدون خطا اجرا شده است.
- [ ] `.env` و `assets` در GitHub Desktop دیده نمی‌شوند.
- [ ] Commit و Push موفق انجام شده است.
- [ ] Logseq و مهاجرت اصلی هنوز اجرا نشده‌اند.

## اطلاعات لازم هنگام گزارش خطا

اگر خطایی رخ داد، این موارد را ارسال کنید:

1. شماره مرحله این راهنما
2. متن دقیق خطا
3. تصویر کامل پنجره
4. مسیری که در آن هستید
5. کاری که درست قبل از خطا انجام دادید
6. نسخه Obsidian یا Python، اگر مرتبط است

اطلاعات محرمانه مانند Token، API Key، فایل `.env` یا رمز حساب را در تصویر و پیام قرار ندهید.
