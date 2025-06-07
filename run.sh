#!/bin/bash

# Black Box Challenge - The Reimbursement Team of '62 Implementation
# This script interfaces with the SACRED CALCULATION ENGINE
# Usage: ./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>

# Call the Python script that contains the tears of overworked engineers
python3 calculate_reimbursement.py "$1" "$2" "$3" 