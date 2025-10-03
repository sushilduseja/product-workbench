"""
Small helper to create a project folder from the template.

Usage:
  python scripts/generate_project_readme.py "project-slug" "Project Title" "One-liner"

Creates project folder under `projects/` with README.md and case-study.md copied from TEMPLATE_PROJECT.md placeholders.
"""
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / 'projects' / 'TEMPLATE_PROJECT.md'
PROJECTS_DIR = ROOT / 'projects'

TEMPLATE_README = """# {title}

One-liner: {one_liner}

## Problem
[Describe the problem]

## Solution
[Summarise solution]

## Tech
[Tech stack]

## Results
[Key metrics and outcomes]

See `case-study.md` for full details and `../visuals/` for demo assets.
"""

TEMPLATE_CASE = """# {title} — Case Study

## Problem
[Describe the problem]

## Approach
[Explain approach]

## Impact
[Add measured impact]

## Lessons
[Key takeaways]
"""


def main():
    if len(sys.argv) < 4:
        print('Usage: python scripts/generate_project_readme.py <slug> "Title" "One-liner"')
        sys.exit(2)

    slug = sys.argv[1]
    title = sys.argv[2]
    one_liner = sys.argv[3]

    project_dir = PROJECTS_DIR / slug
    project_dir.mkdir(parents=True, exist_ok=True)

    readme_path = project_dir / 'README.md'
    case_path = project_dir / 'case-study.md'

    if not readme_path.exists():
        readme_path.write_text(TEMPLATE_README.format(title=title, one_liner=one_liner))
        print('Created', readme_path)
    else:
        print('README already exists:', readme_path)

    if not case_path.exists():
        case_path.write_text(TEMPLATE_CASE.format(title=title))
        print('Created', case_path)
    else:
        print('Case study already exists:', case_path)


if __name__ == '__main__':
    main()
