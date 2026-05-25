# 🔍 Vibe Code Audit — Popular But Broken

> AI projects with many stars but poor code quality, security issues, or broken architecture.
> We identify the issues and propose fixes. Learn from others' mistakes.

## What is "Vibe Coding"?

Vibe coding = building software by prompting AI without understanding the code. Results in:
- Many GitHub stars (good marketing)
- Poor code quality (AI-generated spaghetti)
- Security vulnerabilities (no review)
- Missing tests (AI doesn't write good tests)
- Broken architecture (no design, just prompts)
- Abandoned maintenance (no understanding = no fixes)

## How We Audit

For each project, we check:
1. **Code quality** — Is it readable? Maintainable? DRY?
2. **Security** — SQL injection, XSS, hardcoded secrets, etc.
3. **Tests** — Are there tests? Do they pass?
4. **Architecture** — Is there a clear design pattern?
5. **Dependencies** — Are they up to date? Any known vulnerabilities?
6. **Documentation** — Is it accurate? Complete?
7. **CI/CD** — Is there automated testing/deployment?
8. **License** — Is there one? Is it appropriate?

## Audited Projects

_(Being populated — we're scanning the top 1000 AI projects on GitHub)_

### Template

#### [Project Name](URL)
- **Stars:** X
- **Language:** X
- **Issues found:**
  - 🔴 Critical: [description]
  - 🟡 Medium: [description]
  - 🟢 Minor: [description]
- **Proposed fixes:**
  - [specific fix]
- **Verdict:** [Keep using / Use with caution / Avoid]

---

## Common Patterns in Vibe-Coded Projects

### 1. The "Single File Monster"
Everything in one 5000-line file. No modules, no separation of concerns.
**Fix:** Refactor into modules, use proper project structure.

### 2. The "Hardcoded Secrets"
API keys, database credentials, and tokens committed to the repo.
**Fix:** Use environment variables, .env files, secret management.

### 3. The "No Error Handling"
Every function assumes success. No try/catch, no validation.
**Fix:** Add proper error handling, input validation, graceful degradation.

### 4. The "Copy-Paste Architecture"
Code copied from Stack Overflow and tutorials without understanding.
**Fix:** Understand the code, refactor for the specific use case.

### 5. The "Missing Tests"
Zero test coverage. "It works on my machine."
**Fix:** Add unit tests, integration tests, CI/CD pipeline.

### 6. The "Dependency Hell"
200+ dependencies, many unused, some with known CVEs.
**Fix:** Audit dependencies, remove unused ones, update vulnerable ones.

### 7. The "No License"
No LICENSE file. Legally unclear if you can use it.
**Fix:** Add an appropriate open-source license.

### 8. The "Abandoned Abandoned"
Last commit 2 years ago. Open issues piling up. No responses.
**Fix:** Fork and maintain, or find an alternative.

---

## Our Improvement Projects

For each vibe-coded project we audit, we create an improved version:

| Original | Our Improved Version | Improvements |
|----------|---------------------|--------------|
| _(Coming soon)_ | _(Coming soon)_ | _(Coming soon)_ |

---

*Last updated: 2026-05-25*
