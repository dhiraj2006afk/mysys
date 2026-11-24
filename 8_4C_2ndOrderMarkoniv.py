weather = [
    "Sunny", "Cloudy", "Rainy", "Rainy",
    "Cloudy", "Sunny", "Cloudy", "Rainy",
    "Sunny", "Sunny", "Cloudy", "Rainy",
    "Rainy", "Cloudy", "Sunny", "Cloudy"
]

pairs = []
next_states = []

# Store previous two states and next state
for i in range(2, len(weather)):
    pairs.append((weather[i-2], weather[i-1]))
    next_states.append(weather[i])

# Find unique pairs
unique_pairs = []

for pair in pairs:
    if pair not in unique_pairs:
        unique_pairs.append(pair)

# Calculate probabilities
print("Learned transition probabilities:")

for pair in unique_pairs:
    sunny = 0
    cloudy = 0
    rainy = 0

    for i in range(len(pairs)):
        if pairs[i] == pair:
            if next_states[i] == "Sunny":
                sunny += 1
            elif next_states[i] == "Cloudy":
                cloudy += 1
            else:
                rainy += 1

    total = sunny + cloudy + rainy

    print("\n", pair, "->")

    if sunny > 0:
        print(" Sunny:", format(sunny/total, ".2%"))
    if cloudy > 0:
        print(" Cloudy:", format(cloudy/total, ".2%"))
    if rainy > 0:
        print(" Rainy:", format(rainy/total, ".2%"))

# Predict next weather
a = weather[-2]
b = weather[-1]

sunny = 0
cloudy = 0
rainy = 0

for i in range(len(pairs)):
    if pairs[i] == (a, b):
        if next_states[i] == "Sunny":
            sunny += 1
        elif next_states[i] == "Cloudy":
            cloudy += 1
        else:
            rainy += 1

print("\nPrevious two states:", (a, b))

if sunny >= cloudy and sunny >= rainy:
    print("Predicted next state: Sunny")
elif cloudy >= sunny and cloudy >= rainy:
    print("Predicted next state: Cloudy")
else:
    print("Predicted next state: Rainy")