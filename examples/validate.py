from taiwanid import TaiwanID


def validate():
    taiwan_id = TaiwanID()
    print(taiwan_id.validate('A123456789'))
    print(taiwan_id.validate('A12345678'))
    print(taiwan_id.validate('0123456789'))
    print(taiwan_id.validate('A12345678A'))
    print(taiwan_id.validate('A123456780'))


if __name__ == '__main__':
    validate()
