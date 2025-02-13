def normalize_url(url: str) -> str:
    https = "https://"
    if url[:7] == 'http://':
        return f'{https}{url[7:]}'
    elif url[:8] == https:
        return url
    else:
        return f'{https}{url}'
