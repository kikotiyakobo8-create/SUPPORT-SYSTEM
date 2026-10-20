# Stage 1 — Requirements Validation Pack

**Project:** Technical Support Management System (TSMS)  
**Source:** Software Requirements Specification (SRS), version 1.0 draft, 14 October 2026  
**Purpose:** Provide the stakeholder review material needed to validate the proposed requirements before they become an approved baseline.

## 1. Validation outcome sought

At the end of Stage 1, the company representative, Technical Team, employee representatives, and system administrator should agree on:

1. The business problem TSMS will solve.
2. The user roles and who is authorized for each role.
3. The first-release scope and exclusions.
4. The ticket workflow, including assignment, priorities, escalation, closure, and reopening.
5. The information captured in tickets and who may see it.
6. Required notifications and reports.
7. The decisions that must be finalized in Stage 2 before implementation begins.

**Stage 1 does not approve implementation.** It records agreement, disagreement, assumptions, and decisions still required for formal SRS approval.

## 2. Proposed baseline for stakeholder validation

### 2.1 Business need

The current informal, in-person support process does not provide a dependable record of requests, work, priorities, escalations, outcomes, or technician workload. TSMS will provide a single internal web system through which employees submit technical issues and the Technical Team manages them to closure.

### 2.2 Users and access boundaries

| Role | Main responsibilities | Required access boundary |
| --- | --- | --- |
| Employee / Requester | Submit, track, add information, request reopening | Own tickets and permitted updates only |
| Support Technician | Work tickets, record notes, update status, escalate, resolve and close | Authorized support queue and assigned tickets |
| Technical Supervisor | Oversee queues, allocations, priorities, escalations, and reports | Support operations and approved reports |
| System Administrator | Manage accounts, roles, categories, and configuration | Administrative functions only; ticket access must be explicitly authorized |
| Management / Report Viewer | Review approved reports | Read-only reports only |

External specialists will not receive accounts in release 1. The Technical Team will record and coordinate their involvement internally.

### 2.3 First-release functions proposed for confirmation

- Sign-in, sign-out, password recovery, user administration, and role-based access control.
- Employee ticket submission with a stable unique reference, category, description, and initial status.
- Employee view of their own tickets, status, permitted updates, and notifications.
- Technician queues, assignment/reassignment, search, filters, impact/urgency capture, and suggested priority.
- Recorded priority overrides, investigation/work notes, escalation records, resolution, closure, and reopening requests.
- In-app notifications, audit trail, category/configuration administration, and basic operational reports.
- Backup/recovery procedures, deployment documentation, and user documentation.

### 2.4 Explicitly excluded from release 1

- Native mobile applications.
- Email, SMS, WhatsApp, or real-time push notifications.
- External-specialist accounts.
- Remote-control tools, equipment inventory, AI diagnosis, complex SLA automation, extensive BI dashboards, and directory integration unless separately approved.

## 3. Proposed workflow to validate

```text
Employee submits ticket
        |
        v
Submitted / Open --> Assigned --> In Progress --> Resolved --> Closed
                         |             |              |
                         |             +--> Waiting for Information
                         |             +--> Escalated
                         |
                         +--> Reassigned

Closed --> Reopening Requested --> technician review --> reopen same ticket or record a new ticket
```

The exact state names and permitted transitions remain subject to approval. A resolution must be recorded before closure, and historical records must never be silently overwritten.

## 4. Stakeholder validation workshop

**Suggested attendees:** company sponsor/approver, all three technicians, representative employees, proposed system administrator, management report consumer, and development representative.

**Suggested duration:** 2–3 hours, followed by written confirmation of decisions.

| Topic | Questions to validate | Expected Stage 1 output |
| --- | --- | --- |
| Current support process | What happens today from report to closure? What workarounds exist? | Agreed current-state process and pain points |
| Roles | Who fills each role? Can a technician also supervise? Is a report-viewer role needed? | Initial role list and owners |
| Ticket intake | What information is mandatory? Which categories exist? Are screenshots needed? | Ticket form and initial category proposal |
| Workflow | Which statuses are needed? Who assigns, resolves, closes, and approves reopenings? | Draft state-transition rules |
| Priority | How are impact, urgency, and critical incidents assessed? | Draft impact/urgency definitions and matrix |
| Visibility | Which notes are internal-only? What information must never be entered? | Visibility and confidentiality rules |
| Notifications | Which events matter and who should see each event? | Notification-event matrix |
| Reports | What decisions must reports support? | Prioritized report list and measures |
| Operations | Who administers accounts, hosting, backups, and outage communication? | Named operational owners and open decisions |

## 5. Requirements validation checklist

Mark each item **Confirmed**, **Change requested**, **Deferred**, or **Not applicable** during the review.

