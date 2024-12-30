# DPLL Procedure Assignment

Use the **Davis-Putnam-Logemann-Loveland (DPLL)** procedure to find a satisfying assignment of the formulas \( \phi_i \). Write down all the steps that the algorithm performs in the meantime. If you have to apply a splitting rule, select the branching variables in **alphabetical order** and select **true** first, then **false**. Explicitly note the satisfying assignment.

---

### a)
\[
\phi_1 = (\neg A \vee C \vee \neg D) \land (A \vee B \vee \neg D) \land (\neg A \vee \neg E) \land \neg C \land (A \vee D) \land (A \vee C \vee E) \land (D \vee E)
\]

---

### b)
\[
\phi_2 = (E \vee A) \land (B \vee \neg A \vee C) \land (E \vee \neg D) \land (B \vee \neg C) \land (\neg B \vee D) \land (\neg E \vee \neg A \vee \neg D \vee \neg B)
\]

---

### Instructions

Please display the **final assignment** as given below:

**Final Assignment**:  
\[
A \to 1; \; B \to 0; \; C \to 1; \; \ldots
\]
