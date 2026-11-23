
def unify(pattern, fact, subst=None):
    if subst is None:
        subst = {}

    if pattern == fact:
        return subst

    # Variable matching
    if isinstance(pattern, str) and pattern.startswith("?"):
        if pattern in subst:
            return subst if subst[pattern] == fact else None

        subst[pattern] = fact
        return subst

    # Predicate matching
    if isinstance(pattern, tuple) and isinstance(fact, tuple):
        if pattern[0] != fact[0] or len(pattern) != len(fact):
            return None

        for p, f in zip(pattern[1:], fact[1:]):
            subst = unify(p, f, subst)

            if subst is None:
                return None

        return subst

    return None


def substitute(expr, subst):
    if isinstance(expr, str) and expr.startswith("?"):
        return subst.get(expr, expr)

    if isinstance(expr, tuple):
        return (expr[0],) + tuple(
            substitute(arg, subst) for arg in expr[1:]
        )

    return expr


def parse(text):
    text = text.strip()

    if not text:
        raise ValueError("Input cannot be empty!")

    if "(" not in text or not text.endswith(")"):
        raise ValueError(
            "Invalid format! Use Predicate(argument)"
        )

    name, args = text.split("(", 1)
    args = args[:-1]

    if not name.strip() or not args.strip():
        raise ValueError("Invalid predicate!")

    return (name.strip(),) + tuple(
        x.strip() for x in args.split(",")
    )


def forward_chaining(facts, rules, query):
    kb = list(facts)

    while True:
        new_facts = []

        for premises, conclusion in rules:

            def match_all(index, subst):
                if index == len(premises):
                    return [subst]

                results = []

                for fact in kb:
                    current = unify(
                        substitute(premises[index], subst),
                        fact,
                        dict(subst)
                    )

                    if current is not None:
                        results.extend(
                            match_all(index + 1, current)
                        )

                return results

            substitutions = match_all(0, {})

            for subst in substitutions:
                result = substitute(conclusion, subst)

                if result not in kb and result not in new_facts:
                    new_facts.append(result)

                    # Check whether query is proved
                    answer = unify(result, query)

                    if answer is not None:
                        return True, answer

        if not new_facts:
            return False, None

        kb.extend(new_facts)


# Main Program

print("FIRST ORDER LOGIC - FORWARD CHAINING")

facts = []
rules = []

try:
    # Read facts
    n = int(input("\nEnter number of facts: "))

    print("Enter facts:")

    for i in range(n):
        facts.append(parse(input()))

    # Read rules
    r = int(input("\nEnter number of rules: "))

    print("Enter rules in format: premise1 & premise2 -> conclusion")

    for i in range(r):
        rule = input().strip()

        if "->" not in rule:
            raise ValueError("Invalid rule format!")

        left, right = rule.split("->", 1)

        premises = [parse(x) for x in left.split("&")]
        conclusion = parse(right)

        rules.append((premises, conclusion))

    # Read query
    query = parse(input("\nEnter query to prove: "))

    # Perform forward chaining
    result, substitution = forward_chaining(
        facts, rules, query
    )

    # Display result
    if result:
        print("\nQuery Proved!")
        print("Substitution:", substitution)
    else:
        print("\nQuery Cannot Be Proved!")

except ValueError as e:
    print("\nInput Error:", e)
