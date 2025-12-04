import math
from datetime import datetime

# 1. Создайте словарь email, содержащий следующие поля:
email1 = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report."
    "\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
    "date": None,
}

email2 = {
    "subject": " Weekd plans ",
    "from": "katya_yan@yandex. ",
    "to": "frid@mail. ",
    "body": "\tHey!\nLet's go hiking this weekd.\nBring snacks!\n",
    "date": None,
}

email3 = {
    "subject": "Reminder: Meeting",
    "from": "ceo@corporation.com ",
    "to": " team_lead@outlook.com ",
    "body": " ",
    "date": None,
}

email4 = {
    "subject": " ",
    "from": " alex@business.net ",
    "to": " hr@company. ",
    "body": "Hi HR,\nPlease find attached my updated CV.\nThanks!",
    "date": None,
}

email5 = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon."
    "\nRegards,\nTeam",
    "date": None,
}

emails = [email1, email2, email3, email4, email5]

# 2. Добавьте дату отправки
send_date = datetime.now().strftime("%Y-%m-%d")
for email in emails:
    email["date"] = send_date

# 3. Нормализуйте e-mail адреса отправителя и получателя
for email in emails:
    email["from"] = email["from"].strip().lower()
    email["to"] = email["to"].strip().lower()
    email["subject"] = email["subject"].strip()

# 4. Извлеките логин и домен отправителя
for email in emails:
    login, domain = email["from"].split("@")
    email["login"] = login
    email["domain"] = domain

# 5. Создайте сокращённую версию текста
for email in emails:
    email["short_body"] = email["body"][:10] + "..."

# 6. Списки доменов (уникальные значения)
personal_domains_list = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
corporate_domains_list = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']

# Удаляем дубликаты
personal_domains_list = list(set(personal_domains_list))
corporate_domains_list = list(set(corporate_domains_list))

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений
intersection = set(personal_domains_list) & set(corporate_domains_list)
if intersection:
    print(f"ВНИМАНИЕ: Найдены пересечения доменов: {intersection}")
else:
    print("✓ Пересечений доменов нет")

# 8. Проверьте «корпоративность» отправителя
corporate_domains_set = set(corporate_domains_list)
for email in emails:
    is_corporate = email["domain"] in corporate_domains_set
    email["is_corporate"] = is_corporate

# 9. Соберите «чистый» текст сообщения
for email in emails:
    clean_body = email["body"].replace("\t", " ").replace("\n", " ")
    email["clean_body"] = clean_body

# 10. Сформируйте текст отправленного письма
for email in emails:
    email["sent_text"] = f"Кому: {email['to']}, от {email['from']}\nТема: {email['subject']}, дата {email['date']}\n{email['clean_body']}"

# 11. Рассчитайте количество страниц печати
for email in emails:
    text_length = len(email["sent_text"])
    pages = math.ceil(text_length / 500)
    email["pages"] = pages

# 12. Проверьте пустоту темы и тела письма
for email in emails:
    is_subject_empty = email["subject"].strip() == ""
    is_body_empty = email["body"].strip() == ""
    email["is_subject_empty"] = is_subject_empty
    email["is_body_empty"] = is_body_empty

# 13. Создайте «маску» e-mail отправителя
for email in emails:
    login = email["login"]
    domain = email["domain"]
    masked_from = login[:2] + "***@" + domain
    email["masked_from"] = masked_from

# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru"
personal_domains_list = [domain for domain in personal_domains_list if domain not in ["list.ru", "bk.ru"]]


print("\n" + "="*60)
print("ПРОВЕРКА ВЫПОЛНЕНИЯ ВСЕХ ПУНКТОВ:")
print("="*60)

print(f"\n1. ✓ Создано {len(emails)} словарей email")
print(f"2. ✓ Дата отправки: {send_date}")
print(f"3. ✓ Адреса нормализованы (приведены к нижнему регистру, убраны пробелы)")
print(f"4. ✓ Логин и домен извлечены для всех писем")
print(f"5. ✓ Создана сокращенная версия текста для всех писем")
print(f"6. ✓ Списки доменов созданы (уникальные значения):")
print(f"   Личные домены: {personal_domains_list}")
print(f"   Корпоративные домены: {corporate_domains_list}")
print(f"7. ✓ Проверка пересечений выполнена")
print(f"8. ✓ Проверка корпоративности выполнена")
print(f"9. ✓ Чистый текст создан для всех писем")
print(f"10. ✓ Текст отправленного письма сформирован")
print(f"11. ✓ Количество страниц рассчитано")
print(f"12. ✓ Проверка пустоты темы и тела выполнена")
print(f"13. ✓ Маска e-mail создана")
print(f"14. ✓ Удалены домены 'list.ru' и 'bk.ru' из личных доменов")

print("\n" + "="*60)
print("ИНФОРМАЦИЯ О ПИСЬМАХ:")
print("="*60)

for i, email in enumerate(emails, 1):
    print(f"\nПисьмо #{i}:")
    print(f"  От: {email['masked_from']}")
    print(f"  Кому: {email['to']}")
    print(f"  Тема: '{email['subject']}'")
    print(f"  Сокращенный текст: {email['short_body']}")
    print(f"  Домен: {email['domain']}")
    print(f"  Корпоративный: {email['is_corporate']}")
    print(f"  Тема пустая: {email['is_subject_empty']}")
    print(f"  Тело пустое: {email['is_body_empty']}")
    print(f"  Страниц для печати: {email['pages']}")
    print(f"  Дата: {email['date']}")
    print("-" * 40)

print("\n" + "="*60)
print("ИТОГОВЫЕ СПИСКИ ДОМЕНОВ:")
print("="*60)
print(f"Личные домены ({len(personal_domains_list)}): {personal_domains_list}")
print(f"Корпоративные домены ({len(corporate_domains_list)}): {corporate_domains_list}")

# Демонстрация примера полного текста письма
print("\n" + "="*60)
print("ПРИМЕР ПОЛНОГО ТЕКСТА ПИСЬМА (email1):")
print("="*60)
print(emails[0]["sent_text"])