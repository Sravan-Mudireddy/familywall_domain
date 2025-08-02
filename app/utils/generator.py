from app.utils.scorer import heuristic_domain_score
from app.model.loader import generator
from app.utils.safety import is_safe_input

def generate_and_evaluate(desc):
    if not is_safe_input(desc):
        return {"business": desc, "domain": None, "score": None, "status": "blocked"}

    prompt = f"Business: {desc}\nDomain:"
    result = generator(prompt, max_new_tokens=20, num_return_sequences=1, do_sample=True)[0]["generated_text"]
    domain = result.split("Domain:")[1].strip().split()[0]
    score = heuristic_domain_score(desc, domain)
    return {"business": desc, "domain": domain, "score": score, "status": "success"}
