# Technical Coordination Memo: D1 to D2 (Quality Assurance & Milestones Alignment)

**Date:** November 10, 2026  
**From:** Dupla 1 (D1 — Quality Assurance, Organizational Governance & Problem Definition)  
**To:** Dupla 2 (D2 — Solution Architecture, Work Plan, WBS & Economic Alignment)  
**Scope:** Integration of Informe 3 Deliverables, Resolution of Article 46 Observations (`CAL-03`, `CAL-06`, `ALC-02`, `GEN-05`) and Interface Alignment.  
**Repository Working Path:** `06_Repositorios_Git/repo/Informe-3/d1/`

---

## 1. Executive Summary & Purpose

Dupla 1 has completed the implementation of pending quality assurance and acceptance requirements in `Informe-3/d1/09-calidad/`. These modifications resolve structural objections raised during Informe 2 regarding the lack of formal acceptance protocol sheets by milestone (`CAL-06`), the absence of explicit traceability for the 29 case acceptance criteria (`CAL-03`), and the need for end-to-end transactional rollback verification (`ALC-02`).

All work has been conducted under **Strict Mirror Mode**: preserving 100% fidelity to D2's canonical WBS (54 work packages), schedule activities (A01–A25 in T-14/T-15), requirements (RF-001–RF-028, RNF-001–RNF-014 in T-12), and the milestone calendar of Article 17 of the Bases Administrativas.

This memo details what has been implemented and highlights three critical sensitivities where D2 must review schedule buffers and cash-flow assumptions.

---

## 2. Implemented Deliverables in `Informe-3/d1/`

### 2.1. `CAL-06`: Formal Milestone Acceptance Protocol Sheets (T-17)
* **File Created:** `09-calidad/formularios/protocolos-hitos-T-17.tex` (linked directly into `09-calidad/formularios/T-17.tex` before the test catalog, and referenced in `09-calidad/contenido.tex` §9.3.3).
* **Content:**
  * 12 individual protocol sheets for contractual milestones **H1 through H12**, plus 1 consolidated sheet for the **Final Deliverable (Producto Final)**.
  * Each sheet specifies: Contractual Deliverable, Objective Acceptance Criteria (e.g., 99.9% availability, RTO $\le 4$ h, RPO $\le 15$ min, 72 h local buffering), Verification Method (test battery, physical HIL, or documentary inspection), Required Evidence for the Docket, Sign-off Roles (Líder de Calidad audIT and Contraparte Técnica Curimón), 10-day review/rectification window under Article 18, and formal Acceptance Minute model.

### 2.2. `CAL-03`: 29-Criteria Traceability Matrix (T-17)
* **File Updated:** `09-calidad/formularios/trazabilidad-T-17.tex` (`tab:9-rtm-29`).
* **Content:**
  * Complete 29-row matrix mapping each criterion from Chapter 18 of the Case / Formulario T-12 to its requirement (RF/RNF), EDT package, contractual month and milestone sheet (H1–H12/Final), specific test cases (CP-XXX) or inspection method, and acceptance evidence.
  * **Parameter vs. Measurement Decoupling:** For Criteria 7 (tachographs), 10 (geofences), and 28 (safe rest areas), the matrix explicitly distinguishes parameter fixing at Month 12 (H5) from sustained operational verification starting at Month 16 (H7).
  * **Innovation Isolation:** Criterio 28 is traced strictly to the baseline catalog of reachable safe rest stops under Article 25 bis, keeping it decoupled from the incremental circadian fatigue pilot of Innovation 5 (`INN-03`).
  * **Documentary Inspection:** Criterio 19 is traced to documentary delivery in Month 6 (H2) for commercial contract renegotiation.

