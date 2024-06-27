def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    if sender == 'university.help@gmail.com':
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        if '@' not in sender or not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        if '@' not in recipient or not (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        elif recipient != sender and '@' in sender and '@' in recipient and (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) and (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')):
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


send_email('Hi!', 'nddb.com')
send_email('Hi!', 'nddb@battlefront.xyz')
send_email('Hi!', 'university.help@gmail.com')
send_email('Hi!', 'nddb@battlefront.com', sender='univer@gmail.com')
send_email('Hi!', 'nddb@battlefront.com')
