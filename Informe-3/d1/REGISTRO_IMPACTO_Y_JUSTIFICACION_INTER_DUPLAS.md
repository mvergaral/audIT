# Inter-Dupla Impact and Justification Register (Informe 3 Deliverables)

**Document Reference:** `AUDIT-REG-D1-D2D3D4-20261110`  
**Date:** November 10, 2026  
**Originating Team:** Dupla 1 (D1 — Quality Assurance, Governance, Company Presentation & Problem Understanding)  
**Target Teams:** Dupla 2 (D2 — Architecture, WBS, Schedule & Economics), Dupla 3 (D3 — Software Architecture & Systems), Dupla 4 (D4 — Hardware, Telemetry & S4 Infrastructure)  
**Working Directory:** `06_Repositorios_Git/repo/Informe-3/d1/`

---

## 1. Executive Summary & Strategic Approach

During the remediation of Article 46 observations for Informe 3, Dupla 1 implemented technical, structural, and narrative adjustments across Subdocuments 1, 2, and 9, as well as Formularios T-6, T-13, T-17, and T-19.

To prevent inter-dupla friction, schedule discrepancies, and cash-flow contradictions, D1 adopted **Option C: Strict Mirror Mode & Analytical Architectural Justification**:
1. **Zero Unfunded Headcount:** No additional full-time employees, external crews, or ad-hoc subcontracts were invented. All explanations rely on the 22 permanent plant staff and the 37 FTE peak already modeled by D2 in S1 §1.2, T-15, and the Economic Offer.
2. **Zero Arbitrary Metric Changes:** The hard canonical figure of **96,000 trips/year** from the Bases Técnicas was preserved intact. Operational peak loads were formally characterized as engineering stress ceilings (+33.1% over high-season average) rather than unverified client history.
3. **Strict Procedural Alignment:** Rollback and acceptance protocols were anchored directly to the 6-step cutover sequence in Formulario T-18 and the 12 contractual milestones (H1–H12) of Article 17.

This document serves as the formal audit trail explaining **why each change was introduced**, **which files were modified**, and **how each change directly interacts with the deliverables of D2, D3, and D4**.

---

## 2. Granular Register of Changes, Justifications, and Cross-Dupla Impacts

### Item 1: `EMP-01` — Operational Capacity vs. Scale of Transportes Curimón S.A.
* **Problem Addressed:** The evaluation committee noted a credibility gap between audIT's past homologous projects (up to 120 trucks and 5,500 daily events) and Curimón's scale (374 trucks, 96,000 trips/year, 41M km/year), requesting an analytical justification of how audIT's 22-person plant staff and 37 FTE peak absorb this volume without execution failure.
* **Files Modified by D1:**
  * `01-empresa/contenido.tex` (Added subsection `\subsection{Capacidad operativa y absorción de escala para el contrato}\label{sec:1-capacidad-escala}` with Table `1-capacidad-frentes`).
  * `01-empresa/formularios/T-6.tex` (Added cross-reference linking historical projects to §1.4 scale absorption analysis).
  * `01-empresa/declaracion-ia.tex` (Updated supervisory review declaration under Comunicado 10 §7.2).
* **Technical Justification:**
  Capacity was decomposed by operational front rather than assuming linear hiring:
  1. *Hardware & Fleet Mounting Front (Célula Beta):* 374 vehicles over 12 months in Stage 1 represents an installation rate of only ~1.5 trucks/day across the 5 main terminals. This is fully handled by 2 mobile technical crews (4 specialists from Célula Beta) during scheduled vehicle maintenance and overnight layovers, guaranteeing zero unscheduled fleet immobilization.
  2. *Cloud Platform & Software Front (Célula Alfa):* Scaling from 5,500 events/day to 96,000 trips/year is absorbed by the horizontal elastic scaling of Azure Kubernetes Service (AKS) and Azure IoT Hub, decoupling transaction volume from software engineering headcount.
  3. *Control Tower & 24/7 Operations Front:* 4 rotating 4x4 shifts (2 operators per shift) provide continuous coverage of all 5 terminals, supported by Level 2 engineering escalation in $\le 15$ min.
