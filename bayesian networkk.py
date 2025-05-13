from pgmpy.models import DiscreteBayesianNetwork as BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure
model = BayesianNetwork([
    ('Fever', 'Corona'),
    ('Cough', 'Corona'),
    ('Fatigue', 'Corona'),
    ('BreathingProblem', 'Corona')
])

# CPDs
cpd_fever = TabularCPD('Fever', 2, [[0.3], [0.7]])
cpd_cough = TabularCPD('Cough', 2, [[0.4], [0.6]])
cpd_fatigue = TabularCPD('Fatigue', 2, [[0.5], [0.5]])
cpd_breathing = TabularCPD('BreathingProblem', 2, [[0.6], [0.4]])

cpd_corona = TabularCPD(
    'Corona', 2,
    values=[
        [0.99, 0.97, 0.95, 0.92, 0.95, 0.92, 0.90, 0.70,
         0.96, 0.93, 0.88, 0.68, 0.93, 0.86, 0.80, 0.50],
        [0.01, 0.03, 0.05, 0.08, 0.05, 0.08, 0.10, 0.30,
         0.04, 0.07, 0.12, 0.32, 0.07, 0.14, 0.20, 0.50],
    ],
    evidence=['Fever', 'Cough', 'Fatigue', 'BreathingProblem'],
    evidence_card=[2, 2, 2, 2]
)

# Add CPDs and check model
model.add_cpds(cpd_fever, cpd_cough, cpd_fatigue, cpd_breathing, cpd_corona)
print("Model valid?", model.check_model())

# Inference
infer = VariableElimination(model)

# --- Input Section ---
print("\n--- Corona Prediction System ---")
fever = int(input("Do you have Fever? (1=Yes, 0=No): "))
cough = int(input("Do you have Cough? (1=Yes, 0=No): "))
fatigue = int(input("Do you feel Fatigue? (1=Yes, 0=No): "))
breathing = int(input("Do you have Breathing Problem? (1=Yes, 0=No): "))

# Query the model
result = infer.query(
    variables=['Corona'],
    evidence={
        'Fever': fever,
        'Cough': cough,
        'Fatigue': fatigue,
        'BreathingProblem': breathing
    }
)

# Display results
print("\n--- Prediction Result ---")
print(result)

# Extract probability of Corona = Yes
prob_yes = result.values[1]  # Index 1 = Corona=Yes

# Final message based on probability
print("\n--- Final Message ---")
if prob_yes < 0.2:
    print("✅ Low Risk of Corona. Stay healthy!")
elif prob_yes < 0.5:
    print("⚠️ Medium Risk. Monitor your symptoms and consider a test.")
else:
    print("❌ High Risk! Please consult a doctor and get tested immediately.")
