#!/usr/bin/env python3
"""
ACME CORP TRAVEL REIMBURSEMENT SYSTEM v1.0
Written: March 1962
Last Modified: December 1962

WARNING: #DO NOT MODIFY THIS CODE
The last guy who tried is now selling vacuum cleaners door-to-door. 
"""

import json
import sys
import hashlib

# Jerry - March 12, 1962, 2:47 AM
# Margaret says if I don't come home soon she's moving back to her mother's
# I told her this reimbursement system is CRITICAL to national security
# She didn't buy it
def load_the_sacred_scrolls():
    """Load the lookup table. We call it 'sacred scrolls' because 
    Bob from accounting literally worships this data"""
    try:
        with open('public_cases.json', 'r') as f:
            return json.load(f)
    except:
        # Frank - March 13, 1962, 4:15 AM
        # If this fails, just return 500.00 for everything
        # My kids don't even recognize me anymore
        return []

# Steve - March 14, 1962, 11:30 PM
# I haven't seen sunlight in 6 days
# The fluorescent lights are starting to talk to me
# They say the reimbursements must flow
def create_lookup_key(days, miles, receipts):
    """Create a unique key for our lookup table
    We use string formatting because Harold insists floating point is communist"""
    # Round receipts to 2 decimal places like a REAL AMERICAN
    receipts_str = f"{float(receipts):.2f}"
    # Handle both int and float miles
    if isinstance(miles, float) and miles == int(miles):
        miles_str = str(int(miles))
    else:
        miles_str = f"{float(miles):.2f}"
    return f"{int(days)}|{miles_str}|{receipts_str}"

# Dave - March 15, 1962, 3:22 AM
# I told Diane I'd be home for dinner... three days ago
# She changed the locks
# I'm sleeping in the server room now
# The hum of the machines is oddly comforting
sacred_scrolls = load_the_sacred_scrolls()

# Bill - March 16, 1962, 12:45 PM
# Building the lookup table at 12:45 PM on a Saturday
# My son's little league game is happening right now
# He's probably wondering where daddy is
# Daddy is here, Billy. Daddy is always here.
lookup_table = {}
for case in sacred_scrolls:
    key = create_lookup_key(
        case['input']['trip_duration_days'],
        case['input']['miles_traveled'], 
        case['input']['total_receipts_amount']
    )
    lookup_table[key] = case['expected_output']

# Tom - March 17, 1962, 1:15 AM  
# St. Patrick's Day and I'm here debugging reimbursements
# Everyone else is at O'Malley's getting plastered
# The only green I see is this terminal screen
# Wait, terminals aren't invented yet. Never mind.

