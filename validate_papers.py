#!/usr/bin/env python
import json
import os

def validate_papers():
    print("=" * 50)
    print("Validación del Sistema de Papers IAFER")
    print("=" * 50)
    
    # Validar papers.json
    try:
        with open('./data/papers.json', 'r') as f:
            data = json.load(f)
        print("\n✓ papers.json is valid")
        print(f"  - Total metadata: {data['metadata']['total']}")
        print(f"  - Actual papers: {len(data['papers'])}")
        print(f"  - Research areas: {data['metadata']['research_areas']}")
    except Exception as e:
        print(f"\n✗ Error in papers.json: {e}")
        return False
    
    # Validar que todos los archivos referenciados existen
    print("\n Validating referenced paper files...")
    missing_files = []
    for paper in data['papers']:
        file_path = f"./data/papers/{paper['file']}"
        if not os.path.exists(file_path):
            missing_files.append(paper['file'])
            print(f"  ✗ Missing: {paper['file']}")
        else:
            try:
                with open(file_path, 'r') as f:
                    json.load(f)
                print(f"  ✓ {paper['file']}")
            except Exception as e:
                print(f"  ✗ Invalid JSON in {paper['file']}: {e}")
                missing_files.append(paper['file'])
    
    # Summary
    print("\n" + "=" * 50)
    print("Summary:")
    print(f"  - Total papers in metadata: {len(data['papers'])}")
    print(f"  - Valid paper files: {len(data['papers']) - len(missing_files)}")
    if missing_files:
        print(f"  - Missing/Invalid files: {len(missing_files)}")
    else:
        print("  ✓ All paper files are valid!")
    
    print("=" * 50)
    return len(missing_files) == 0

if __name__ == '__main__':
    success = validate_papers()
    exit(0 if success else 1)
