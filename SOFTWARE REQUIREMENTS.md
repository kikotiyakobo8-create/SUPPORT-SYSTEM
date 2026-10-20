# SOFTWARE REQUIREMENTS SPECIFICATION (SRS)

PRELIMINARY PROJECT DOCUMENT — FOR CLIENT REVIEW AND APPROVAL

# Technical Support Management System (TSMS)

Document version

Version 1.0 — Draft

Date

14 October 2026

Prepared for

A company with approximately 30 employees

Project team

System analyst and development team

Document status: Proposed requirements pending stakeholder validation. Version 1.0 identifies the complete proposed baseline; it does not mean the client has approved it.

## Document purpose

This Software Requirements Specification defines the proposed requirements for a web-based Technical Support Management System (TSMS). It establishes what the system should do, who will use it, how support requests will be handled, what information will be recorded, how the system will be secured, and how the completed system will be evaluated.

The document is intended to guide system analysis, system design, implementation, testing, deployment, and future maintenance. It also provides a basis for the client to approve the project's scope before development begins.

Some operational policies, such as exact working hours, priority definitions, data-retention periods, and hosting arrangements, have not yet been confirmed. They are identified as decisions requiring client approval rather than treated as established facts.

# 1. Introduction

## 1.1 Background

The company has approximately 30 employees and a Technical Team (TT) consisting of three people.

Currently, when an employee experiences a technical problem, the employee normally has to physically visit the Technical Team's room to report the problem. A technician may then travel to the employee's workstation or office to investigate and resolve it.

Some technical problems cannot be solved internally and require assistance from an external specialist. In these cases, the Technical Team coordinates the assistance and follows up on the issue.

Although this arrangement enables employees to receive support, it creates operational difficulties. Employees and technicians spend time moving between offices, support requests are not centrally recorded, and management lacks reliable information about the volume, progress, and outcomes of technical support activities.

The company therefore needs a centralized system that makes it easier to report technical problems and manage them systematically.

## 1.2 Problem statement

The existing technical support process relies mainly on physical communication and informal follow-up. There is no formal, centralized record of every support request, its priority, assignment, investigation, escalation, resolution, and closure.

Consequently:

- Employees may experience delays when reporting problems or obtaining updates.
- Technicians may find it difficult to track all pending and ongoing requests.
- Urgent problems may not be prioritized consistently.
- Requests may be forgotten, duplicated, or followed up inefficiently.
- Escalations to external specialists may be difficult to track.
- Management cannot reliably measure response times, resolution times, recurring problems, or technician workload.
- The company lacks dependable historical information for evaluating and improving technical support services.

A digital system is required to address these challenges by maintaining a complete, accessible, and auditable record of technical support activities.

## 1.3 Proposed solution

The proposed solution is a responsive web-based Technical Support Management System.

Employees will submit support requests through a browser on a computer or smartphone. The system will generate a unique ticket reference and store the request in a centralized database.

The Technical Team will use a shared workspace to view, assign, prioritize, investigate, escalate, resolve, and close tickets. Employees will be able to check the progress of their own requests and ask for a ticket to be reopened when a problem remains unresolved or returns.

The system will also provide in-app notifications and basic reports to help management evaluate technical support operations.

## 1.4 Purpose of the system

The purpose of TSMS is to improve the efficiency, accountability, accessibility, and measurability of technical support services within the company.

## 1.5 Project objectives

The system shall aim to:

1. Provide a convenient way for employees to report technical problems without physically visiting the Technical Team merely to submit a request.
2. Assign a unique reference number to every support ticket.
3. Centralize support requests and their related records.
4. Help the Technical Team prioritize and allocate work efficiently.
5. Record investigations, actions taken, specialist assistance, resolutions, and closures.
6. Enable employees to track the progress of their own tickets.
7. Provide in-app notifications about relevant ticket events.
8. Preserve the history of important ticket changes and decisions.
9. Produce reports showing ticket volume, status, response time, resolution time, escalations, and workload.
10. Support evidence-based decisions about improving technical support.
11. Protect company information through authentication, authorization, and appropriate operational controls.
12. Deliver an affordable, maintainable first release without unnecessary features.

## 1.6 Success criteria

The project will be considered successful when the approved system can:

- Record support requests centrally.
- Generate unique ticket references.
- Enforce user permissions correctly.
- Support ticket assignment and priority management.
- Preserve investigation and escalation history.
- Record resolutions, closures, and reopening requests.
- Notify the correct users through the application.
- Generate accurate reports from stored records.
- Operate on the agreed desktop and smartphone browsers.
- Restore data successfully from a backup.
- Meet the performance and availability targets approved by the company.
- Be used by employees and the Technical Team in a controlled pilot.

Numerical targets, such as maximum response time or acceptable system downtime, must be agreed before acceptance testing.

## 1.7 Definitions and abbreviations

| Term                       | Definition                                                                                                  |
| -------------------------- | ----------------------------------------------------------------------------------------------------------- |
| TSMS                       | Technical Support Management System                                                                         |
| TT                         | Technical Team                                                                                              |
| SRS                        | Software Requirements Specification                                                                         |
| Ticket                     | A recorded technical support request or incident                                                            |
| Requester                  | An employee who submits a support ticket                                                                    |
| Technician                 | A Technical Team member who investigates and resolves tickets                                               |
| Technical Supervisor       | An authorized person who oversees assignments, priorities, escalations, and technical support operations    |
| System Administrator       | A person responsible for user accounts, system configuration, and administration                            |
| Management / Report Viewer | An authorized user who reviews operational reports                                                          |
| Priority                   | The relative order in which a ticket should receive attention                                               |
| Impact                     | The extent to which an incident affects users, services, or business operations                             |
| Urgency                    | How quickly an incident needs attention                                                                     |
| Escalation                 | A recorded request for additional or specialist assistance                                                  |
| Resolution                 | The recorded outcome or solution for a technical problem                                                    |
| Closure                    | The administrative completion of a ticket under the approved workflow                                       |
| RBAC                       | Role-Based Access Control                                                                                   |
| Audit trail                | A chronological record of important actions and changes                                                     |
| In-app notification        | A message displayed inside TSMS                                                                             |
| Response time              | The elapsed time between submission and the first qualifying support response, as defined by company policy |
| Resolution time            | The elapsed time between submission and recorded resolution, using an agreed calculation rule               |

# 2. Overall system description

## 2.1 Product perspective

TSMS will be a new internal business application for managing technical support requests.

It will consist of three principal technical components:

1. Frontend: The user interface through which employees, technicians, supervisors, administrators, and authorized report viewers interact with the system.
2. Backend: The application logic responsible for authentication, permissions, ticket workflows, priority suggestions, notifications, reports, and validation.
3. Database: The persistent storage for users, tickets, assignments, status history, work notes, escalations, notifications, and other system records.

The frontend will communicate with the backend through an API. The backend will access the database to create, retrieve, and update information.

## 2.2 Proposed technology stack

The following technologies are recommended for initial evaluation.

