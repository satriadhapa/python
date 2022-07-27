def calon_presiden(umur):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return umur >= 35

print("pantas atau tidak menjadi presiden", calon_presiden(24))
print("pantas atau tidak menjadi presiden", calon_presiden(36))
