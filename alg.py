from math import radians, sin, cos, sqrt, atan2

def calculate_distance(coord1, coord2):
    # Функция для расчета расстояния между двумя координатами
    R_YAKUTSK = 7.0  # Радиус Якутска в километрах

    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R_YAKUTSK * c

    return distance

def priority_client(client, deliverycar):
    # По задании я должен минимизировать время доставки от точки А до точки Б, тоесть приоритет в скорости доставки
    # Распределяем заказы по координатам курьеров и клиенттов (ближайшего курьера на ближайших заказ)

    for order in client:
        order['assigned_deliverycar'] = None

    for deliverycar in deliverycars:
        for order in client:
            if order['assigned_deliverycar'] is None:
                order['assigned_deliverycar'] = deliverycar
                break

    return client

# Заказы:
client = [
    {'from': (62.0339, 129.7330), 'to': (62.0281, 129.7327), 'cost': 250},
    {'from': (62.0274, 129.7337), 'to': (62.0312, 129.7369), 'cost': 300},
    {'from': (63.0555, 130,7888), 'to': (72.0312, 155.7849), 'cost': 500},
    {'from': (62.0274, 129.7337), 'to': (62.0315, 129.7369), 'cost': 300},
    # Заказ from ОТКУДА to КУДА и стоимость заказа. 
]

# Курьеры:
deliverycars = [
    {'location': (62.0285, 129.7320)},
    {'location': (62.0300, 129.7380)},
    {'location': (63.0655, 130,7900)},
    {'location': (62.0310, 129.7380)},
    # 
]

prioritized_client = priority_client(client, deliverycars)

# Ответ
for order in prioritized_client:
    print(f"Order: {order}, Assigned deliverycar: {order['assigned_deliverycar']}")