| Component         | Proposed technology                                                           | Reason                                                                                     |
| ----------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Frontend          | React.js                                                                      | Supports a responsive and maintainable browser interface                                   |
| Backend           | Django                                                                        | Provides application structure, authentication facilities, and administrative capabilities |
| API               | Django REST Framework                                                         | Supports communication between frontend and backend                                        |
| Database          | PostgreSQL                                                                    | Provides relational data storage, transactions, and access-control capabilities            |
| Web communication | HTTPS                                                                         | Protects information transmitted between browsers and the server                           |
| Authentication    | Secure application-managed authentication or an approved identity integration | Allows controlled access to the application                                                |
| Hosting           | Low-cost managed cloud hosting, subject to evaluation                         | Potentially reduces the need to maintain dedicated application-server hardware             |
| Notifications     | Database-backed in-app notifications                                          | Avoids external messaging-service costs in the first release                               |

The final technology and hosting decisions must consider total cost, security, maintainability, staff capabilities, company policy, backup arrangements, and the requirements of the selected deployment environment.

## 2.3 User classes and proposed roles

The system will use role-based access control. Permissions will be enforced by the backend rather than relying only on which buttons are displayed in the frontend.

### 2.3.1 Employee / Requester

Employees will use the system to:

- Sign in and sign out.
- Submit technical support tickets.
- Receive a unique ticket reference.
- View the status and history of their own tickets.
- Provide additional information when requested.
- Receive relevant in-app notifications.
- Request reopening of a closed ticket.

Employees must not be able to view another employee's restricted ticket simply by changing a ticket reference, URL, or API request.

### 2.3.2 Support Technician

Technicians will use the system to:

- View tickets in their authorized support queue.
- View assigned tickets.
- Investigate reported problems.
- Record work performed and findings.
- Update ticket statuses.
- Assign or reassign tickets where authorized.
- Review system-suggested priorities.
- Adjust priorities where authorized and record reasons.
- Record specialist escalations and follow-up.
- Record resolutions and close tickets.
- Review reopening requests.

### 2.3.3 Technical Supervisor

The Technical Supervisor role is proposed for overseeing technical support operations.

Its responsibilities may include:

- Monitoring the support queue.
- Assigning and reassigning tickets.
- Reviewing priority decisions.
- Monitoring overdue or unassigned tickets.
- Reviewing escalations.
- Monitoring technician workload.
- Accessing operational reports.
- Reviewing reopening decisions where required by company policy.

The company must confirm whether one of the three technicians will perform this role or whether it will be assigned to another employee.

### 2.3.4 System Administrator

The System Administrator will be responsible for:

- Creating and maintaining user accounts.
- Assigning approved roles.
- Deactivating accounts when access is no longer required.
- Managing ticket categories and approved configuration values.
- Maintaining system settings.
- Reviewing operational administration information.
- Supporting deployment, backups, and maintenance according to assigned responsibilities.

Administrative permissions must be limited to authorized users. Technical administration should not automatically grant unrestricted access to all confidential business information unless that access is explicitly authorized.

### 2.3.5 Management / Report Viewer

Management may require read-only access to reports that show:

- Ticket volume.
- Open, resolved, closed, and escalated tickets.
- Response and resolution times.
- Technician workload.
- Common problem categories.
- Trends over selected periods.

A separate Management / Report Viewer role should be implemented only if the company confirms that it is necessary. Alternatively, authorized supervisors may provide the required reports.

### 2.3.6 External specialists

External specialists will not have TSMS accounts in the first release.

The Technical Team will remain responsible for coordinating specialist assistance and recording:

- The reason for escalation.
- The assistance requested.
- The date and time of the escalation.
- The internal technician responsible.
- Follow-up actions.
- The specialist's response or findings, where available.
- The final outcome.

## 2.4 Operating environment

The application shall be designed for:

- Desktop and laptop computers.
- Smartphones with supported web browsers.
- Reliable internet access.
- A centrally hosted or otherwise approved application server.
- A supported relational database.
- Secure browser-to-server communication.

The company must approve the browser versions and minimum device requirements before final testing.

## 2.5 General operating constraints

The system must account for the following:

- Approximately 30 employees and three Technical Team members.
- A very limited development and hosting budget.
- Reliable internet connectivity.
- Access through a responsive web application.
- Support during normal company working hours.
- In-app notifications only in the first release.
- Technician-controlled ticket closure.
- Employee requests to reopen closed tickets.
- Internal management of external specialist escalations.
- A need for secure storage, backups, and maintainable deployment.

## 2.6 Assumptions and dependencies

The initial requirements assume that:

1. The company will appoint a representative authorized to approve requirements.
2. The company will provide the list of initial users and their approved roles.
3. The company will define working hours and relevant support policies.
4. The company will approve ticket categories and impact/urgency rules.
5. The company will identify who maintains the deployed application.
6. The company will approve how long support records are retained.
7. The company will decide whether attachments are necessary.
8. The company will approve the selected hosting arrangement.
9. Users will have supported devices and network access.
10. The Technical Team will be responsible for the internal management of specialist escalations.

# 3. System scope

## 3.1 Features included in the first release

The first release shall include:

1. User authentication.
2. Role-based permissions.
3. User-account administration.
4. Ticket submission.
5. Unique ticket references.
6. Ticket status tracking.
7. Technician ticket queues.
8. Assignment and reassignment.
9. Impact and urgency capture.
10. System-suggested priority.
11. Authorized priority overrides with recorded reasons.
12. Investigation and work notes.
13. Escalation records.
14. Resolution and technician closure.
15. Employee reopening requests.
16. In-app notifications.
17. Basic management reports.
18. Ticket history and audit records.
19. Backup and recovery procedures.
20. Deployment and user documentation.

## 3.2 Features excluded from the first release

Unless separately approved, the first release will not include:

- Native Android or iOS applications.
- Email, SMS, or WhatsApp notifications.
- External specialist accounts.
- Remote desktop or remote-control features.
- AI-based diagnosis or automated repair.
- Computer and equipment asset inventory.
- Complex SLA automation and contractual penalty management.
- Extensive business intelligence dashboards.
- Advanced real-time notification delivery.
- Complex integration with an existing company directory.
- A comprehensive knowledge base beyond any explicitly approved basic content.

These exclusions are intended to keep the first release focused and affordable.

## 3.3 Potential future enhancements

After the first release has been evaluated, the company may consider:

- A searchable knowledge base.
- Live notification updates.
- Equipment inventory management.
- Email or messaging integrations.
- Advanced performance and trend reports.
- External specialist collaboration features.
- Additional automation and SLA monitoring.

Any future enhancement must be assessed and approved separately.

# 4. Functional requirements

Functional requirements describe the actions and behavior the system must support.

Priority labels:

- Must: Required for the proposed first release.
- Should: Desirable if the approved budget and schedule allow.
- Proposed: Requires confirmation or a policy decision.

## 4.1 Authentication and user management