* **Direct Impact on Other Duplas & Required Verifications:**
  * **Dupla 2 (Schedule, WBS & Economics):**
    * *Verification Item in `T-14` / `T-15`:* Ensure that installation activities A02, A05, A08, and A10 remain scheduled across M1–M12 without compression into peak fruit season (Dec–Apr).
    * *Verification Item in Economic Offer:* Confirm that the labor budget reflects the 22 plant staff and 37 FTE peak without external mounting contractor line items, as this work is confirmed to be internal.
  * **Dupla 4 (Hardware & Fleet):**
    * *Verification Item in S4 / T-11:* Confirm that the 1.5 trucks/day terminal installation rate aligns with the Technoton CANCrocodile non-invasive reader mounting procedures and HIL bench validation (`CP-HW-08`).

---

### Item 2: `EMP-04` — Corporate Alliances & Boundary with Formulario T-8
* **Problem Addressed:** Subdocument 1 previously contained narrative referrals to S12/T-8 to substantiate partner commitments, creating circular dependencies since S12 was not part of the initial technical delivery scope.
* **Files Modified by D1:**
  * `01-empresa/contenido.tex` (§1.6 `\section{Alianzas}\label{sec:1-alianzas}`).
  * `01-empresa/declaracion-ia.tex`.
* **Technical Justification:**
  Redefined S1 §1.6 to present institutional, corporate-level alliances (Microsoft Azure CSP Tier 1, Quectel Wireless Solutions, Technoton, and Ruta 5 certified regional workshop network) as proof of engineering maturity and Tier 1 escalation capability. Formally stipulated that contract-specific commitment letters, subcontracts, and named partner specialists are filed in the administrative dossier of Sobre N.º 1 and summarized in Formulario T-8.
* **Direct Impact on Other Duplas & Required Verifications:**
  * **Dupla 2 & Dupla 4 (Procurement & Formulario T-8):**
    * *Verification Item in Sobre N.º 1 / T-8:* Verify that commitment letters for Microsoft Enterprise 24/7 support and Quectel modem hardware supply are present in Sobre N.º 1.
    * *Verification Item in Economics:* Ensure that cloud licensing and satellite airtime rates reflect Microsoft CSP direct tier discounts.

---

### Item 3: `NEC-01` — Seasonal Demand Model & 450 Trips/Day Stress Ceiling
* **Problem Addressed:** The evaluation committee questioned the presentation of 450 trips/day as an unverified historical claim without empirical data from Curimón's legacy TMS 2013.
* **Files Modified by D1:**
  * `02-problema/contenido.tex` (§2.1 `\section{Resumen Ejecutivo}` and §2.2.3 `\paragraph{Ecuación de balance anual}`).
  * `02-problema/declaracion-ia.tex`.
* **Technical Justification:**
  1. *Hard Canonical Baseline:* 96,000 trips/year established as the non-negotiable contract canon (overall annual average of 263.01 trips/day).
  2. *Seasonal High vs. Valley Balance:* High fruit season (Dec–Apr, 151 days) concentrates 51,060 trips (average of 338.15 trips/day), while valley season (May–Nov, 214 days) handles 44,940 trips (average of 210 trips/day). Sensitivity analysis ($\pm15\%$ on valley) yields high-season averages between 293.50 and 382.79 trips/day.
  3. *Characterization of 450 Trips/Day:* Explicitly reframed as an **engineering stress design ceiling (+33.1% above high-season average)** adopted conservatively by audIT to dimension cloud ingestion elasticity, message queues, and API gateways.
  4. *Empirical Cleansing Protocol:* Explicitly scheduled under Activity A04 in Milestone H1 (Month 2) to extract and clean TMS 2013 data (handling cancellations, duplicates, time zones, and reconciliation against 96,000 annual trips).
  5. *Metric Disambiguation:* Explicitly differentiated physical trips/day from interactive user sessions in Control Tower (380 nominal and 570 stress sessions in Formulario T-13 and `CP-PERF-01`).
* **Direct Impact on Other Duplas & Required Verifications:**
  * **Dupla 3 & Dupla 4 (Software Architecture & Cloud Sizing in S4 / T-13):**
    * *Verification Item in S4 §4.2 / T-13:* Ensure that cloud message broker throughput (Azure Event Hubs partitions) and AKS autoscaling rules are sized to handle the 450 trips/day peak burst without message drop.
    * *Verification Item in T-13 / T-17:* Confirm that test case `CP-PERF-01` continues to evaluate 380 nominal sessions and 570 stress sessions as interactive user load, while data ingestion pipes test the 450 trips/day equivalent transactional throughput.
  * **Dupla 2 (Schedule & Gantt T-15):**
    * *Verification Item in `T-15`:* Verify that Activity A04 (legacy TMS 2013 data extraction and baseline approval) concludes within Month 2 (Milestone H1) as planned.

