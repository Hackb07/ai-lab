from collections import defaultdict

class KnowledgeBase:
    def __init__(self):
        self.rules = defaultdict(list)
        self.facts = set()

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        self.rules[tuple(premise)].append(conclusion)

    def forward_chaining(self):
        new_facts = True
        while new_facts:
            new_facts = False
            for premise, conclusions in list(self.rules.items()):
                if all(p in self.facts for p in premise):
                    for conclusion in conclusions:
                        if conclusion not in self.facts:
                            self.facts.add(conclusion)
                            new_facts = True

    def backward_chaining(self, goal):
        if goal in self.facts:
            return True
        for premise, conclusions in self.rules.items():
            if goal in conclusions:
                if all(self.backward_chaining(p) for p in premise):
                    return True
        return False

# User Input
kb = KnowledgeBase()

n_facts = int(input("Enter the number of known facts: "))
for _ in range(n_facts):
    kb.add_fact(input("Enter a fact: "))

n_rules = int(input("Enter the number of rules: "))
for _ in range(n_rules):
    premises = input("Enter premises (comma separated): ").split(',')
    conclusion = input("Enter conclusion: ")
    kb.add_rule(premises, conclusion)

# Forward Chaining
kb.forward_chaining()
print("Facts after forward chaining:", kb.facts)

# Backward Chaining
goal = input("Enter the goal to check using backward chaining: ")
print(f"Can we infer '{goal}'? {kb.backward_chaining(goal)}")