| ID    | Requirement                                                                                                        | Priority                   |
| ----- | ------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| FR-01 | The system shall allow authorized users to sign in securely.                                                       | Must                       |
| FR-02 | The system shall allow authenticated users to sign out.                                                            | Must                       |
| FR-03 | The system shall enforce role-based permissions on the backend.                                                    | Must                       |
| FR-04 | The system shall prevent unauthorized access to protected functions and records.                                   | Must                       |
| FR-05 | The administrator shall be able to create and update user accounts.                                                | Must                       |
| FR-06 | The administrator shall be able to assign approved roles to users.                                                 | Must                       |
| FR-07 | The administrator shall be able to deactivate user accounts without deleting associated historical ticket records. | Must                       |
| FR-08 | The system shall provide an approved password reset and account recovery process.                                  | Must                       |
| FR-09 | The system shall record important account and permission changes in an audit trail.                                | Must                       |
| FR-10 | The system should support integration with an existing company identity provider if required and approved.         | Should / Decision required |

Open decision: The company must determine whether users will have accounts managed directly in TSMS or use an existing company directory.

## 4.2 Ticket submission

| ID    | Requirement                                                                                                | Priority          |
| ----- | ---------------------------------------------------------------------------------------------------------- | ----------------- |
| FR-11 | An authenticated employee shall be able to submit a technical support request through a supported browser. | Must              |
| FR-12 | The system shall generate a unique reference for each ticket.                                              | Must              |
| FR-13 | The system shall record the requester and submission timestamp.                                            | Must              |
| FR-14 | The system shall record a description of the reported problem.                                             | Must              |
| FR-15 | The system shall associate each ticket with an approved category.                                          | Must              |
| FR-16 | The system shall assign an initial status to a new ticket.                                                 | Must              |
| FR-17 | The system should collect impact and urgency information using approved choices.                           | Should            |
| FR-18 | The system shall validate required fields before saving a ticket.                                          | Must              |
| FR-19 | The system shall provide understandable validation messages when submission fails.                         | Must              |
| FR-20 | The system should support attachments if the client approves file requirements and security controls.      | Decision required |

## 4.3 Ticket viewing and tracking

| ID    | Requirement                                                                                                               | Priority |
| ----- | ------------------------------------------------------------------------------------------------------------------------- | -------- |
| FR-21 | Employees shall be able to view their own tickets.                                                                        | Must     |
| FR-22 | Employees shall be able to view the status of their own tickets.                                                          | Must     |
| FR-23 | Employees shall be able to view relevant updates and outcomes on their tickets.                                           | Must     |
| FR-24 | Technicians shall be able to view tickets permitted by their role and support responsibilities.                           | Must     |
| FR-25 | Authorized users shall be able to search tickets using the unique reference.                                              | Must     |
| FR-26 | Authorized users shall be able to filter tickets by agreed fields such as status, category, priority, date, and assignee. | Must     |
| FR-27 | The system shall retain ticket history when assignments, priorities, or statuses change.                                  | Must     |
| FR-28 | The system shall enforce record-level authorization for ticket details and related API endpoints.                         | Must     |

## 4.4 Ticket assignment

| ID    | Requirement                                                                                        | Priority |
| ----- | -------------------------------------------------------------------------------------------------- | -------- |
| FR-29 | Authorized users shall be able to assign tickets to technicians.                                   | Must     |
| FR-30 | Authorized users shall be able to reassign tickets when necessary.                                 | Must     |
| FR-31 | The system shall record assignment and reassignment events.                                        | Must     |
| FR-32 | The system shall record who made an assignment change and when it occurred.                        | Must     |
| FR-33 | Assigned tickets shall appear in the appropriate technician's queue.                               | Must     |
| FR-34 | The system should provide a queue view showing unassigned and pending tickets to authorized users. | Should   |

## 4.5 Priority management

| ID    | Requirement                                                                                             | Priority          |
| ----- | ------------------------------------------------------------------------------------------------------- | ----------------- |
| FR-35 | The system shall support the approved impact and urgency levels.                                        | Must              |
| FR-36 | The system shall suggest a priority based on the approved impact/urgency rules.                         | Must              |
| FR-37 | An authorized technician or supervisor shall be able to adjust a suggested priority where permitted.    | Must              |
| FR-38 | A priority override shall record the old value, new value, user, timestamp, and reason.                 | Must              |
| FR-39 | The system shall display priority clearly in the authorized ticket queue.                               | Must              |
| FR-40 | The system should allow a supervisor to review priority overrides if the company requires this control. | Decision required |

### 4.5.1 Proposed priority levels

The following levels are proposed for discussion:

- Critical: Severe disruption to essential operations or multiple users.
- High: Significant impact on work or an important service.
- Normal: An issue affecting ordinary work, potentially with a workaround.
- Low: A minor issue or request that can wait behind more urgent work.

These definitions are not final until approved by the company.

### 4.5.2 Priority decision rules

The company must approve:

- The meaning of each impact level.
- The meaning of each urgency level.
- The mapping between impact/urgency combinations and suggested priority.
- Which users may override priorities.
- Whether priority downgrades require supervisor approval.
- How critical incidents outside normal working hours are handled.

## 4.6 Technician investigation and work records

| ID    | Requirement                                                                                             | Priority |
| ----- | ------------------------------------------------------------------------------------------------------- | -------- |
| FR-41 | Technicians shall be able to record investigation steps.                                                | Must     |
| FR-42 | Technicians shall be able to record work performed.                                                     | Must     |
| FR-43 | Technicians shall be able to record relevant findings and diagnostic outcomes.                          | Must     |
| FR-44 | Technicians shall be able to update ticket status according to the approved workflow.                   | Must     |
| FR-45 | The system shall record the author and timestamp of work notes.                                         | Must     |
| FR-46 | The system shall preserve historical work records instead of silently overwriting previous entries.     | Must     |
| FR-47 | The system should support a request for more information from the employee if approved in the workflow. | Should   |

The company must determine whether any work notes should be internal-only and hidden from requesters.

## 4.7 Escalation management

| ID    | Requirement                                                                                  | Priority               |
| ----- | -------------------------------------------------------------------------------------------- | ---------------------- |
| FR-48 | The Technical Team shall be able to record a ticket escalation.                              | Must                   |
| FR-49 | An escalation shall record the reason for seeking additional assistance.                     | Must                   |
| FR-50 | An escalation shall record the assistance requested.                                         | Must                   |
| FR-51 | The system shall record the responsible internal technician.                                 | Must                   |
| FR-52 | The system shall support recording follow-up actions and outcomes.                           | Must                   |
| FR-53 | Escalation records shall remain linked to the original ticket.                               | Must                   |
| FR-54 | The system shall preserve the escalation history.                                            | Must                   |
| FR-55 | The Technical Team shall remain responsible for coordinating external specialist assistance. | Must                   |
| FR-56 | The first release shall not require external specialist accounts.                            | Must for scope control |

## 4.8 Ticket status, resolution, and closure

