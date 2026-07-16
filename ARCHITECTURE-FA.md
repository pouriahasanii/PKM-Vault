# معماری جامع سیستم مدیریت دانش شخصی PKM-Vault

## خلاصه مدیریتی

`PKM-Vault` یک سیستم مدیریت دانش شخصی محلی، مبتنی بر Markdown و آماده نسخه‌بندی با Git است. Obsidian محیط اصلی کار روزمره است؛ GitHub تاریخچه تغییرات و نسخه پشتیبان نوت‌های متنی را نگه می‌دارد؛ فایل‌های حجیم در `assets` قرار می‌گیرند و جداگانه پشتیبان‌گیری می‌شوند. Logseq در وضعیت فعلی فقط یک قابلیت آینده و آزمایشی است و تا اصلاح لایه سازگاری نباید روی Vault اصلی فعال شود.

این معماری چند روش معتبر را ترکیب می‌کند:

- **PARA:** تفکیک پروژه‌ها، مسئولیت‌های دائمی، منابع و آرشیو
- **Johnny Decimal:** شماره‌گذاری پایدار پوشه‌ها
- **Zettelkasten:** تبدیل اطلاعات مهم به نوت‌های اتمی و ماندگار
- **LATCH:** ساخت نماها بر اساس مکان، الفبا، زمان، دسته‌بندی و سلسله‌مراتب
- **Progressive Summarization:** خلاصه‌سازی تدریجی به‌جای پردازش سنگین در لحظه ورود
- **Atomic Notes:** نگهداری هر ایده مستقل در یک نوت مشخص

## نقش هر فناوری

| فناوری | نقش اصلی | نباید برای چه کاری استفاده شود؟ |
|---|---|---|
| Obsidian | نوشتن، لینک‌سازی و مرور دانش | همگام‌سازی Git هم‌زمان با چند افزونه |
| Git | نگهداری تاریخچه تغییرات | همگام‌سازی لحظه‌ای دستگاه‌ها |
| GitHub Private | نسخه پشتیبان نوت‌ها و تنظیمات غیرمحرمانه | نگهداری Token و فایل‌های حجیم |
| GitHub Desktop | Commit و Push ساده و کنترل‌شده | اجرای هم‌زمان با Obsidian Git |
| `assets` | نگهداری PDF، تصویر، صوت و ویدئو | ثبت مستقیم در تاریخچه عادی Git |
| Logseq | رابط بلوکی آینده | استفاده هم‌زمان پیش از تکمیل سازگاری |

## ساختار کامل پوشه‌ها

```text
PKM-Vault/
├── 00 Inbox/
│   ├── Imports/
│   ├── Telegram/
│   ├── Web/
│   ├── Clipboard/
│   └── _Inbox Dashboard.md
├── 10 Projects/
│   ├── _Projects Dashboard.md
│   └── EXAMPLE-PKM - Example Project.md
├── 20 Areas/
│   └── _Areas Dashboard.md
├── 30 Resources/
│   └── _Resources Dashboard.md
├── 40 Zettelkasten/
│   └── _Zettelkasten Dashboard.md
├── 50 Visual Lab/
│   ├── _Visual Lab Dashboard.md
│   └── Projects/
│       └── EXAMPLE-PKM/
│           ├── 00 Brief.md
│           ├── 01 Visual Index.md
│           └── 02 Decisions.md
├── 60 Journal/
│   └── Daily/
├── 70 Maps of Content/
│   └── _MOC Dashboard.md
├── 80 Archive/
├── 90 System/
│   ├── Guides/
│   ├── Scripts/
│   └── Templates/
├── assets/
├── logseq/
├── .obsidian/
├── .env.example
├── .gitignore
├── ARCHITECTURE.md
└── README.md
```

## توضیح پوشه‌ها

### `00 Inbox`

تنها درگاه ورود اطلاعات است. هنگام ثبت اطلاعات لازم نیست درباره مقصد نهایی تصمیم بگیرید. نوت جدید باید ابتدا با `status: inbox` وارد این پوشه شود.

نمونه ورودی‌ها:

