from http.client import responses

books = {
    'LevTolstoy': 'Anna Karenina',
    'AnthonChekhov': 'The Cherry Otchard'
}
books2 = {'Lev Tolstoy', 'Anthon Chekhov'}

print(books2)

response = {
    'statusCode': '200',
    'user':{
        'id': 1, 'name': 'Janna'
    }
}
print(response['user'],['name'])

data = [1, 2, 33]
print(isinstance(data, list))

value = 22
print(isinstance(value, int))

value = 22.1
print(isinstance(value, float))

team_ages = {
    "Kristina": 39,
    "Alex":40,
    "Tatiana": 54,
    "Andrey": 44,
    "Vladimir":65
}
print(team_ages.keys())
print(team_ages.values())

team_names = "Kristina", "Alex", "Tatiana", "Andrey", "Vladimir"
team_num = [39, 40, 54, 44, 65]
team_ages = {name: age for name, age in zip(team_names, team_num)}
print(team_ages)