| ID    | Requirement                                                                                               | Priority |
| ----- | --------------------------------------------------------------------------------------------------------- | -------- |
| FR-57 | Every ticket shall have a status.                                                                         | Must     |
| FR-58 | The system shall record ticket status changes with actor and timestamp.                                   | Must     |
| FR-59 | The system shall support the client-approved ticket lifecycle.                                            | Must     |
| FR-60 | A technician shall record the resolution before completing the ticket according to the approved workflow. | Must     |
| FR-61 | The system shall record the closure timestamp when a ticket is closed.                                    | Must     |
| FR-62 | The system shall preserve resolution and closure history.                                                 | Must     |
| FR-63 | The system shall prevent invalid status transitions defined by the approved workflow.                     | Must     |

### 4.8.1 Proposed ticket lifecycle

The proposed lifecycle is:

Submitted → Open / Assigned → In Progress → Escalated or Waiting, when applicable → Resolved → Closed

A ticket may move between investigation and waiting/escalation states when required. Exact status names and permitted transitions must be agreed before implementation.

## 4.9 Reopening requests

| ID    | Requirement                                                                                           | Priority          |
| ----- | ----------------------------------------------------------------------------------------------------- | ----------------- |
| FR-64 | An employee shall be able to request reopening of a closed ticket.                                    | Must              |
| FR-65 | The system shall record the reopening request and its reason.                                         | Must              |
| FR-66 | The system shall record the requester and timestamp.                                                  | Must              |
| FR-67 | The system shall notify the appropriate authorized support user about the request.                    | Must              |
| FR-68 | The system shall preserve the original ticket reference and history.                                  | Must              |
| FR-69 | The system shall follow the approved rule for reopening the original ticket or creating a new ticket. | Decision required |

Proposed approach: A technician reviews the reopening request and decides whether to reopen the same ticket or document why a new ticket is needed. The company must approve this approach, any time limit, and whether supervisor approval is required.

## 4.10 In-app notifications

| ID    | Requirement                                                                | Priority               |
| ----- | -------------------------------------------------------------------------- | ---------------------- |
| FR-70 | The system shall create in-app notifications for agreed ticket events.     | Must                   |
| FR-71 | Notifications shall identify the event that occurred.                      | Must                   |
| FR-72 | Notifications may link to the related ticket when appropriate.             | Must                   |
| FR-73 | The system shall check authorization before displaying a linked ticket.    | Must                   |
| FR-74 | The system should indicate whether a notification has been read.           | Should                 |
| FR-75 | The first release shall not require email, SMS, or WhatsApp notifications. | Must for scope control |

Proposed notification events include:

- Ticket assignment.
- Relevant ticket status changes.
- Requests for additional information.
- Relevant escalation updates.
- Resolution or closure.
- Reopening requests.

The company must approve which events trigger notifications and who receives them.

The initial implementation may store notifications in the database and display them when a user loads or refreshes the application. Real-time updates may be introduced later if required.

## 4.11 Reporting and management information

| ID    | Requirement                                                                                             | Priority |
| ----- | ------------------------------------------------------------------------------------------------------- | -------- |
| FR-76 | Authorized users shall be able to view ticket-volume reports for a selected period.                     | Must     |
| FR-77 | The system shall show counts of open, resolved, closed, and escalated tickets using agreed definitions. | Must     |
| FR-78 | The system shall calculate response times using the approved definition.                                | Must     |
| FR-79 | The system shall calculate resolution times using the approved definition.                              | Must     |
| FR-80 | The system should provide workload summaries by technician.                                             | Should   |
| FR-81 | The system should show common or recurring ticket categories.                                           | Should   |
| FR-82 | The system should support date-range filters for reports.                                               | Should   |
| FR-83 | Reports shall be available only to authorized roles.                                                    | Must     |
| FR-84 | Report calculations shall be based on stored ticket records and agreed calculation rules.               | Must     |

The company must decide whether reports need downloadable CSV or spreadsheet exports. Export functionality is not assumed to be mandatory in the first release.

## 4.12 Administration and configuration

| ID    | Requirement                                                             | Priority |
| ----- | ----------------------------------------------------------------------- | -------- |
| FR-85 | An authorized administrator shall be able to manage ticket categories.  | Must     |
| FR-86 | The system shall apply approved impact/urgency priority rules.          | Must     |
| FR-87 | Important configuration changes should be recorded in the audit trail.  | Should   |
| FR-88 | The system shall restrict administrative functions to authorized users. | Must     |

## 4.13 Audit trail and data integrity

| ID    | Requirement                                                                                             | Priority |
| ----- | ------------------------------------------------------------------------------------------------------- | -------- |
| FR-89 | The system shall record ticket creation.                                                                | Must     |
| FR-90 | The system shall record assignment, reassignment, priority, and status changes.                         | Must     |
| FR-91 | The system shall record escalations, resolution, closure, and reopening requests.                       | Must     |
| FR-92 | Audit events shall identify the actor and timestamp.                                                    | Must     |
| FR-93 | Relevant changes shall preserve previous and new values where appropriate.                              | Must     |
| FR-94 | Ordinary users shall not be able to alter or delete audit history through normal application functions. | Must     |
| FR-95 | Deactivating a user shall not remove historical ticket activity.                                        | Must     |

# 5. Non-functional requirements

Non-functional requirements describe the expected quality, security, reliability, and operating characteristics of the system.

## 5.1 Usability

- NFR-01: The system shall provide a responsive interface for supported desktop and smartphone browsers.
- NFR-02: Ticket submission shall use clear labels and understandable instructions.
- NFR-03: The ticket-submission process should require as few steps as reasonably possible.
- NFR-04: Statuses, priorities, and categories shall use consistent labels.
- NFR-05: Validation errors shall explain how the user can correct the problem.
- NFR-06: The interface should avoid relying on color alone to communicate priority or status.
- NFR-07: Navigation shall be appropriate to the user's authorized role.

## 5.2 Security

- NFR-08: Production traffic shall be protected using HTTPS.
- NFR-09: Authentication and authorization shall be enforced on the backend.
- NFR-10: The system shall validate user input on the server.
- NFR-11: The system shall prevent unauthorized access to other employees' restricted tickets.
- NFR-12: Passwords and authentication secrets shall be handled using established secure practices.
- NFR-13: Secrets and production credentials shall not be hard-coded into source code or committed to the repository.
- NFR-14: Error messages shall not disclose passwords, tokens, secret settings, or unnecessary personal information.
- NFR-15: The system shall be configured and tested to reduce common web-application vulnerabilities.
- NFR-16: Administrative permissions shall be granted only to approved users.
- NFR-17: Security updates shall be applied under an agreed maintenance process.
- NFR-18: Access to backups and production data shall be restricted.
- NFR-19: Any file attachment functionality shall include appropriate validation, storage, and access controls.

## 5.3 Privacy and confidentiality

- NFR-20: Ticket information shall be accessible only to users authorized to view it.
- NFR-21: The company shall define which information may be entered in ticket descriptions and work notes.
- NFR-22: Internal work notes, if implemented, shall be distinguishable from information visible to requesters.
- NFR-23: Personal and confidential information shall be retained only according to the company's approved policy and applicable obligations.
- NFR-24: Data export and deletion procedures shall be defined before production use.

