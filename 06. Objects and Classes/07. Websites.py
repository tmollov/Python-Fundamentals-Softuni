while True:
    info = input().split(" | ")
    if len(info) == 1:
        break
    
    host = info[0]
    domain = info[1]

    seperator = "&"
    try:
        queries = info[2].split(",")
        queries = map(lambda x : f"[{x}]",queries)
        print(f"https://www.{host}.{domain}/query?={seperator.join(queries)}")
    except Exception:
        print(f"https://www.{host}.{domain}")  