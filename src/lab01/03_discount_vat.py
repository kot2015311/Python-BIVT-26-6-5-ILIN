price = int(input('Price: '))
discount = float(input('discount: '))
vat = float(input('vat: '))
base =  price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'База после скидки: {round(base,2)} \nНДС: {round(vat_amount,2)} \nИтого к оплате: {round(total,2)}')