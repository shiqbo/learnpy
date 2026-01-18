try:
    r = int(input('enter number:'))
except Exception:
    print('invalid number')


try:
    r = int(input('enter number:'))
except ValueError:
    print('ValueError, invalid number')


try:
    r = int(input('enter number:'))
    print(r / 0)
except (ValueError, ZeroDivisionError):
    print('ValueError or ZeroDivisionError')


try:
    print(1 / 0)
except Exception as e:
    print(e)


try:
    r = int(input('enter number:'))
except ValueError:
    print('ValueError')
else:
    print(r)
finally:
    print('Done')
