"""25. Sector Rotation
Sector rotation involves moving investments among different sectors of the economy in an attempt to capture the economic and market cycle’s benefits.
"""

def sector_rotation(current_sector_performance, previous_sector_performance):
    if current_sector_performance > previous_sector_performance:
        return "rotate to current sector"
    else:
        return "stay in previous sector"