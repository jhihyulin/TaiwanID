from taiwanid import TaiwanID


def parse():
    taiwan_id = TaiwanID()
    parse_result = taiwan_id.parse('A123456789')
    print(f'Parse result: {parse_result}')
    print(f'City: {parse_result.city}')
    print(f'City name: {parse_result.city.name}')
    print(f'Gender: {parse_result.gender}')
    print(f'Gender name: {parse_result.gender.name}')
    print(f'Citizenship: {parse_result.citizenship}')
    print(f'Citizenship name: {parse_result.citizenship.name}')
    print(f'Naturalization: {parse_result.naturalization}')
    print(f'Naturalization name: {parse_result.naturalization.name}')


if __name__ == '__main__':
    parse()
