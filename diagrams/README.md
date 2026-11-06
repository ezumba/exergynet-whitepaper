# diagrams/

Architecture diagrams for ExergyNet V5.

---

## Files

| File | Format | Description |
|------|--------|-------------|
| `public-architecture.mmd` | Mermaid | High-level V5 architecture — public components only |

---

## Rendering

Diagrams are written in [Mermaid](https://mermaid.js.org/) format (`.mmd`).

### Options for rendering:

**GitHub:** Mermaid renders natively in GitHub Markdown when embedded in a
`.md` file using a fenced code block:

````markdown
```mermaid
<diagram content>
```
````

**CLI:**
```bash
npx @mermaid-js/mermaid-cli -i public-architecture.mmd -o public-architecture.svg
```

**VS Code:** Install the "Markdown Preview Mermaid Support" extension.

---

## Disclosure Note

These diagrams show only the public architectural structure documented in V5.
Production topology, routing internals, authority gate implementation details,
and LNES subsystem architecture are not represented.
