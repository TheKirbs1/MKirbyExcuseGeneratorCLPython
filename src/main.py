import random

excuse_starters = [
    "I'm sorry, but",
    "Sadly I've got to say",
    "Due to unforseen circumstances,",
    "Unfortunately",
]

excuse_reasons = [
    "my dog ate my homework",
    "my alarm didn't go off",
    "I am stuck in traffic",
    "I have a sudden family emergency",
    "my computer crashed and I lost everything",
]

excuse_endings = [
    "so I couldn't complete the task on time.",
    "which led to the delay.",
    "resulting in my inability to meet the deadline.",
    "causing me to miss out on the event."
]

def generate_excuse():
    
    random_starter = random.choice(excuse_starters)
    random_reason = random.choice(excuse_reasons)
    random_ending = random.choice(excuse_endings)
    final_excuse = random_starter + " " + random_reason + " " + random_ending
    return final_excuse

num_excuses = int(input("Enter the number of excuses to generate: "))

print("Generated Excuses: ")
for _ in range(num_excuses):
    excuse=generate_excuse();
    print(excuse)
    print("-" * 40)
