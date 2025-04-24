import re

def mask_pii(text):
    entities = []
    
    patterns = {
        "full_name": r"\bMy name is ([A-Z][a-z]+(?: [A-Z][a-z]+)*)\b",
        "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "phone_number": r"\+?[0-9][0-9()\-\s]{7,}[0-9]",
        "dob": r"\b(?:\d{1,2}[/-])?\d{1,2}[/-]\d{2,4}\b",
        "aadhar_num": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}\b",
        "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
        "cvv_no": r"\b\d{3}\b",
        "expiry_no": r"\b(0[1-9]|1[0-2])\/\d{2,4}\b"
    }
    
    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            start, end = match.start(), match.end()
            entity_val = text[start:end]
            entities.append({
                "position": [start, end],
                "classification": label,
                "entity": entity_val
            })
            text = text[:start] + f"[{label}]" + text[end:]
            break  # Replace only first match of each type

    return text, entities