---

### Item 4: `CAL-06`, `CAL-03`, `ALC-02` — Quality & Acceptance Framework
* **Problem Addressed:** Absence of formal milestone protocol sheets in T-17 (`CAL-06`), lack of explicit traceability for the 29 case acceptance criteria (`CAL-03`), and lack of cutover/rollback process verification (`ALC-02`).
* **Files Modified by D1:**
  * `09-calidad/contenido.tex` (Milestone protocols reference in §9.3.3).
  * `09-calidad/formularios/T-17.tex` (Inputs milestone sheets before catalog).
  * `09-calidad/formularios/protocolos-hitos-T-17.tex` (Created: 13 formal protocol sheets H1–H12/Final).
  * `09-calidad/formularios/trazabilidad-T-17.tex` (Created: Table `9-rtm-29` with 29 criteria).
  * `09-calidad/formularios/catalogo-T-17.tex` (`CP-SYS-20` expanded with 6-step cutover rollback).
  * `09-calidad/declaracion-ia.tex` (Updated).
* **Direct Impact on Other Duplas & Required Verifications:**
  * **Dupla 2 (Gantt, Critical Path & Billing Calendar):**
    * *Milestone H5 Sensitivity:* Activity A12 finishes Day 226. Bases Art. 18 gives Curimón 10 business days to review (Day 236). If observations occur, audIT's 10 business days for rectification move final sign-off to Day 246 (Month 13). D2 must confirm that the 10% payment for H5 (E-25) in the cash flow accounts for this review cycle.
    * *Peak Season User Availability (`CAL-04` / `PLA-10`):* D2 must specify in S7 / T-18 the client user availability shifts during fruit season (Dec–Apr) so UAT sign-off in A12 is not delayed.
    * *WBS & Activity Codes:* D2 must confirm that WBS packages 10.1, 10.2, 10.3, 11.1, 11.2, and activities A01–A25 referenced across all 13 protocol sheets remain unrenamed.
  * **Dupla 3 & Dupla 4 (Data & Rollback):**
    * *Verification in S3 / S4:* Confirm that the 6-step cutover rollback in `CP-SYS-20` (15-min API gateway shift to N-1, 20-min/truck buffer replay, and 24-h ERP reconciliation) is reflected in the disaster recovery design of S4.

---

## 3. Matrix of Required Cross-Dupla Verification Actions

| Target Dupla | Subdocument / Form | Specific File to Check | Verification Requirement | Criticality |
|:---|:---|:---|:---|:---:|
| **D2** | `Subdoc 7 / T-15` | `07-plan-trabajo/formularios/T-15.tex` | Check Milestone H5 review window (Day 226 completion vs. 10+10 days review under Art. 18 vs. Month 12 payment). | **High** |
| **D2** | `Subdoc 7 / T-18` | `07-plan-trabajo/formularios/T-18.tex` | Formalize client user rosters and backups for UAT during peak fruit season (Dec–Apr). | **High** |
| **D2** | `Subdoc 3 / T-12` | `03-solucion/formularios/T-12.tex` | Ensure the 29 criteria table in T-12 remains synchronized with Table `9-rtm-29` in T-17. | **Medium** |
| **D2** | `Oferta Económica` | `economico/oferta-economica/contenido.tex` | Verify that fleet mounting labor relies on internal Célula Beta staff without outsourced crew costs. | **Medium** |
| **D3 / D4** | `Subdoc 4 / S4` | `04-arquitectura/contenido.tex` | Confirm that Azure Event Hubs and API Gateway sizing withstands 450 trips/day stress ceiling. | **Medium** |
| **D4** | `Subdoc 4 / T-11` | `04-arquitectura/formularios/T-11.tex` | Validate 1.5 trucks/day terminal installation rate against Technoton CANCrocodile mounting specs. | **Low** |
| **Integrador** | `Sobre N.º 1 / T-8` | `12-equipo/formularios/T-8.tex` | Verify inclusion of partner letters (Azure CSP Tier 1, Quectel) and 3 project reference letters. | **Medium** |

---
*Register approved and compiled by Dupla 1 for full auditability across all project teams.*
