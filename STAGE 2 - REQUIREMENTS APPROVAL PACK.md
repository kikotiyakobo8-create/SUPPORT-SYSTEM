# Stage 2 — Requirements Approval Pack

**Project:** Technical Support Management System (TSMS)  
**Baseline candidate:** SRS version 1.0, dated 14 October 2026  
**Supporting document:** Stage 1 — Requirements Validation Pack  
**Status:** Pending stakeholder decisions and formal approval

## 1. Purpose

This pack turns the reviewed SRS into an approval-ready baseline. It must be completed by the client before detailed system design begins. Once signed, the baseline controls scope; later changes must follow the change-management process in the SRS.

## 2. Approval gate

The SRS can be marked **Approved for Design** only when all items below are complete:

- Stage 1 validation results have been reviewed and changes to the SRS have been recorded.
- Every required decision in section 3 has an approved answer or an explicit, time-bound deferral that does not block design.
- The company has named its SRS approver and user-acceptance-test approver.
- The approved release-1 scope, exclusions, and acceptance criteria are accepted.
- All named approvers sign section 7.

**Current gate status: Not ready for approval.** The source SRS and Stage 1 pack contain no stakeholder decisions or signatures yet.

## 3. Required decision record

Complete the "Approved decision" and "Approver" columns. If a decision changes an SRS requirement, identify the affected SRS section and update the next SRS version before signing.

| ID | Decision required | Approved decision | SRS impact / section | Approver | Date |
| --- | --- | --- | --- | --- | --- |
| D-01 | Technical Supervisor and Management / Report Viewer role | | 2.3 | | |
| D-02 | TSMS-managed accounts or company-directory integration | | 4.1 | | |
| D-03 | Working days, hours, holidays, maintenance periods, and after-hours submission | | 2.5, 5.5 | | |
| D-04 | Impact and urgency definitions; priority matrix; priority override authority | | 4.5, 6.3 | | |
| D-05 | Final ticket statuses and permitted status transitions | | 4.8, 6.7 | | |
| D-06 | Internal-note visibility and prohibited/confidential ticket content | | 4.6, 5.3 | | |
| D-07 | Reopening review process, time limit, and decline/new-ticket rules | | 4.9, 6.6 | | |
| D-08 | Notification events, recipients, and refresh-based first-release behaviour | | 4.10 | | |
| D-09 | Launch categories, category ownership, and attachments decision | | 4.2, 4.12 | | |
| D-10 | Required reports, filters, and CSV/spreadsheet export | | 4.11 | | |
| D-11 | Hosting option, budget, maintenance owner, and data-location policy | | 2.2, 14 | | |
| D-12 | Backup frequency, retention, recovery-time objective, and acceptable data loss | | 5.6 | | |
| D-13 | Ticket, audit, notification, and attachment retention; deletion/export process | | 5.3, 7.3 | | |
| D-14 | Supported browsers, minimum device dimensions, and measurable performance/availability targets | | 2.4, 5.4, 5.5 | | |
| D-15 | Authority for SRS and UAT approval | | 15, 16 | | |

## 4. Scope confirmation

The approver confirms that release 1 includes the following capabilities:

| Capability group | Confirmed? | Comments / approved change |
| --- | --- | --- |
| Authentication, password recovery, user accounts, roles, and backend authorization | | |
| Ticket submission, unique reference, validation, category, status, and ownership | | |
| Ticket views, search, filtering, record-level authorization, and history | | |
| Assignment, reassignment, queues, impact/urgency, suggested priority, and recorded overrides | | |
| Work notes, escalation records, resolution, closure, and reopening requests | | |
| In-app notifications and notification authorization | | |
| Basic reports, audit trail, categories, and approved configuration | | |
| Responsive browser support, security controls, backup/recovery, deployment, and documentation | | |

The approver also confirms that the following remain excluded unless approved through a change request: native apps; email/SMS/WhatsApp notifications; external-specialist accounts; remote-control features; asset inventory; AI diagnosis; complex SLA automation; advanced BI; and unapproved integrations.

## 5. Acceptance criteria confirmation

The client confirms that acceptance will be demonstrated through the SRS criteria AC-01 to AC-17, including:

- Desktop and smartphone ticket submission.
- Record-level access protection.
- Assignment, priority, escalation, notification, closure, and reopening history.
- Accurate, authorized reporting.
- Backup restoration, approved performance/availability testing, documentation, UAT, and resolution of critical defects before launch.

| Acceptance criteria set | Accepted? | Approved changes or clarifications |
| --- | --- | --- |
| AC-01 to AC-10: principal ticket workflows | | |
| AC-11 to AC-12: reports and administration authorization | | |
| AC-13 to AC-17: operations, quality, acceptance, and launch | | |

## 6. Baseline-change record

Record every modification agreed during Stage 1 or Stage 2. Do not overwrite the original SRS without preserving its version history.

| Change ID | Source requirement / section | Approved change | Reason | Scope, cost, schedule, security, or test impact | Approved by | Date |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |
| | | | | | | |
| | | | | | | |

## 7. Formal approval

By signing below, the parties approve the updated SRS baseline for detailed system design. Approval means the documented requirements are understood and accepted; it does not authorize unrecorded scope changes.

| Approval role | Name | Signature | Date |
| --- | --- | --- | --- |
| Authorized company sponsor / SRS approver | | | |
| Technical Team representative | | | |
| System Administrator representative | | | |
| Management/reporting representative, if applicable | | | |
| Development team representative | | | |

## 8. Stage 2 completion output

When signed, produce the following controlled artifacts:

1. **SRS version 1.1 — Approved**, incorporating approved decisions and the change record.
2. A completed copy of this approval pack.
3. A requirements traceability matrix linking SRS requirements to design, build, and test evidence.
4. Authorization to start **Stage 3: System Design**.

Until those artifacts exist, TSMS must remain in requirements validation/approval and must not be represented as an approved implementation baseline.

