# Security Policy

This repository contains a published scientific white paper and associated
documentation. It does not contain executable production software.

---

## Scope

**In scope:**
- Accidental disclosure of private information (credentials, keys, internal
  paths, unreleased data) in any tracked file, commit, or Git history.
- Errors in the SHA-256 verification scripts that could cause false integrity
  verification results.
- Incorrect PDF hash values that could cause a modified document to be
  accepted as authentic.

**Out of scope:**
- Vulnerabilities in the ExergyNet production platform.
- Security issues in the portal (`portal.exergynet.org`).
- API security issues.

For production platform security, refer to the ExergyNet security contact at
[https://exergynet.org/security.html](https://exergynet.org/security.html).

---

## Reporting a Disclosure Issue

If you discover that this repository accidentally contains private, sensitive,
or restricted information, **do not open a public issue.**

Contact the authors through the ExergyNet platform at
[https://exergynet.org](https://exergynet.org).

Include:
- The file path or commit reference containing the sensitive content.
- A description of what was exposed (do not reproduce the sensitive content
  in your report).
- Your contact information for follow-up.

We will respond within 48 hours and take appropriate remediation action,
which may include removing content from Git history.

---

## PDF Integrity

The canonical SHA-256 for the V5 PDF is:

```
416974f1d7c1f4d569866027e2ff7a58d7480ed80b87738d8203feb6e518b0eb
```

If you download the PDF and the hash does not match, do not use the file.
Report the discrepancy as a security issue using the contact above.
