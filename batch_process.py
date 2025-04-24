import pandas as pd
import json
from utils import mask_pii
from models import classify_email

df = pd.read_csv("combined_emails_with_natural_pii.csv")
results = []

for _, row in df.iterrows():
    original = row["email"]
    masked, entities = mask_pii(original)
    pred_type = classify_email(masked)

    results.append({
        "input_email_body": original,
        "list_of_masked_entities": entities,
        "masked_email": masked,
        "category_of_the_email": pred_type,
        "true_label": row["type"]
    })

with open("processed_emails.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("✅ Processed emails saved to 'processed_emails.json'")
