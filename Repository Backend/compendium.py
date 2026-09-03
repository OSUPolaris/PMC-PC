"""Build an index of Cookbook Research Projects by parsing each project's description.md."""

import re
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR_NAME = "Cookbook Research Projects"
PROJECTS_DIR = REPO_ROOT / PROJECTS_DIR_NAME
OUTPUT_CSV = Path(__file__).resolve().parent / "compendium.csv"
OUTPUT_MARKDOWN = REPO_ROOT / "Compendium.md"

# Matches lines like "# Title: X", "*Subfield: X*", "*Topics covered: X*", "*Type of project: X*"
FIELD_PATTERNS = {
    "Title": re.compile(r"^#\s*Title:\s*(.+?)\s*$", re.MULTILINE),
    "Subfield": re.compile(r"^\*Subfield:\s*(.+?)\*?\s*$", re.MULTILINE),
    "Topics Covered": re.compile(r"^\*Topics covered:\s*(.+?)\*?\s*$", re.MULTILINE),
    "Project Type": re.compile(r"^\*Type of project:\s*(.+?)\*?\s*$", re.MULTILINE),
}


def parse_description(description_path: Path) -> dict:
    """Extract the fields of interest from a description.md file."""
    text = description_path.read_text(encoding="utf-8")

    fields = {}
    for field_name, pattern in FIELD_PATTERNS.items():
        match = pattern.search(text)
        fields[field_name] = match.group(1).strip() if match else None

    return fields


def build_project_index(projects_dir: Path) -> pd.DataFrame:
    """Scan each subdirectory of projects_dir for a description.md and collect project info."""
    records = []

    for project_dir in sorted(p for p in projects_dir.iterdir() if p.is_dir()):
        description_path = project_dir / "description.md"
        if not description_path.is_file():
            continue

        fields = parse_description(description_path)
        fields["Directory"] = str(project_dir.relative_to(projects_dir))
        records.append(fields)

    columns = ["Title", "Subfield", "Topics Covered", "Project Type", "Directory"]
    return pd.DataFrame(records, columns=columns)


def generate_markdown(df: pd.DataFrame) -> str:
    """Render the project index as a Markdown document grouped by subfield."""
    lines = ["# Cookbook Research Projects Compendium", ""]

    for subfield, group in df.groupby("Subfield", dropna=False, sort=True):
        subfield_name = subfield if pd.notna(subfield) else "Uncategorized"
        lines.append(f"## {subfield_name}")
        lines.append("")

        for _, project in group.sort_values("Title").iterrows():
            description_link = f"{PROJECTS_DIR_NAME}/{project['Directory']}/description.md"
            lines.append(f"### [{project['Title']}]({description_link})")
            lines.append(f"- **Topics Covered:** {project['Topics Covered']}")
            lines.append(f"- **Project Type:** {project['Project Type']}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    df = build_project_index(PROJECTS_DIR)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Wrote {len(df)} project(s) to {OUTPUT_CSV}")

    markdown = generate_markdown(df)
    OUTPUT_MARKDOWN.write_text(markdown, encoding="utf-8")
    print(f"Wrote compendium markdown to {OUTPUT_MARKDOWN}")


if __name__ == "__main__":
    main()
