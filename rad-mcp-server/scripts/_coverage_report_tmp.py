import json
import pathlib

ref = pathlib.Path("skills/rad-cli-operations/references")

families = []
for p in ref.glob("command-tree-*.md"):
    fam = p.name[len("command-tree-") : -3]
    if (ref / ("cli-help-" + fam + ".jsonl")).exists():
        families.append(fam)
families.sort()

for fam in families:
    tree_lines = (ref / ("command-tree-" + fam + ".md")).read_text(encoding="utf-8").splitlines()
    data = [
        json.loads(l)
        for l in (ref / ("cli-help-" + fam + ".jsonl")).read_text(encoding="utf-8").splitlines()
        if l.strip()
    ]

    levels = {d["context"] for d in data if d.get("kind") == "level"}
    captures = {(d["context"], d.get("prefix", "")) for d in data if d.get("prefix", "") != ""}
    noenter = [d for d in data if d.get("kind") == "args-noenter"]

    nodes = []
    for line in tree_lines:
        i = line.find("+---")
        if i < 0:
            continue
        depth = i // 4
        name = line[i + 4 :].strip()
        if not name:
            continue
        nodes.append((depth, name))

    stack = []
    entries = []
    for i, (depth, name) in enumerate(nodes):
        while len(stack) > depth:
            stack.pop()
        stack.append(name)
        is_context = i + 1 < len(nodes) and nodes[i + 1][0] > depth
        entries.append((tuple(stack), is_context))

    missing_ctx = []
    missing_leaf = []
    for path, is_context in entries:
        if path == ("|",):
            continue
        full = " ".join(path)
        if is_context:
            if full not in levels:
                missing_ctx.append(full)
        else:
            parent = " ".join(path[:-1]) or "<root>"
            pref = path[-1]
            if (parent, pref) not in captures:
                missing_leaf.append((parent, pref))

    print(
        f"FAMILY {fam}: noenter={len(noenter)} missing_ctx={len(missing_ctx)} missing_leaf={len(missing_leaf)} total_records={len(data)}"
    )

    for d in noenter:
        print("NOENTER", fam, "::", d.get("context", ""), "::", d.get("prefix", ""))
