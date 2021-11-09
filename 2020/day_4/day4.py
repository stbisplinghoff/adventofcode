# Solution for Advent of Code 2020 day 4
import re

# Read plain data
with open("input.txt") as inFile:
    data = inFile.read()

# Part1
passports = [{k: v for k, v in [field.split(":") for field in passport.replace("\n", " ").split(" ")]} for passport in
             data.split("\n\n")]
validPassports = [len(passport) == 8 or (len(passport) == 7 and "cid" not in passport) for passport in passports].count(
    True)
print("Valid Passports:", validPassports)

# Part 2
validPassports = 0
for passport in passports:
    if not (len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)):
        continue
    conditions = [int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002,
                  int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020,
                  int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030,
                  (passport["hgt"].endswith("cm") and int(passport["hgt"][:-2]) >= 150 and int(
                      passport["hgt"][:-2]) <= 193)
                  or (passport["hgt"].endswith("in") and int(passport["hgt"][:-2]) >= 59 and int(
                      passport["hgt"][:-2]) <= 76),
                  re.match(r"#[0-9a-f]{6}$", passport["hcl"]) is not None,
                  passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                  re.match(r"[0-9]{9}$", passport["pid"]) is not None
                  ]
    if all(conditions):
        validPassports += 1
print("Valid Passports:", validPassports)
