
from itertools import product

# Implication function
def implies(a, b):
    return (not a) or b


print("PROPOSITIONAL LOGIC - TRUTH TABLE ENUMERATION\n")

# Table heading
print(" P  Q  R | Q->P | P->~Q | QvR | R->P | Q->R |  KB ")
print("----------------------------------------------------")

models = []

# Generate all 8 combinations
for P, Q, R in product([False, True], repeat=3):

    # Knowledge Base statements
    a = implies(Q, P)
    b = implies(P, not Q)
    c = Q or R

    # Query statements
    d = implies(R, P)
    e = implies(Q, R)

    # Knowledge Base
    KB = a and b and c

    # Store true models
    if KB:
        models.append((P, Q, R))

    # Display values in aligned columns
    values = [P, Q, R, a, b, c, d, e, KB]

    print(
        f" {int(P)}  {int(Q)}  {int(R)} |"
        f"  {int(a)}   |"
        f"   {int(b)}    |"
        f"  {int(c)}  |"
        f"  {int(d)}   |"
        f"  {int(e)}   |"
        f"  {int(KB)}"
    )


# Display models
print("\nModels where KB is TRUE:")

for model in models:
    print(model)


# Entailment checking
print("\nENTAILMENT RESULTS")

print("KB entails R    :", all(R for P, Q, R in models))
print("KB entails R->P :", all(implies(R, P) for P, Q, R in models))
print("KB entails Q->R :", all(implies(Q, R) for P, Q, R in models))
