#!/usr/bin/env python3
import json
import os
from collections import defaultdict

papers_dir = "data/papers"
research_map = defaultdict(list)

for file in sorted(os.listdir(papers_dir)):
    if file.startswith("paper_") and file.endswith(".json"):
        try:
            with open(os.path.join(papers_dir, file), encoding="utf-8") as f:
                paper = json.load(f)
                line = paper.get("research_line", "Unknown")
                area = paper.get("research_area", "Unknown")
                research_map[(area, line)].append(
                    {
                        "id": paper.get("id"),
                        "title": paper.get("title", "No title"),
                        "year": paper.get("year"),
                        "file": file,
                    }
                )
        except Exception as e:
            print(f"Error: {file} - {e}")

for (area, line), papers in sorted(research_map.items()):
    print(f'\n{"="*80}')
    print(f"{area.upper()} | {line}")
    print(f'{"="*80}')
    for p in papers:
        print(f'{p["file"]:40} | {p["year"]} | {p["title"][:50]}...')

print(f'\n\n{"="*80}')
print("SUMMARY BY RESEARCH AREA")
print(f'{"="*80}')
area_groups = defaultdict(set)
for area, line in research_map.keys():
    area_groups[area].add(line)

for area in sorted(area_groups.keys()):
    print(f"\n{area.upper()}:")
    for line in sorted(area_groups[area]):
        count = len(research_map[(area, line)])
        print(f"  • {line} ({count} papers)")