## 5.4 Performance

- NFR-25: The system shall support the expected population of approximately 30 employees and three technicians under normal use.
- NFR-26: Ticket lists shall use suitable pagination and filtering.
- NFR-27: The system shall use appropriate database queries and indexes where needed.
- NFR-28: The client and development team shall agree measurable response-time targets for ticket submission, ticket-list loading, ticket-detail loading, and basic reports.
- NFR-29: Performance shall be tested with representative data before acceptance.

Exact response-time limits remain to be agreed. They must not be treated as passed or guaranteed until tested in the target environment.

## 5.5 Availability

- NFR-30: The system shall be available during the company's approved working hours, subject to agreed hosting and maintenance arrangements.
- NFR-31: The company shall define working days, working hours, holidays, and planned maintenance periods.
- NFR-32: The company shall decide whether employees may submit tickets outside working hours and how those tickets are handled.
- NFR-33: The deployment shall have a documented process for handling outages.
- NFR-34: The company shall define the acceptable availability target before operational acceptance.

## 5.6 Backup and recovery

- NFR-35: The system shall have a documented backup procedure for the database and any stored attachments.
- NFR-36: Backup frequency and retention periods shall be approved by the company.
- NFR-37: Backup data shall be protected from unauthorized access.
- NFR-38: Backup copies should be stored separately from the primary data where feasible.
- NFR-39: A controlled restoration test shall be completed before operational acceptance.
- NFR-40: The company shall define acceptable data loss and service restoration time.
- NFR-41: Restoration procedures shall be documented and tested periodically.

## 5.7 Maintainability

- NFR-42: The application shall use a documented and maintainable code structure.
- NFR-43: Source code, database migrations, deployment instructions, and configuration guidance shall be maintained.
- NFR-44: Development, testing, and production settings shall be appropriately separated.
- NFR-45: The system shall use supported dependencies and a documented update process.
- NFR-46: The company shall identify who is responsible for application maintenance after launch.
- NFR-47: The system should be deployable to another compatible environment without rewriting its core business logic.

## 5.8 Auditability

- NFR-48: Important ticket and administrative events shall be traceable to an actor or system process and timestamp.
- NFR-49: Historical records shall be protected against unauthorized modification.
- NFR-50: Ticket and audit retention shall follow an approved company policy.
- NFR-51: Audit records shall contain only the information necessary for accountability and operational investigation.

## 5.9 Cost effectiveness

- NFR-52: The solution shall minimize unnecessary recurring expenses.
- NFR-53: Paid hosting and third-party services shall be disclosed and approved before purchase.
- NFR-54: Security, backup, and recovery requirements shall not be removed solely to reduce costs.
- NFR-55: The first release shall focus on essential ticket-management functions and defer nonessential integrations.

# 6. Business rules and ticket workflows

## 6.1 Ticket creation rules

1. Only authenticated and authorized employees may submit tickets.
2. Each successfully created ticket must have a unique reference.
3. A ticket must identify its requester and creation time.
4. Required information must be validated before the ticket is saved.
5. Each ticket must have an initial status.
6. Ticket history must be preserved after creation.
7. A ticket reference must remain stable throughout the ticket's lifecycle.

## 6.2 Assignment rules

1. Only authorized users may assign or reassign tickets.
2. Assignment changes must be recorded.
3. The assigned technician must be able to find the ticket in the appropriate queue.
4. Reassignment must not erase the previous assignment history.
5. Notifications about assignments shall follow the approved notification policy.

## 6.3 Priority rules

1. The system will suggest a priority based on the approved impact/urgency matrix.
2. Authorized technicians may adjust the suggested priority according to company policy.
3. Every priority override must record the previous value, new value, actor, timestamp, and reason.
4. The final priority definitions and matrix must be approved before implementation.
5. Any special handling of critical incidents outside working hours must be documented.

## 6.4 Investigation rules

1. Technicians shall record relevant work performed and findings.
2. Status changes shall be recorded with the actor and timestamp.
3. Historical work records must remain available according to retention policy.
4. A ticket awaiting external assistance must remain linked to its original record.
5. The system must distinguish resolution from closure if the approved workflow treats them as separate events.

## 6.5 Escalation rules

1. The Technical Team remains responsible for managing external specialist assistance.
2. Every escalation must be associated with the original ticket.
3. The reason for escalation and assistance requested must be recorded.
4. Follow-up actions and outcomes must be recorded as information becomes available.
5. Escalation history must not be lost when a ticket is resolved or closed.

## 6.6 Closure and reopening rules

1. A technician closes a ticket according to the approved workflow.
2. Resolution details must be recorded before closure.
3. The system records the closure timestamp.
4. An employee may request reopening of a closed ticket.
5. The reopening request must contain a reason and be recorded in the ticket history.
6. The system must follow the client-approved review process.
7. Reopening a ticket must not silently erase its previous resolution or closure history.

## 6.7 Proposed status model

The following status model is recommended for discussion:

| Status                  | Meaning                                                        |
| ----------------------- | -------------------------------------------------------------- |
| Submitted               | A new ticket has been recorded                                 |
| Open                    | The ticket is awaiting assignment or further action            |
| Assigned                | A technician has been assigned                                 |
| In Progress             | Investigation or work is underway                              |
| Waiting for Information | Additional information is required, if this status is approved |
| Escalated               | Additional or specialist assistance is required                |
| Resolved                | A resolution has been recorded                                 |
| Closed                  | The technician has completed the closure process               |
| Reopening Requested     | The employee has requested further work on a closed ticket     |

The final list may be simplified. The company must approve which statuses are necessary and which transitions are allowed.

# 7. Preliminary data requirements

## 7.1 Main data entities

The following entities are proposed for the system's database design.

| Entity            | Purpose                                     | Example attributes                                                                                    |
| ----------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| User              | Stores authorized user information          | User ID, name, username, role, active status                                                          |
| Ticket            | Stores the main support request             | Ticket ID, reference, requester, description, category, impact, urgency, priority, status, timestamps |
| Ticket Assignment | Records assignment history                  | Ticket, technician, assigned by, assigned time                                                        |
| Ticket Activity   | Records ticket events                       | Ticket, actor, event type, timestamp, change details                                                  |
| Work Note         | Records investigation and work performed    | Ticket, author, note, timestamp, visibility                                                           |
| Escalation        | Records additional or specialist assistance | Ticket, reason, requested assistance, internal owner, follow-up, outcome                              |
| Notification      | Stores in-app notifications                 | Recipient, event, related ticket, created time, read status                                           |
| Category          | Defines ticket categories                   | Category ID, name, description, active status                                                         |
| Priority Rule     | Stores impact/urgency mapping               | Impact, urgency, suggested priority                                                                   |
| Reopening Request | Stores requests to reopen closed tickets    | Ticket, requester, reason, request time, review outcome                                               |
| Audit Event       | Records important system events             | Actor, action, target record, timestamp, change details                                               |
| System Setting    | Stores approved configuration values        | Setting name, value, updated by, updated time                                                         |

