# Repository Backend

This directory contains the tooling used to maintain the [Cookbook Research Projects](../Cookbook%20Research%20Projects) collection and to build [Compendium.md](../Compendium.md), the repo's project index.

## Adding a new project

1. Create a new directory under `Cookbook Research Projects/` (do **not** prefix it with an underscore — see [Excluding a directory](#excluding-a-directory)).
2. Copy [`_repotemplate/description_template.md`](../Cookbook%20Research%20Projects/_repotemplate/description_template.md) into your new directory and rename it to `README.md`.
3. Fill in the README following the format below.
4. Add any project files (notebooks, data, scripts, etc.) to the directory.
5. Run `compendium.py` (see [Updating the compendium](#updating-the-compendium)) to regenerate the project index.

## README.md format

Each project's `README.md` must follow the structure of the template so `compendium.py` can parse it correctly:

```markdown
# Title: <Project Title>
Original Author: <Name>
*Subfield: <Subfield>*
*Topics covered: <Topic 1, Topic 2, ...>*
*Type of project: <Type>*

## Short Description:
<A few sentences describing the project.>

## Materials
Project files can be found at <link or path>.
```

The parser looks for these exact fields (each on its own line):

- `# Title: ...`
- `*Subfield: ...*`
- `*Topics covered: ...*`
- `*Type of project: ...*`

If a field is missing or doesn't match this format, it will show up as blank in the compendium.

## Excluding a directory

Any directory in `Cookbook Research Projects/` whose name starts with an underscore (e.g. `_repotemplate`, `_old`) is ignored when building the compendium, even if it contains a `README.md`. Use this prefix for templates, archives, or other non-project folders.

## Updating the compendium

Run the following from the repository root whenever a project is added, removed, or its `README.md` is updated:

```powershell
python "Repository Backend/compendium.py"
```

This script:

1. Scans each subdirectory of `Cookbook Research Projects/` (skipping underscore-prefixed directories) for a `README.md`.
2. Parses the Title, Subfield, Topics Covered, and Project Type from each README.
3. Writes the full project index to `Repository Backend/compendium.csv`.
4. Generates `Compendium.md` at the repository root, grouping projects by Subfield with links to each project's directory.

Commit the updated `compendium.csv` and `Compendium.md` along with your project changes.
