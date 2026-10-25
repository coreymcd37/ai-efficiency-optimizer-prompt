# Security Checklist

An expanded version of the security checklist in [SKILL.md](../SKILL.md) for cloud, agent, or automation setups. Go through it before you run anything that touches real data, money, or accounts.

## Access

- [ ] Least-privilege access: each key, account, or agent can do only what its job needs.
- [ ] Separate accounts or keys per project, so one leak doesn't expose everything.
- [ ] Master credentials are never shared.
- [ ] Multi-factor authentication is on for every account involved.

## Secrets

- [ ] Secrets live in a secret manager or environment variables.
- [ ] No secrets in prompts, code, chat, logs, or shared files.
- [ ] `.env` files are listed in `.gitignore`.

## Spending

- [ ] Billing alerts are set.
- [ ] Spending caps are on.
- [ ] Retry limits and a cost ceiling are defined. If something fails twice, change approach.

## Untrusted input

- [ ] Web pages, files, and tool outputs are treated as untrusted data, because they can contain hidden instructions.
- [ ] Irreversible actions (spending, deleting, sending, publishing) require confirmation.

## Data handling

- [ ] Sensitive data (personal, financial, medical, legal, credentials, confidential) isn't sent to a third party without the user's informed OK.
- [ ] Each service's data retention, training-on-your-data policy, and storage location have been checked.
- [ ] Local processing is used for sensitive work where practical.

## Operations

- [ ] Agent actions are logged.
- [ ] Time and cost limits are set.
- [ ] Changes are tested on copies of data first.
- [ ] Backups exist and there's an undo path.

## Red flags

Stop and reconsider if any of these apply:

- Sensitive data would leave the user's control without consent.
- A "free" option demands data, rights, or unlimited access.
- Costs scale with usage and there's no cap or alert.
- The plan depends on bypassing a login, paywall, license, or terms of service.
