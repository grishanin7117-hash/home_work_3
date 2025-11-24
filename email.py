import math
from datetime import datetime

send_date = datetime.now().strftime("%Y-%m-%d")


email1 = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report."
    "\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
    "date": send_date,
}

email2 = {
    "subject": " Weekd plans ",
    "from": "katya_yan@yandex. ",
    "to": "frid@mail. ",
    "body": "\tHey!\nLet's go hiking this weekd.\nBring snacks!\n",
    "date": send_date,
}

email3 = {
    "subject": "Reminder: Meeting",
    "from": "ceo@corporation.com ",
    "to": " team_lead@outlook.com ",
    "body": " ",
    "date": send_date,
}

email4 = {
    "subject": " ",
    "from": " alex@business.net ",
    "to": " hr@company. ",
    "body": "Hi HR,\nPlease find attached my updated CV.\nThanks!",
    "date": send_date,
}

email5 = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon."
    "\nRegards,\nTeam",
    "date": send_date,
}


emails = [email1, email2, email3, email4, email5]

for email in emails:
    email["from"] = email["from"].strip().lower()
    email["to"] = email["to"].strip().lower()
    email["subject"] = email["subject"].strip()
    email["short_body"] = email["body"][:10] + "..."


for email in emails:
    login, domain = email["from"].split("@")

    email["login"] = login
    email["domain"] = domain


personal_domains = {
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
}

corporate_domains = {
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
}


for email in emails:

    domain = email["domain"]

    is_corporate = domain in corporate_domains

    email["is_corporate"] = is_corporate

    for email in emails:
        clean_body = email["body"].replace("\t", " ").replace("\n", " ")

        email["clean_body"] = clean_body


for email in emails:
    email[
        "sent_text"
    ] = f"""Кому: {email['to']}, от {email['from']}
Тема: {email['subject']}, дата {email['date']}
{email['clean_body']}"""

    for email in emails:
        email[
            "sent_text"
        ] = f"""Кому: {email['to']}, от {email['from']}
    Тема: {email['subject']}, дата {email['date']}
    {email['clean_body']}"""

    for email in emails:
        text_length = len(email["sent_text"])
        pages = math.ceil(text_length / 500)
        email["pages"] = pages

        for email in emails:

            is_subject_empty = email["subject"].strip() == ""

            is_body_empty = email["body"].strip() == ""

            email["is_subject_empty"] = is_subject_empty
            email["is_body_empty"] = is_body_empty

            for email in emails:

                login = email["login"]
                domain = email["domain"]

                masked_from = login[:2] + "**@" + domain

                email["masked_from"] = masked_from


personal_domains -= {"list.ru", "bk.ru"}

print(f"  От: '{email['from']}'")
print(f"  Кому: '{email['to']}'")
print(f"  Тэма: '{email['subject']}'")
print(f"Содержание: {email['short_body']}")
print(f"Письмо от: {email['from']}")
print(f"  Логин: {login}")
print(f"  Домен: {domain}")
print("Личные домены :", personal_domains)
print("Корпоративные :", corporate_domains)
print(f"Отправитель: {email['from']}")
print(f"  Домен: {domain}")
print(f"  Корпоративный: {is_corporate}")
print(f"Оригинальный текст: {repr(email['body'])}")
print(f"Чистый текст: {repr(email['clean_body'])}")
print("-" * 50)
print(f"Письмо: {email['subject']}")
print(f"Длина текста: {text_length} символов")
print(f"Количество страниц: {pages}")
print("@" * 30)
print(f"Письмо: {email['from']}")
print(f"  Тема: '{email['subject']}'")
print(f"  Тема пустая: {is_subject_empty}")
print(f"  Тело пустое: {is_body_empty}")
print("-" * 40)
print(email["sent_text"])
print("=" * 50)
print(f"Маска: {masked_from}")
print("-" * 50)