### 2.3. `ALC-02`: Transactional Rollback & Cutover Reconciliation (CP-SYS-20)
* **File Updated:** `09-calidad/formularios/catalogo-T-17.tex`.
* **Content:**
  * `CP-SYS-20` was expanded beyond hardware FOTA rollback to fully test the 6-step cutover rollback procedure from `07-plan-trabajo/formularios/T-18.tex`:
    1. Incident detection by Service Desk within 15 min.
    2. Rollback decision formalization with Contraparte Técnica within 30 min.
    3. Ingress / API Gateway traffic rerouting to version $N-1$ within 15 min.
    4. Onboard 72-h buffer replay and deduplication at $\le 20$ min/truck (RT-03.13 profile).
    5. Automated transactional reconciliation with ERP within $\le 24$ h with zero data loss.
    6. Root-cause analysis report within 5 business days (Art. 78.2).

### 2.4. `GEN-05`: Human Supervision Declarations
* **File Updated:** `09-calidad/declaracion-ia.tex`.
* **Content:** Updated under the strict 6-column format of Comunicado 10 §7.2, certifying case-by-case human verification by Carlos Abarza.

---

## 3. Key Sensitivities & Actions Required from D2

### Point 1: Milestone H5 Review Window vs. Month 12 Payment (`T-15` / Gantt / `E-25`)
* **Fact:** In D2's schedule, Activity A12 (Stage 1 comprehensive testing) finishes on **Day 226**.
* **Contractual Rule (Art. 18):** Curimón has **10 business days** to review the deliverable package (bringing the date to Day 236). If Curimón issues observations and audIT uses its **10 business days** for rectification, resubmission occurs on **Day 246 (Month 13)**.
* **Impact:** If D2's economic model / cash-flow statement assumes that Milestone H5 (10% payment under E-25) is collected strictly within **Month 12 (Day 240)**, this assumption is under tight schedule pressure.
* **Recommended D2 Action:** Check if A12 internal completion can be set a few days earlier in the Gantt, or verify that the economic cash-flow reflects the billing lag resulting from the formal 10-day review period without delaying E-25 beyond contractual limits.

### Point 2: User Availability during Peak Season (`CAL-04` / `PLA-10` in `S7` / `T-18`)
* **Fact:** Activity A12 (UAT, M10–M12) and Activity A15 (Marcha Blanca Stage 1, M13–M15) coincide with Curimón's peak agricultural season (December–April).
* **Contractual Rule:** T-17 and Art. 17.3 require certified client personnel to execute UAT and sign off on acceptance acts.
* **Recommended D2 Action:** In `S7` (§7.3) and `T-18`, formalize the operational protocol for user availability: specify dedicated shifts, backup personnel (suplentes), and off-peak testing windows so Curimón cannot claim operational disruption as an impediment to testing.

### Point 3: Maintenance of 29 Acceptance Criteria Alignment (`T-12`)
* **Fact:** T-17 now explicitly mirrors the 29 criteria from `03-solucion/formularios/T-12.tex`.
* **Recommended D2 Action:** If D2 modifies any target, contractual month, or measurement description in T-12, notify D1 immediately so `tab:9-rtm-29` in T-17 remains 100% synchronized.

### Point 4: WBS Code Consistency (`T-14` / `T-15`)
* **Fact:** T-17 protocol sheets reference WBS packages 10.1 (Testing Strategy), 10.2 (Automated Test Execution), 10.3 (Acceptance & Staging), as well as deployment packages (11.1, 11.2) and project governance (1.1).
* **Recommended D2 Action:** Confirm that no WBS package number has been altered in T-14.

---

## 4. Status of D1 Files Ready for Review

The following files are located in `06_Repositorios_Git/repo/Informe-3/d1/` and pass all LaTeX syntax and brace balance checks:
- `09-calidad/contenido.tex` (Milestone protocols reference added in §9.3.3)
- `09-calidad/formularios/T-17.tex` (Inputs milestone protocol sheets before catalog)
- `09-calidad/formularios/protocolos-hitos-T-17.tex` (13 milestone acceptance protocol sheets)
- `09-calidad/formularios/trazabilidad-T-17.tex` (29-criteria and 42-requirement matrices)
- `09-calidad/formularios/catalogo-T-17.tex` (CP-SYS-20 cutover rollback updated)
- `09-calidad/declaracion-ia.tex` (Human supervision declaration updated)

---
*Document prepared by Dupla 1 for internal team coordination.*
