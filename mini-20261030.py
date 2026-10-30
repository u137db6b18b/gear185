"""Odds and ends."""

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

# see notes
