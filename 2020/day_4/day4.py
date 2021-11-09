# Solution for Advent of Code 2020 day 4
import re

# Read plain data
with open("input.txt") as inFile:
    data = inFile.read()

# Part1
passports = [{k:v for k,v in [field.split(":") for field in passport.replace("\n", " ").split(" ")]} for passport in data.split("\n\n")]
validPassports = [len(passport) == 8 or (len(passport) == 7 and "cid" not in passport) for passport in passports].count(True)
print("Valid Passports:", validPassports)

# Part 2
validPassports = 0
for passport in passports:
    if not (len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)):
        continue
    invalidField = False
    for k,v in passport.items():
        if (k == "byr") and not (int(v) >= 1920 and int(v) <= 2002):
            invalidField = True
        if (k == "iyr") and not (int(v) >= 2010 and int(v) <= 2020):
            invalidField = True
        if (k == "eyr") and not (int(v) >= 2020 and int(v) <= 2030):
            invalidField = True
        if (k == "hgt") and not ((v.endswith("cm") and int(v[:-2]) >= 150 and int(v[:-2]) <= 193)
                                or (v.endswith("in") and int(v[:-2]) >= 59 and int(v[:-2]) <= 76)):
            invalidField = True
        if (k == "hcl") and not (re.match(r"#[0-9a-f]{6}$", v)):
            invalidField = True
        if (k == "ecl") and not v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            invalidField = True
        if (k == "pid") and not (re.match(r"[0-9]{9}$", v)):
            invalidField = True
    if not invalidField:
        validPassports += 1
print("Valid Passports:", validPassports)
