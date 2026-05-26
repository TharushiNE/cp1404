"""
CP1404- Practical 01
Broken program to determine score status
"""

score = float(input("Enter score: "))
if 0 <= score < 101:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
else:
    print("Invalid score")