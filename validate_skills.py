"""Check each skill folder against Lovable's import limits."""
import pathlib, re, sys

NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
errors = []
for skill in sorted(p.parent for p in pathlib.Path(__file__).parent.glob("*/SKILL.md")):
    text = (skill / "SKILL.md").read_text()
    m = re.match(r"^---\nname: (.+)\ndescription: (.+)\n---\n", text)
    if not m:
        errors.append(f"{skill.name}: bad frontmatter"); continue
    name, desc = m.groups()
    if name != skill.name or not NAME.match(name) or len(name) > 64:
        errors.append(f"{skill.name}: bad name {name!r}")
    if not desc.startswith("Use when") or len(desc) > 1024:
        errors.append(f"{skill.name}: description must start 'Use when' and be <=1024 chars")
    if len(text) > 100_000:
        errors.append(f"{skill.name}: SKILL.md over 100,000 chars")
    files = [f for f in skill.rglob("*") if f.is_file()]
    if len(files) > 200 or sum(f.stat().st_size for f in files) > 10_000_000:
        errors.append(f"{skill.name}: over 200 files or 10 MB")
    errors += [f"{skill.name}: {f.name} over 1 MB" for f in files if f.stat().st_size > 1_000_000]
    for link in re.findall(r"\]\(([^)#]+\.md)\)", text):
        if not (skill / link).exists():
            errors.append(f"{skill.name}: broken link {link}")
    print(f"ok  {name}  ({len(text)} chars, {len(files)} files)")
print("\n".join(errors) or "all skills pass")
sys.exit(1 if errors else 0)
