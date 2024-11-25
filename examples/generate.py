from taiwanid import TaiwanID


def generate():
    taiwan_id = TaiwanID()

    print('Generate without parameters:')
    print(taiwan_id.generate())

    print('Generate with city parameter:')
    city = taiwan_id.city[0]
    print(f'City: {city}')
    print(taiwan_id.generate(city=city))

    print('Generate with city, citizenship and naturalization parameters:')
    city = taiwan_id.city[0]
    citizenship = taiwan_id.Citizenships.Native
    naturalization = taiwan_id.Naturalizations.National
    print(f'City: {city}')
    print(f'Citizenship: {citizenship}')
    print(f'Naturalization: {naturalization}')
    print(taiwan_id.generate(city=city, citizenship=citizenship, naturalization=naturalization))

    print('Generate with gender and citizenship parameters:')
    gender = taiwan_id.Genders.Female
    citizenship = taiwan_id.Citizenships.Foreign
    print(f'Gender: {gender}')
    print(f'Citizenship: {citizenship}')
    print(taiwan_id.generate(gender=gender, citizenship=citizenship))

    print('Generate with citizenship and naturalization parameters:')
    citizenship = taiwan_id.Citizenships.Native
    naturalization = taiwan_id.Naturalizations.NationalFormerlyHongKongOrMacaoResident
    print(f'Citizenship: {citizenship}')
    print(f'Naturalization: {naturalization}')
    print(taiwan_id.generate(citizenship=citizenship, naturalization=naturalization))

    print('Generate with citizenship and wrong naturalization parameters:')
    citizenship = taiwan_id.Citizenships.Foreign
    naturalization = taiwan_id.Naturalizations.National
    print(f'Citizenship: {citizenship}')
    print(f'Naturalization: {naturalization}')
    print(taiwan_id.generate(citizenship=citizenship, naturalization=naturalization))


if __name__ == '__main__':
    generate()
