# import json
# import time
# import random
# from datetime import datetime
# from faker import Faker
# from kafka import KafkaProducer

# fake = Faker()

# # Kafka producer config
# producer = KafkaProducer(
#     bootstrap_servers='localhost:9092',
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# # Event fields and pricing
# plans = ['Basic', 'Pro', 'Enterprise']
# plan_prices = {'Basic': 49.0, 'Pro': 99.0, 'Enterprise': 199.0}
# regions = ['US', 'EU', 'IN', 'APAC']
# event_types = ['signup', 'payment', 'upgrade', 'downgrade', 'login', 'subscription_renewal']

# # Track users
# user_counter = 1000
# user_profiles = {}  # user_id -> { region, plan, is_trial }

# # Downgrade logic
# def downgrade_plan(current):
#     if current == 'Enterprise':
#         return 'Pro'
#     elif current == 'Pro':
#         return 'Basic'
#     return 'Basic'

# def generate_event():
#     global user_counter

#     event_type = random.choice(event_types)

#     if event_type == 'signup':
#         user_id = user_counter
#         user_counter += 1
#         region = random.choice(regions)
#         plan = random.choice(plans)
#         is_trial = random.choice([True, False])
#         user_profiles[user_id] = {'region': region, 'plan': plan, 'is_trial': is_trial}
#     elif user_profiles:
#         user_id = random.choice(list(user_profiles.keys()))
#         region = user_profiles[user_id]['region']
#         plan = user_profiles[user_id]['plan']
#         is_trial = False

#         if event_type == 'upgrade' and plan != 'Enterprise':
#             new_plan = plans[plans.index(plan) + 1]
#             user_profiles[user_id]['plan'] = new_plan
#         elif event_type == 'downgrade' and plan != 'Basic':
#             user_profiles[user_id]['plan'] = downgrade_plan(plan)
#     else:
#         return None

#     current_plan = user_profiles[user_id]['plan']
#     amount = plan_prices.get(current_plan, 0.0) if event_type in ['payment', 'subscription_renewal', 'upgrade'] else 0.0

#     return {
#         "event_id": str(fake.uuid4())[:8],
#         "user_id": user_id,
#         "event_type": event_type,
#         "plan": current_plan,
#         "region": user_profiles[user_id]['region'],
#         "amount": amount,
#         "currency": "USD",
#         "is_trial": is_trial,
#         "timestamp": datetime.utcnow().isoformat()
#     }

# # Stream every 2 seconds
# if __name__ == "__main__":
#     print("Producing events to Kafka topic: saas-events")
#     while True:
#         event = generate_event()
#         if event:
#             producer.send('saas-events', value=event)
#             print("✅ Sent:", event)
#         time.sleep(2)




import json
import time
import random
from datetime import datetime
from faker import Faker
from kafka import KafkaProducer

fake = Faker()

# Kafka producer config
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Event fields and pricing
plans = ['Basic', 'Pro', 'Enterprise']
plan_prices = {'Basic': 49.0, 'Pro': 99.0, 'Enterprise': 199.0}
regions = ['US', 'EU', 'IN', 'APAC']
event_types = ['signup', 'payment', 'upgrade', 'downgrade', 'login', 'subscription_renewal']

# Track users
user_counter = 1000
user_profiles = {}  # user_id -> { region, plan, is_trial }

# Downgrade logic
def downgrade_plan(current):
    if current == 'Enterprise':
        return 'Pro'
    elif current == 'Pro':
        return 'Basic'
    return 'Basic'

# Random historical timestamp generator (last 5 years)
def get_random_timestamp():
    start_year = datetime.utcnow().year - 5
    random_year = random.randint(start_year, datetime.utcnow().year)
    random_month = random.randint(1, 12)
    random_day = random.randint(1, 28)  # keep it safe for all months
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    return datetime(random_year, random_month, random_day, random_hour, random_minute, random_second).isoformat()

def generate_event():
    global user_counter

    event_type = random.choice(event_types)

    if event_type == 'signup':
        user_id = user_counter
        user_counter += 1
        region = random.choice(regions)
        plan = random.choice(plans)
        is_trial = random.choice([True, False])
        user_profiles[user_id] = {'region': region, 'plan': plan, 'is_trial': is_trial}
    elif user_profiles:
        user_id = random.choice(list(user_profiles.keys()))
        region = user_profiles[user_id]['region']
        plan = user_profiles[user_id]['plan']
        is_trial = False

        if event_type == 'upgrade' and plan != 'Enterprise':
            new_plan = plans[plans.index(plan) + 1]
            user_profiles[user_id]['plan'] = new_plan
        elif event_type == 'downgrade' and plan != 'Basic':
            user_profiles[user_id]['plan'] = downgrade_plan(plan)
    else:
        return None

    current_plan = user_profiles[user_id]['plan']
    amount = plan_prices.get(current_plan, 0.0) if event_type in ['payment', 'subscription_renewal', 'upgrade'] else 0.0

    return {
        "event_id": str(fake.uuid4())[:8],
        "user_id": user_id,
        "event_type": event_type,
        "plan": current_plan,
        "region": user_profiles[user_id]['region'],
        "amount": amount,
        "currency": "USD",
        "is_trial": is_trial,
        "timestamp": get_random_timestamp()
    }

# Stream every 2 seconds
if __name__ == "__main__":
    print("Producing events to Kafka topic: saas-events")
    while True:
        event = generate_event()
        if event:
            producer.send('saas-events', value=event)
            print("✅ Sent:", event)
        time.sleep(2)