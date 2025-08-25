def ctr(clicks, impressions):
    return (clicks / impressions) * 100 if impressions else 0

def cpc(spend, clicks):
    return (spend / clicks) if clicks else 0

def cpa(spend, conversions):
    return (spend / conversions) if conversions else 0

def roas(revenue, spend):
    return (revenue / spend) if spend else 0