These are logical entities. The final database may combine or separate some entities during detailed design, provided that the approved requirements are met.

## 7.2 Data integrity rules

- Every ticket must have a unique reference.
- Every ticket must be associated with a requester.
- Ticket assignment, priority, and status changes must be traceable.
- Escalations must be linked to their original tickets.
- User deactivation must not delete historic ticket activity.
- Notifications must be linked to the correct recipient and, where relevant, ticket.
- Users must not access records solely by guessing identifiers.
- Date and time values must be stored and displayed consistently.
- Records must be retained or disposed of according to the approved retention policy.
- Attachments, if implemented, must be subject to approved security and storage rules.

## 7.3 Data retention

The company must specify how long it needs to retain:

- Tickets.
- Work notes.
- Escalation records.
- Notifications.
- Audit events.
- Attachments, if supported.
- Backup copies.

The system must support the approved policy without deleting records that need to be retained for accountability, operational analysis, or applicable obligations.

# 8. External interface requirements

## 8.1 User interface

The system shall provide the following principal screens:

1. Sign-in screen: Allows authorized users to access the system.
2. Employee dashboard: Displays the employee's own tickets and relevant notifications.
3. Ticket submission screen: Allows employees to report technical problems.
4. Ticket detail screen: Displays the ticket information, permitted history, and current status.
5. Technician dashboard: Displays the support queue and assigned work.
6. Ticket management workspace: Allows authorized technicians to record work, update status, manage escalations, and resolve tickets.
7. Assignment and priority controls: Allow authorized users to allocate work and manage priority.
8. Notification area: Displays in-app notifications.
9. Reporting screen: Displays approved operational reports.
10. Administration screens: Allow authorized administrators to manage users, roles, categories, and approved configuration.

Detailed page layouts, navigation, and visual design will be prepared during the system-design phase.

## 8.2 Software interfaces

- The React frontend shall communicate with the backend through an authenticated API.
- The backend shall validate requests and enforce permissions.
- The backend shall interact with the selected relational database.
- The deployed application shall use secure communication.
- Any additional external integration must be separately approved.

## 8.3 Hardware and network interfaces

The first release does not require a specialized hardware interface. Users require a compatible device, supported browser, and network/internet access.

The final hosting environment must meet the system's agreed storage, performance, security, backup, and availability requirements.

# 9. Use cases

## 9.1 Use Case 1: Submit a technical support ticket

Primary actor: Employee.

Preconditions:

- The employee has an active account.
- The employee is authenticated.

Main flow:

1. The employee opens the ticket-submission page.
2. The employee enters the problem description.
3. The employee selects the relevant category.
4. The employee provides any required impact and urgency information.
5. The system validates the submitted information.
6. The system creates the ticket.
7. The system generates a unique ticket reference.
8. The system saves the ticket and its initial status.
9. The system displays the reference to the employee.
10. The system creates any approved notifications.

Alternative flow: If required information is missing or invalid, the system explains the problem and asks the employee to correct it.

Postcondition: The ticket is saved and visible to authorized support users.

## 9.2 Use Case 2: Assign and prioritize a ticket

Primary actor: Authorized technician or Technical Supervisor.

Preconditions:

- The ticket exists.
- The actor has permission to assign or modify the ticket.

Main flow:

1. The actor opens the support queue.
2. The system displays relevant ticket information and suggested priority.
3. The actor selects a ticket.
4. The actor assigns or reassigns the ticket.
5. If required, the actor adjusts its priority and provides a reason.
6. The system records the changes.
7. The system updates the appropriate queue.
8. The system creates approved notifications.

Postcondition: The ticket has an updated assignment and priority, with history preserved.

## 9.3 Use Case 3: Investigate and resolve a ticket

Primary actor: Support Technician.

Preconditions:

- The ticket exists.
- The technician is authorized to work on it.

Main flow:

1. The technician opens the ticket.
2. The technician reviews the problem description.
3. The technician investigates the problem.
4. The technician records relevant work and findings.
5. The technician updates the ticket status.
6. If additional assistance is required, the technician records an escalation.
7. The technician records the resolution.
8. The technician closes the ticket according to the approved workflow.
9. The system preserves the relevant history and timestamps.
10. The system creates approved notifications.

Postcondition: The ticket has a recorded outcome and closure state.

## 9.4 Use Case 4: Manage a specialist escalation

Primary actor: Support Technician.

Preconditions:

- A ticket exists.
- The technician determines that additional assistance is needed.

Main flow:

1. The technician opens the ticket.
2. The technician creates an escalation record.
3. The technician records the reason and assistance requested.
4. The technician records the internal owner and follow-up details.
5. The Technical Team coordinates the external assistance.
6. The technician records new findings and outcomes.
7. The system preserves the escalation history against the original ticket.

Postcondition: Specialist involvement is traceable within the original support record.

## 9.5 Use Case 5: Request reopening of a closed ticket

Primary actor: Employee.

Preconditions:

- The employee can access the ticket.
- The ticket is closed.

Main flow:

1. The employee opens the ticket.
2. The employee selects the reopening-request option.
3. The employee provides a reason.
4. The system records the request.
5. The system notifies the appropriate support user.
6. An authorized technician reviews the request.
7. The technician follows the approved reopening rule.
8. The system preserves the original history.

Postcondition: The reopening request and its outcome are recorded.

## 9.6 Use Case 6: View management reports

Primary actor: Technical Supervisor or authorized report viewer.

Preconditions:

- The user has reporting permission.
- Ticket data exists.

Main flow:

1. The user opens the reports section.
2. The user selects a date range and available filters.
3. The system retrieves relevant ticket data.
4. The system calculates the requested measures.
5. The system displays the results.

Postcondition: Authorized users can inspect support operations using recorded data.

## 9.7 Use Case 7: Manage users and categories

Primary actor: System Administrator.

Preconditions:

- The administrator is authenticated.
- The administrator has the necessary permissions.

Main flow:

1. The administrator opens the relevant management screen.
2. The administrator creates or updates an account, role, category, or approved setting.
3. The system validates the change.
4. The system saves the change.
5. The system records important administrative activity.

Postcondition: The approved configuration is updated and traceable.

# 10. Acceptance criteria

Acceptance criteria define the evidence required to determine whether the implemented system satisfies the agreed requirements.