- لینک وب
- متن Clipboard
- پیام تلگرام
- ایده شخصی
- نوت مرجع یک PDF
- فایل‌های مهاجرت‌یافته از Vault قدیمی

Inbox محل نگهداری دائمی نیست. هر نوت پس از مرور باید حذف، بایگانی، به پروژه متصل یا به منبع/نوت دائمی تبدیل شود.

### `10 Projects`

برای کارهایی است که خروجی مشخص و نقطه پایان دارند؛ مانند «راه‌اندازی سایت»، «ساخت سیستم PKM» یا «تولید یک دوره».

هر پروژه باید این موارد را داشته باشد:

- `project_id` یکتا
- Outcome یا نتیجه مورد انتظار
- Definition of Done
- Next Action
- وضعیت مشخص
- لینک به فضای Visual Lab

### `20 Areas`

برای مسئولیت‌هایی است که پایان قطعی ندارند؛ مانند سلامت، امور مالی، یادگیری برنامه‌نویسی یا مدیریت محتوا.

تفاوت Area و Project:

```text
ساخت وب‌سایت جدید        → Project
نگهداری وب‌سایت‌ها       → Area
گذراندن دوره پایتون      → Project
یادگیری برنامه‌نویسی     → Area
```

### `30 Resources`

برای مقاله‌ها، کتاب‌ها، ویدئوها، ابزارها و اطلاعات مرجع است. دسته‌بندی باید بر اساس موضوع باشد، نه برنامه‌ای که اطلاعات از آن آمده است.

مثال:

```text
Telegram درباره Python → 30 Resources/Programming
مقاله Web درباره AI    → 30 Resources/AI
PDF مدیریت پروژه       → 30 Resources/Management
```

### `40 Zettelkasten`

محل نوت‌های دائمی و اتمی است. نوت دائمی باید:

1. فقط یک ادعای اصلی داشته باشد.
2. با زبان خودتان نوشته شود.
3. دلیل اهمیت آن مشخص باشد.
4. به منبع یا نوت مرتبط لینک شود.
5. بدون منبع اولیه نیز قابل‌فهم باشد.

### `50 Visual Lab`

فضای تفکر دیداری و شروع پروژه است. هر پروژه دیداری یک پوشه با همان `project_id` دارد.

```text
50 Visual Lab/Projects/WEBSITE-01/
├── 00 Brief.md
├── 01 Visual Index.md
├── 02 Decisions.md
├── Website Architecture.canvas
└── User Flow.excalidraw.md
```

`00 Brief.md` مسئله و خروجی را تعریف می‌کند. `01 Visual Index.md` همه دیاگرام‌ها را فهرست می‌کند. `02 Decisions.md` نتیجه تفکر دیداری را به تصمیم متنی و قابل‌جست‌وجو تبدیل می‌کند.

فایل Canvas یا Excalidraw نباید تنها منبع حقیقت باشد؛ تصمیم‌های مهم باید به Markdown منتقل شوند.

### `60 Journal`

نوت‌های روزانه در مسیر زیر ساخته می‌شوند:

```text
60 Journal/Daily/YYYY-MM-DD.md
```

Daily Note برای ثبت Focus، تصمیم‌ها، Captureهای سریع و مرور روز استفاده می‌شود؛ نه برای انباشتن دائمی اطلاعات مرجع.

### `70 Maps of Content`

MOCها صفحات راهبری دست‌ساز هستند. آن‌ها نوت‌ها را جابه‌جا یا کپی نمی‌کنند؛ فقط مسیرهای دسترسی متفاوت ایجاد می‌کنند.

مثال:

```text
AI MOC
├── مفاهیم پایه
├── مدل‌های زبانی
├── Prompt Engineering
├── پروژه‌های فعال
└── نوت‌های دائمی منتخب
```

### `80 Archive`

برای پروژه‌های تمام‌شده و مطالب غیرفعال است. هنگام انتقال به Archive لینک‌ها و Frontmatter باید حفظ شوند و `status` به `archived` تغییر کند.

### `90 System`

زیرساخت Vault است:

- `Templates`: قالب‌ها
- `Scripts`: اسکریپت‌های اعتبارسنجی و مهاجرت
- `Guides`: راهنماها

