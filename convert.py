from pathlib import Path

src = Path("category-ai-!cn.list").read_text(
encoding="utf-8"
).splitlines()

out = []

for line in src:
line = line.strip()

```
if not line:
    continue

if line.startswith("#"):
    continue

if line.startswith("+."):
    out.append(
        f"DOMAIN-SUFFIX,{line[2:]}"
    )

elif line.startswith("."):
    out.append(
        f"DOMAIN-SUFFIX,{line[1:]}"
    )

else:
    out.append(
        f"DOMAIN,{line}"
    )
```

# 去重

out = list(dict.fromkeys(out))

header = [
"# NAME: AI Rules",
"# AUTHOR: YourName",
"# UPDATED: auto",
f"# TOTAL: {len(out)}",
""
]

Path("shadowrocket.list").write_text(
"\n".join(header + out),
encoding="utf-8"
)

print("done")