| ID    | Acceptance criterion                                                                                                         |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| AC-01 | An authorized employee can submit a valid ticket through a desktop browser, and the system saves it with a unique reference. |
| AC-02 | An authorized employee can submit a valid ticket through a supported smartphone browser.                                     |
| AC-03 | An employee cannot access another employee's restricted ticket by changing a URL, ticket reference, or API request.          |
| AC-04 | An authorized assignment is saved and the ticket appears in the appropriate technician queue.                                |
| AC-05 | Approved impact/urgency combinations produce the expected suggested priority.                                                |
| AC-06 | A permitted priority override records the previous value, new value, actor, timestamp, and reason.                           |
| AC-07 | An escalation records its reason, assistance requested, follow-up, and outcome against the original ticket.                  |
| AC-08 | An approved ticket event creates an in-app notification for the correct authorized recipient.                                |
| AC-09 | Resolution and closure details and timestamps are preserved in the ticket history.                                           |
| AC-10 | An employee can submit a reopening request, and the request is recorded and processed using the approved workflow.           |
| AC-11 | An authorized report for a selected date range matches the underlying ticket records under the agreed calculation rules.     |
| AC-12 | Unauthorized administrative actions are rejected by the backend.                                                             |
| AC-13 | A backup can be restored successfully in a controlled test before production acceptance.                                     |
| AC-14 | The system meets the approved performance and availability targets during the agreed test period.                            |
| AC-15 | The company receives the agreed deployment, administrator, backup, and recovery documentation.                               |
| AC-16 | The system's principal workflows pass the approved user acceptance tests.                                                    |
| AC-17 | Critical security and workflow defects are resolved before production launch.                                                |

These criteria must be mapped to detailed test cases during testing. A criterion is not considered passed merely because the feature appears on the screen; the relevant behavior must be tested.

# 11. Preliminary risks and mitigation measures

| Risk                                             | Potential impact                                         | Proposed mitigation                                               |
| ------------------------------------------------ | -------------------------------------------------------- | ----------------------------------------------------------------- |
| Requirements are not agreed before coding        | Rework, delays, and disagreement about expected behavior | Review and approve the SRS before detailed implementation         |
| Limited budget                                   | Hosting and maintenance become unsustainable             | Compare total costs and focus on essential features               |
| Unauthorized ticket access                       | Exposure of internal or personal information             | Enforce server-side permissions and test record-level access      |
| Data loss                                        | Loss of ticket history and management information        | Implement backups and test restoration                            |
| Incomplete ticket records                        | Reports become unreliable                                | Use clear categories, validation, and user guidance               |
| Employees continue using only informal reporting | The system lacks complete support records                | Train users and agree the official process for submitting tickets |
| Unclear priority definitions                     | Inconsistent handling of incidents                       | Approve an impact/urgency matrix and override policy              |
| Unclear reopening process                        | Duplicate work and disagreement                          | Approve a reopening workflow                                      |
| Unclear maintenance ownership                    | Security updates and backups may be missed               | Assign operational responsibilities before launch                 |
| Hosting or internet outage                       | Users cannot access the application                      | Define an outage fallback and suitable recovery arrangements      |
| Excessive scope                                  | Increased cost and delayed delivery                      | Keep first release focused and control changes                    |
| Inappropriate information in tickets             | Confidentiality or privacy concerns                      | Define acceptable ticket content and retention rules              |

# 12. Testing and quality assurance

The system shall be tested at several levels.

## 12.1 Unit testing

Individual functions and business rules will be tested, including:

- Ticket reference generation.
- Required-field validation.
- Priority suggestions.
- Status transition rules.
- Notification creation.
- Report calculations.
- Authorization helper logic.

## 12.2 API testing

The backend API will be tested for:

- Successful authorized requests.
- Rejected unauthorized requests.
- Input validation.
- Ticket creation and updates.
- Assignment and priority changes.
- Escalation management.
- Closure and reopening requests.
- Notification permissions.
- Report accuracy.

## 12.3 Integration testing

Testing will verify that the frontend, backend, database, and notification functions work together correctly.

## 12.4 Security testing

Security testing shall include:

- Attempting to access another employee's ticket.
- Attempting unauthorized administrative actions.
- Testing role permissions.
- Testing invalid and unexpected input.
- Checking production configuration and secret handling.
- Verifying that protected data is not exposed through errors or logs.

## 12.5 Responsive testing

The system shall be tested on the agreed desktop and smartphone browsers and screen sizes.

## 12.6 Workflow testing

The team shall test complete scenarios for:

- Ticket submission.
- Assignment and reassignment.
- Priority suggestions and overrides.
- Investigation.
- Escalation.
- Resolution.
- Closure.
- Reopening requests.
- Notifications.
- Reporting.

## 12.7 Backup and restoration testing

A controlled test shall demonstrate that the approved backup process can restore the necessary data and that restored tickets remain consistent.

## 12.8 User acceptance testing

Selected employees, technicians, supervisors, and report viewers shall execute agreed real-world scenarios.

The client will review the results, report defects, and formally accept the system when the approved criteria are satisfied.

## 12.9 Pilot testing

Before company-wide use, a small approved group should test the system in a controlled pilot. Feedback should be collected and important defects corrected before full deployment.

# 13. Deployment, maintenance, and operational requirements

Before production deployment, the company and development team must agree on:

1. The hosting environment.
2. The owner of the hosting account.
3. Domain or subdomain arrangements.
4. HTTPS configuration.
5. Database deployment and access restrictions.
6. Production secrets and configuration management.
7. The people authorized to deploy updates.
8. Backup frequency and retention.
9. Restoration procedures.
10. Monitoring and outage response.
11. Security and dependency updates.
12. User account administration.
13. Initial user training.
14. Post-launch support and defect reporting.
15. The fallback process for reporting urgent issues during an outage.

The production environment must be configured securely. Development settings, debug output, test accounts, and development credentials must not be exposed in production.

# 14. Hosting recommendation

The company has reliable internet connectivity and a very limited budget. A low-cost managed cloud deployment is a reasonable leading option to evaluate, but it should not be selected automatically without comparing costs and risks.

## 14.1 Option A: Cloud hosting

Potential advantages:

- Users can access the system from supported devices and locations with internet access.
- The company may not need to purchase and maintain dedicated application-server hardware.
- Some providers offer managed database, backup, and infrastructure features.

Potential disadvantages:

- Hosting and storage may incur recurring costs.
- Access depends on internet connectivity and provider availability.
- The company must assess data location, privacy, and provider policies.
- The application still needs secure configuration, updates, backups, and maintenance.
- Low-cost plans may have limitations that affect recovery or reliability.

## 14.2 Option B: Local or on-premises hosting

Potential advantages:

- The company has greater direct control over where its application data is stored.
- Existing infrastructure may be usable if it meets the requirements.

Potential disadvantages:

- Suitable hardware, power, networking, and physical security are required.
- The company must maintain the server, database, backups, and security updates.
- A hardware or power failure may make the application unavailable.
- Remote access may require additional secure configuration.
- Initial purchase and ongoing maintenance costs may exceed those of an appropriate cloud option.

## 14.3 Recommended decision

The company should:

1. Estimate total monthly and annual costs for both options.
2. Identify any company rules governing data location and external hosting.
3. Confirm who will maintain the application and infrastructure.
4. Compare backup, recovery, and availability capabilities.
5. Confirm whether the company already has suitable infrastructure that can be maintained safely.
6. Choose the lowest-cost option that meets the approved security and recovery requirements.
7. Document the decision and obtain management approval.

Recommendation: Evaluate a modest cloud deployment first, but finalize the hosting decision only after cost, security, data-policy, and maintenance checks.

# 15. Outstanding questions requiring client decisions

The following questions must be answered before the requirements baseline can be considered fully approved.

