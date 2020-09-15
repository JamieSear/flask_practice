''' Footballers controller '''

footballers = [
    {
        "id": 1,
        "first_name": "Hector",
        "last_name": "Bellerin",
        "team": "Arsenal"
    },
    {
        "id": 2,
        "first_name": "Alex",
        "last_name": "Iwobi",
        "team": "Arsenal"
    },
    {
        "id": 3,
        "first_name": "Mesut",
        "last_name": "Ozil",
        "team": "Arsenal"
    },
    {
        "id": 4,
        "first_name": "Alexis",
        "last_name": "Sanchez",
        "team": "Arsenal"
    },
    {
        "id": 5,
        "first_name": "Theo",
        "last_name": "Walcott",
        "team": "Arsenal"
    },
    {
        "id": 6,
        "first_name": "Marcos",
        "last_name": "Alonso",
        "team": "Chelsea"
    },
    {
        "id": 7,
        "first_name": "Cesar",
        "last_name": "Azpilicueta",
        "team": "Chelsea"
    },
    {
        "id": 8,
        "first_name": "Gary",
        "last_name": "Cahill",
        "team": "Chelsea"
    },
    {
        "id": 9,
        "first_name": "Diego",
        "last_name": "Costa",
        "team": "Chelsea"
    },
    {
        "id": 10,
        "first_name": "Thibaut",
        "last_name": "Courtois",
        "team": "Chelsea"
    },
    {
        "id": 11,
        "first_name": "Eden",
        "last_name": "Hazard",
        "team": "Chelsea"
    },
    {
        "id": 12,
        "first_name": "Nemanja",
        "last_name": "Matic",
        "team": "Chelsea"
    },
    {
        "id": 13,
        "first_name": "Victor",
        "last_name": "Moses",
        "team": "Chelsea"
    },
    {
        "id": 14,
        "last_name": "Willian",
        "team": "Chelsea"
    }
]


def index(req):
    return[p for p in footballers], 200


def create(req):
    new_player = req.get_json()
    new_player['id'] = sorted([p['id'] for p in footballers])[-1] + 1
    footballers.append(new_player)
    return new_player, 201
