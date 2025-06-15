from urllib.parse import urlparse

def extract_features(url):
    """
    Extracts 9 features from a URL (5 real, 4 dummy for demo).
    """
    features = []

    # 1. Has IP address in domain
    domain = urlparse(url).netloc
    features.append(1 if any(char.isdigit() for char in domain) and '.' in domain else 0)

    # 2. URL length > 54
    features.append(1 if len(url) > 54 else 0)

    # 3. Uses a shortening service
    shortening_services = ['bit.ly', 'goo.gl', 'tinyurl.com', 'ow.ly', 't.co', 'is.gd', 'buff.ly']
    features.append(1 if any(service in url for service in shortening_services) else 0)

    # 4. Has '@' symbol
    features.append(1 if '@' in url else 0)

    # 5. Has '-' in domain
    features.append(1 if '-' in domain else 0)

    # 6-9. Dummy features (set to 0 or add more logic)
    features += [0, 0, 0, 0]

    return features