| ID    | Area                  | Decision required                                                                                              |
| ----- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| OQ-01 | Roles                 | Who will serve as Technical Supervisor? Is a separate Management / Report Viewer account required?             |
| OQ-02 | Accounts              | Will TSMS manage its own accounts, or integrate with an existing company directory?                            |
| OQ-03 | Working hours         | What are the exact working days, start and end times, holidays, and maintenance periods?                       |
| OQ-04 | Out-of-hours support  | May employees submit tickets outside working hours? How should those tickets be handled?                       |
| OQ-05 | Critical incidents    | What should happen when a critical incident occurs outside working hours?                                      |
| OQ-06 | Service targets       | Are response and resolution targets required for each priority? If so, what are they?                          |
| OQ-07 | Priority rules        | What impact and urgency levels and priority mapping should be used?                                            |
| OQ-08 | Priority overrides    | Who can override priorities? Do downgrades require supervisor approval?                                        |
| OQ-09 | Notifications         | Which events trigger notifications, and who receives each notification?                                        |
| OQ-10 | Notification behavior | Is notification display on page load/refresh sufficient for the first release?                                 |
| OQ-11 | Hosting               | What recurring hosting cost is affordable? Who will maintain the application and hosting environment?          |
| OQ-12 | Backup and recovery   | How much data loss is acceptable, how quickly must service be restored, and how long must backups be retained? |
| OQ-13 | Data retention        | How long should tickets, notes, notifications, attachments, and audit records be retained?                     |
| OQ-14 | Reopening             | Must a technician review reopening requests? Is there a time limit? Can a request be declined?                 |
| OQ-15 | Attachments           | Are screenshots or files required? If so, what file types and maximum sizes are allowed?                       |
| OQ-16 | Categories            | Which support categories are needed at launch? Who may change them?                                            |
| OQ-17 | Knowledge base        | Is a searchable knowledge base required in the first release or deferred?                                      |
| OQ-18 | Browsers              | Which browsers and minimum device sizes must be supported?                                                     |
| OQ-19 | Reports               | Which reports, filters, and export formats are required?                                                       |
| OQ-20 | Privacy               | What information must not be included in ticket descriptions or notes? Are internal-only work notes required?  |
| OQ-21 | Outage fallback       | How should urgent technical issues be reported if TSMS or internet access is unavailable?                      |
| OQ-22 | Data location         | Are there company policies governing hosting providers or the geographic location of stored data?              |
| OQ-23 | Approval              | Who has authority to approve this SRS and sign off user acceptance testing?                                    |

# 16. Proposed project implementation plan

The recommended development process is divided into ten stages.

## Stage 1: Requirements validation

Review this document with management, employees, and the Technical Team. Confirm the problem, users, roles, scope, workflows, and reporting needs.

Deliverable: Reviewed requirements and a list of confirmed decisions.

## Stage 2: Requirements approval

Resolve the outstanding questions, confirm the first-release scope, agree measurable targets, and record formal approval.

Deliverable: Approved SRS baseline.

## Stage 3: System design

Prepare:

- Use-case diagrams.
- Ticket workflow diagrams.
- Entity-relationship diagram (ERD).
- Database design.
- Role and permission matrix.
- Wireframes and page navigation.
- API outline.
- Deployment and security design.

Deliverable: Approved system-design package.

## Stage 4: Technical and hosting planning

Confirm the technology stack, hosting choice, operating responsibilities, deployment approach, backup policy, and recovery requirements.

Deliverable: Technical architecture and deployment plan.

## Stage 5: Backend development

Implement:

- User and role management.
- Authentication and authorization.
- Ticket models and APIs.
- Assignment and prioritization.
- Work notes and ticket history.
- Escalation management.
- Resolution, closure, and reopening requests.
- In-app notifications.
- Reports and audit records.

Deliverable: Tested backend services and APIs.

## Stage 6: Frontend development

Build the responsive interfaces for employees, technicians, supervisors, administrators, and any approved report viewers.

Deliverable: Functional web interface connected to the backend.

## Stage 7: Testing

Perform unit, API, integration, security, responsive, workflow, reporting, and backup/restoration tests.

Deliverable: Test results and defect-resolution record.

## Stage 8: User acceptance and pilot

Allow selected users to test realistic support scenarios. Collect feedback and correct important defects.

Deliverable: User acceptance results and pilot approval.

## Stage 9: Deployment and training

Deploy the approved system, configure user accounts, train users, and provide documentation.

Deliverable: Production system and handover package.

## Stage 10: Evaluation and maintenance

Review usage, ticket volume, support times, escalations, recurring problems, and user feedback. Fix defects and consider future enhancements only through an approved change process.

Deliverable: Operational evaluation and maintenance plan.

# 17. Change management

Any significant change to the approved requirements should be documented and reviewed before implementation.

A change request should state:

- What requirement is changing.
- Why the change is necessary.
- Which users or workflows are affected.
- The effect on cost, schedule, security, and testing.
- Whether the change affects existing records or reports.
- Who approved the change.

The SRS version and approval record should be updated after an accepted change. This process will help control scope and prevent unplanned additions from making the project unaffordable.

# 18. Project deliverables

The expected deliverables are:

1. Approved Software Requirements Specification.
2. Use-case and workflow diagrams.
3. Entity-relationship diagram and database design.
4. User-interface wireframes.
5. Role and permission matrix.
6. Technical architecture and deployment plan.
7. TSMS backend and API.
8. Responsive web frontend.
9. Database migrations and configuration guidance.
10. Automated tests and testing records.
11. Security-testing results.
12. Backup and restoration procedures.
13. User guide.
14. Administrator and deployment guide.
15. User acceptance testing record.
16. Production deployment and handover documentation.

The final list and delivery schedule must be agreed by the client and development team.

# 19. Approval and sign-off

This SRS represents the proposed requirements baseline for the Technical Support Management System. It is comprehensive enough to guide requirements review and preliminary system design, but operational decisions identified as outstanding must be resolved or explicitly deferred before the document is treated as fully approved.

Approval confirms that the signatories understand and accept the agreed scope, workflows, roles, and requirements. It does not remove the need for testing or formal acceptance of the completed system.

| Approval role                           | Name            | Signature / approval reference | Date            |
| --------------------------------------- | --------------- | ------------------------------ | --------------- |
| Company Management Representative       | To be completed | To be completed                | To be completed |
| Technical Team Representative           | To be completed | To be completed                | To be completed |
| System Analyst / Project Representative | To be completed | To be completed                | To be completed |

## Final recommendation

Before writing code, the company should review and approve the requirements, particularly the user roles, ticket lifecycle, impact/urgency matrix, reopening rules, working hours, notification recipients, hosting budget, backup policy, and data-retention requirements.

Once those decisions are confirmed, the next step is to create the use-case diagram, ticket workflow diagram, entity-relationship diagram (ERD), permission matrix, and user-interface wireframes. These designs will turn the approved SRS into a practical development blueprint.


TECHNOLOGY STACK
Frontend: React
Backend: Python Django, postgres

End of Software Requirements Specification — TSMS, Version 1.0 Draft.


