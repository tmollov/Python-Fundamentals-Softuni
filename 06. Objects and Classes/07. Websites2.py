class Website:
    def __init__(self,host,domain,queries=[]):
        self.host = host
        self.domain = domain
        self.queries = queries

    def Print(self):
        seperator = "&"
        if self.queries:
            a = list(map(lambda x : f"[{x}]",self.queries))
            print(f"https://www.{self.host}.{self.domain}/query?={seperator.join(a)}")
        else:
            print(f"https://www.{self.host}.{self.domain}")  

websites = []

while True:
    info = input().split(" | ")
    if len(info) == 1:
        break
    
    host = info[0]
    domain = info[1]

    try:
        queries = info[2].split(",") 
        websites.append(Website(host,domain,queries))
    except Exception:
        websites.append(Website(host,domain))
        
for site in websites:
    site.Print()