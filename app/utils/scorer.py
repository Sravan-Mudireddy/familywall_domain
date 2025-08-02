import re

def heuristic_domain_score(business, domain):
    business_keywords = set(re.findall(r'\w+', business.lower()))
    domain_keywords = set(re.findall(r'\w+', domain.lower()))
    common_words = business_keywords.intersection(domain_keywords)
    relevance_score = len(common_words) / len(business_keywords)
    length_score = 1 if len(domain) <= 15 else 0.5
    brand_score = 0.3 if re.search(r'\d|[^a-zA-Z0-9.]', domain) else 1.0
    final_score = (0.5 * relevance_score + 0.25 * length_score + 0.25 * brand_score) * 10
    return round(final_score, 2)