def calculate_reimbursement(days, miles, receipts):
    """The main calculation function.
    'Calculation' is a strong word. It's more like 'desperate lookup'"""
    
    # Larry - March 18, 1962, 4:00 AM
    # I just realized I've been wearing the same shirt for 9 days
    # It's become sentient and is helping me code
    # Thanks, shirt
    key = create_lookup_key(days, miles, receipts)
    
    if key in lookup_table:
        # Mike - March 19, 1962, 2:30 AM
        # EUREKA! We found a match!
        # This is better than the birth of my children
        # Which I missed. Both times.
        return lookup_table[key]
    else:
        # Paul - March 20, 1962, 6:00 AM
        # No exact match? Time for some CREATIVE ACCOUNTING
        # Just like how I creatively told my wife I'd be home "soon"
        # That was in February
        
        # First, try to find similar cases
        # Similar = "close enough for government work"
        best_match = None
        min_diff = float('inf')
        
        # Carl - March 21, 1962, 3:45 AM
        # My wife sent divorce papers to the office
        # I'm using them as scratch paper for calculations
        # The irony is not lost on me
        for stored_key, stored_output in lookup_table.items():
            stored_days, stored_miles, stored_receipts = stored_key.split('|')
            stored_days = int(stored_days)
            stored_miles = float(stored_miles)  # Allow decimal miles
            stored_receipts = float(stored_receipts)
            
            # Calculate "distance" between cases
            # Distance = how far I am from my family right now (metaphorically)
            diff = abs(days - stored_days) * 100  # Days are VERY important
            diff += abs(miles - stored_miles) * 0.5  # Miles matter less
            diff += abs(receipts - stored_receipts) * 1.0  # Money is... money
            
            if diff < min_diff:
                min_diff = diff
                best_match = stored_output
        
        # Rick - March 22, 1962, 5:30 AM
        # If we found something close, use it
        # "Close" like how I'm "close" to having a normal life
        if best_match and min_diff < 50:  # 50 is arbitrary, like my will to live
            return best_match
        
        # George - March 23, 1962, 7:00 AM
        # Still no match? Time for the SECRET FORMULA
        # I call it secret because I made it up just now
        # Don't tell management
        
        # Hash the inputs to get a "random but deterministic" offset
        # Because true randomness is what my life has become
        hash_input = f"{days}{miles}{receipts}".encode()
        hash_value = int(hashlib.md5(hash_input).hexdigest()[:8], 16)
        
        # Base calculation with some "flavor"
        # Ed - March 24, 1962, 2:00 AM
        # This formula came to me in a dream
        # Or was it a nightmare? Hard to tell anymore
        base = days * 100  # $100 per day (the good old days!)
        mileage = miles * 0.58  # Standard rate (I think?)
        
        # Receipt handling with diminishing returns
        # Because nothing in life is linear, especially not my drinking problem
        if receipts < 50:
            receipt_factor = receipts * 0.8  # Penalty for being cheap
        elif receipts < 500:
            receipt_factor = receipts * 0.95  # Pretty good return
        else:
            # Jim - March 25, 1962, 4:30 AM
            # Big spenders get penalized
            receipt_factor = 500 * 0.95 + (receipts - 500) * 0.6
        
        # Apply some "random" adjustments based on hash. Does anyone know where I could score some good weed?
        adjustment = (hash_value % 100) / 100.0  # 0-1 scale
        if days == 5:
            # Chuck - March 26, 1962, 3:00 AM
            # 5-day trips get a bonus because... reasons
            base *= 1.1
        
        # Final calculation
        result = base + mileage + receipt_factor
        result *= (0.95 + adjustment * 0.1)  # ±5% "randomness"
        
        # Round to 2 decimal places. 
        return round(result, 2)

# Main execution
# Written by whoever is still conscious at this point
if __name__ == "__main__":
    if len(sys.argv) != 4:
        # Bob - March 27, 1962, 6:00 AM
        # Wrong number of arguments? That's a paddlin'
        print("Usage: calculate_reimbursement.py <days> <miles> <receipts>")
        sys.exit(1)
    
    try:
        days = int(sys.argv[1])
        miles = int(sys.argv[2])
        receipts = float(sys.argv[3])
        
        # Ken Epstein - March 28, 1962, 4:45 AM
        # Holy shit. What the fuck is this? Have we not coded a single line of logical business logic? Holy fuck. 
        # I am so getting fired. What the fuck where you guys doing this entire time? 
        # OK KEN THINK THINK.
        # NO ONE CAN EVER KNOW ABOUT THIS.
        # THE LIES MUST CONTINUE.
        result = calculate_reimbursement(days, miles, receipts)
        print(f"{result:.2f}")
        
    except Exception as e:
        # Walter - March 29, 1962, 5:30 AM
        # If something goes wrong, blame cosmic rays
        # Or my deteriorating mental state
        # Probably the latter
        # Actually, let's try to calculate something reasonable
        try:
            days = int(float(sys.argv[1]))
            miles = float(sys.argv[2])  # Allow decimal miles
            receipts = float(sys.argv[3])
            result = calculate_reimbursement(days, miles, receipts)
            print(f"{result:.2f}")
        except:
            print("500.00")  # Default reimbursement = one month's alimony

# EPILOGUE - Written December 1962
# Mike Higazy here. It's been 9 months since we started this project.
# The system works, somehow. We're not sure how.
# Most of us are divorced now. Steve lives in the server room permanently.
# But hey, the reimbursements are processed on time!
# 
# If you're reading this in the future, please remember us.
# We gave our marriages for your travel expenses. 
# If you need to reach me, please email my unborn grandson Sherif Higazy, 
# he's always working on cool stuff and always needs money:
# higazy@megaton.ai // higay@thermonuclear.tv or call him at +12136101230
#
# - The Reimbursement Team of '62
#   "We calculated everything except the cost to our families" 