نوت‌های دانش عادی نباید در این پوشه قرار گیرند.

### `assets`

محل فایل‌های باینری است:

```text
assets/
├── Images/
├── Documents/
├── Audio/
├── Video/
├── Telegram/
└── Diagram Exports/
```

این فایل‌ها در `.gitignore` قرار دارند و باید با Obsidian Sync، Syncthing یا بکاپ رمزگذاری‌شده جداگانه نگهداری شوند.

## استاندارد Properties

از مجموعه کنترل‌شده زیر استفاده کنید:

```yaml
---
id: note-unique-id
title: Knowledge/Example
type: resource
status: inbox
created: 2026-07-15
updated: 2026-07-15
source: web
source_url: https://example.com
project_id:
area:
tags: [ai, research]
aliases: []
summary_level: 0
---
```

### مقادیر پیشنهادی `type`

```text
capture
project
area
resource
source-note
permanent-note
journal
decision-log
visual-brief
visual-index
dashboard
```

### مقادیر پیشنهادی `status`

```text
inbox
active
waiting
processed
evergreen
completed
archived
example
```

## خلاصه‌سازی تدریجی

از `summary_level` استفاده کنید:

| سطح | معنی |
|---:|---|
| 0 | محتوای خام |
| 1 | پاک‌سازی و اصلاح عنوان |
| 2 | مشخص‌کردن بخش‌های مهم |
| 3 | خلاصه اجرایی کوتاه |
| 4 | تبدیل به بینش دائمی و لینک‌شده |

همه ورودی‌ها لازم نیست به سطح ۴ برسند. فقط اطلاعات ارزشمند باید پردازش عمیق شوند.

## چرخه عمر دانش

```text
Capture
↓
00 Inbox
↓
Clarify: این چیست و چرا ذخیره شده؟
↓
Classify: Project / Area / Resource / Delete
↓
Connect: لینک به پروژه، Area، MOC یا نوت مرتبط
↓
Distill: خلاصه و نکات اصلی
↓
Create: نوت دائمی یا تصمیم قابل استفاده
↓
Review / Archive
```

## سیاست Tag و Link

Tags برای موضوعات مشترک و وضعیت‌های محدود استفاده می‌شوند؛ پوشه و Properties نباید به Tagهای بی‌شمار تبدیل شوند.

مناسب:

```text
#ai
#automation
#programming
#research
```

نامناسب:

```text
#telegram-python-important-read-later-project-a
```

هر نوت مهم باید حداقل به یکی از موارد زیر متصل باشد:

- Project Hub
- Area Hub
- MOC
- نوت دائمی مرتبط
- Source Note

## وضعیت Logseq

فایل `logseq/config.edn` یک پایه آزمایشی فراهم می‌کند، اما ساختار فیزیکی فعلی با مسیرهای پیش‌فرض `pages` و `journals` در Logseq یکسان نیست. تا زمان ایجاد نسخه سازگاری نهایی:

1. Vault اصلی را در Logseq باز نکنید.
2. از Logseq برای ویرایش هم‌زمان استفاده نکنید.
3. ابتدا Obsidian و Git را پایدار کنید.
4. آزمایش Logseq را روی یک Clone یا Branch جدا انجام دهید.

## اصول امنیت

- Token فقط داخل `.env` محلی قرار می‌گیرد.
- `.env` نباید Commit شود.
- `.env.example` فقط نام متغیرها و مقدار نمونه دارد.
- پیش از Commit فایل‌های GitHub Desktop را مرور کنید.
- `assets` جداگانه بکاپ می‌شود.
- Repository همیشه Private باقی می‌ماند.
- توکن افشاشده باید Revoke و تعویض شود.

## معیار سلامت سیستم

سیستم سالم است اگر:

- Capture کمتر از ۲۰ ثانیه طول بکشد.
- Inbox قابل‌کنترل باشد.
- هر پروژه Next Action داشته باشد.
- اطلاعات مهم از طریق Link یا Search پیدا شوند.
- هیچ Secret داخل Git نباشد.
- بتوان نسخه‌های قبلی را از Git بازیابی کرد.
- افزونه‌ها کمک‌کننده باشند، نه شرط دسترسی به دانش.