| Area | Validation statement | Status | Notes / decision |
| --- | --- | --- | --- |
| Problem | A centralized auditable support process is required. | Pending | |
| Scope | The proposed release-1 inclusions are accepted. | Pending | |
| Scope | Release-1 exclusions are accepted. | Pending | |
| Roles | Proposed roles and record-level access boundaries are accepted. | Pending | |
| Ticket intake | Description, category, impact, and urgency fields are appropriate. | Pending | |
| Workflow | Proposed lifecycle and invalid-transition controls are appropriate. | Pending | |
| Assignment | Authorized assignment/reassignment rules are correct. | Pending | |
| Priority | Suggested-priority and override-recording requirements are accepted. | Pending | |
| Notes | Work notes and their requester visibility are defined. | Pending | |
| Escalation | Internal tracking of external specialists is sufficient. | Pending | |
| Closure | Resolution-before-closure and technician closure are accepted. | Pending | |
| Reopening | Employee reopening requests and review process are accepted in principle. | Pending | |
| Notifications | In-app notifications are sufficient for release 1. | Pending | |
| Reports | The proposed basic reports meet management's initial needs. | Pending | |
| Security | Backend RBAC, record-level authorization, audit, and HTTPS are mandatory. | Pending | |
| Data | Retention, privacy, and attachment requirements need formal policy decisions. | Pending | |
| Operations | Backup/recovery, hosting, maintenance, and outage ownership need confirmation. | Pending | |

## 6. Decision register for Stage 2

The following decisions block a fully approved requirements baseline. Each needs an owner, decision date, and recorded answer.

| ID | Decision | Why it matters | Suggested owner | Status |
| --- | --- | --- | --- | --- |
| D-01 | Name Technical Supervisor and determine whether a report-viewer role is needed. | Defines permissions and workflows. | Company sponsor | Open |
| D-02 | Choose TSMS-managed accounts or company-directory integration. | Affects authentication design and cost. | Sponsor / IT | Open |
| D-03 | Define workdays, work hours, holidays, maintenance periods, and out-of-hours submission handling. | Required for availability and timing calculations. | Management | Open |
| D-04 | Approve impact, urgency, priority definitions, mapping, and override authority. | Required for consistent prioritization. | Technical Supervisor / Management | Open |
| D-05 | Approve final statuses and permitted transitions. | Required to enforce workflow safely. | Technical Team | Open |
| D-06 | Decide which ticket notes are internal-only and prohibited ticket content. | Required for confidentiality and UI design. | Management / IT | Open |
| D-07 | Approve reopening rules, review authority, time limit, and decline process. | Required to avoid duplicate work and unclear histories. | Technical Team / Management | Open |
| D-08 | Approve notification events, recipients, and whether refresh-based delivery is sufficient. | Defines notification behaviour. | Technical Team | Open |
| D-09 | Approve launch categories, their administrator, and whether attachments are needed. | Defines ticket form and security controls. | Technical Team | Open |
| D-10 | Prioritize reports and decide whether CSV/spreadsheet export is required. | Defines reporting scope. | Management | Open |
| D-11 | Choose hosting, maintenance owner, data-location constraints, and budget. | Required for deployment architecture. | Management / IT | Open |
| D-12 | Set backup frequency, retention, recovery-time and data-loss targets. | Required for operational acceptance. | Management / IT | Open |
| D-13 | Set ticket/audit/notification retention policy and deletion/export procedures. | Required for data governance. | Management | Open |
| D-14 | Approve supported browsers, minimum device sizes, and measurable performance targets. | Required for testable acceptance criteria. | Sponsor / IT | Open |
| D-15 | Name the authority who approves the SRS and user acceptance testing. | Required for formal governance. | Management | Open |

## 7. Initial acceptance-test traceability

| Validation outcome | SRS acceptance evidence |
| --- | --- |
| Employees can submit and track tickets on desktop and smartphone. | AC-01, AC-02 |
| Employees cannot view other employees' tickets. | AC-03 |
| Assignment, priority, escalation, closure, reopening, and notifications preserve history. | AC-04 to AC-10 |
| Reports and backend administration are correct and authorized. | AC-11, AC-12 |
| Data can be restored and service meets agreed targets. | AC-13 to AC-17 |

## 8. Stage 1 completion record

Stage 1 is complete when the validation workshop has been held, the checklist above has a recorded result for every line, and unresolved items have been transferred to the Stage 2 decision log.

| Field | Record |
| --- | --- |
| Validation workshop date | |
| Company sponsor / representative | |
| Technical Team representatives | |
| Employee representatives | |
| System administrator representative | |
| Key changes requested to SRS | |
| Decisions completed | |
| Decisions deferred to Stage 2 | |
| Prepared by | Development team |
| Review status | Pending stakeholder validation |

