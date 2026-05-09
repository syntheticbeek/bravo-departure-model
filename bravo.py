import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Build your training dataset
data = {
    'cast_member': ['Denise Richards', 'Raquel Leviss', 'Olivia Flowers', 'Taylor Ann Green', 'Kyle Richards'],
    'show': ['RHOBH', 'VPR', 'Southern Charm', 'Southern Charm', 'RHOBH'],
    'trigger_timing': ['mid', 'late', 'early', 'early', 'early'],
    'confirmed': [0, 0, 1, 0, 0],  # 0=denied, 1=confirmed
    'cast_reaction': [2, 2, 1, 2, 1],  # 1=neutral, 2=hostile, 0=supportive
    'betrayal_index': [8, 10, 6.5, 8, 5],
    'narrative_equity': [7, 7, 7, 8, 10],
    'victim_narrative_index': [8, 8, 7, 9, 8],
    'prior_incident': [0, 0, 1, 0, 0],  # Olivia gets 1
    'outcome': [1, 1, 1, 1, 0]  # 1=exited, 0=stayed
}

df = pd.DataFrame(data)

# Encode trigger timing
timing_map = {'early': 0, 'mid': 1, 'late': 2}
df['trigger_timing_encoded'] = df['trigger_timing'].map(timing_map)

print(df[['cast_member', 'betrayal_index', 'victim_narrative_index', 'outcome']])
# Features for training
features = ['trigger_timing_encoded', 'confirmed', 'cast_reaction', 
            'betrayal_index', 'narrative_equity', 'victim_narrative_index', 
            'prior_incident']

X_train = df[features]
y_train = df['outcome']

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Amanda and West prediction data
test_data = {
    'cast_member': ['Amanda', 'West'],
    'trigger_timing_encoded': [2, 2],      # late
    'confirmed': [0, 0],                    # both denied
    'cast_reaction': [2, 2],               # both hostile
    'betrayal_index': [10, 6],
    'narrative_equity': [10, 8],
    'victim_narrative_index': [10, 3],
    'prior_incident': [0, 0]
}

test_df = pd.DataFrame(test_data)
predictions = model.predict_proba(test_df[features])

for i, name in enumerate(['Amanda', 'West']):
    print(f"{name} — Exit probability: {predictions[i][1]:.1%}")