import json
import sys

# Read the JSON result from FOOPS!
with open(sys.argv[1]) as f:
    data = json.load(f)

# Initialize counters
total_tests = 0
passed_tests = 0

# Iterate over the checks and count total tests and passed tests
for check in data['checks']:
    total_tests += check['total_tests_run']
    passed_tests += check['total_passed_tests']

# Calculate the percentage of passed tests
pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

# Print the results (optional)
print(f"Total tests: {total_tests}")
print(f"Passed tests: {passed_tests}")
print(f"Pass percentage: {pass_percentage:.2f}%")

# Create a badge (SVG format)
badge_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="100" height="20">
  <rect width="100" height="20" fill="#555"/>
  <text x="50" y="15" font-size="12" fill="white" text-anchor="middle">
    {pass_percentage:.2f} ({passed_tests}/{total_tests})
  </text>
</svg>"""

# Save the badge as an SVG file
with open('foops-badge.svg', 'w') as badge_file:
    badge_file.write(badge_content)
