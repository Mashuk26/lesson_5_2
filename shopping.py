
def shopping():
    balance = 0
    purchases_history = []

    while True:
        print('1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            amount = float(input('Введите сумму для пополнения счета: '))
            balance += amount
            print(f'Счет успешно пополнен. Текущий баланс: {balance}\n')
        elif choice == '2':
            purchase_amount = float(input('Введите сумму покупки: '))
            if purchase_amount > balance:
                print('Недостаточно средств на счете\n')
            else:
                purchase_name = input('Введите название покупки: ')
                balance -= purchase_amount
                purchases_history.append((purchase_name, purchase_amount))
                print(f'Покупка "{purchase_name}" на сумму {purchase_amount} успешно совершена\n')
        elif choice == '3':
            print('История покупок:')
            for purchase in purchases_history:
                print(f'Покупка: {purchase[0]}, Сумма: {purchase[1]}')
            print()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню\n')

#shopping()

if __name__ == "__main__":
    main()
