# Assignment: Formalization and Resolution

This assignment consists of four parts:  
1. **Formalization in propositional logic**,  
2. **Formula satisfiability**,  
3. **CNF transformation**,  
4. **Resolution method**.

---

## A. Formalization

Please formalize the following natural language statements using the syntax of propositional logic and appropriate symbols:

1. Solutions to NP-complete problems can be found in exponential time and are verifiable in polynomial time.
2. Not following programming guidelines leads to bugs.
3. A complete algorithm finds a correct answer whenever one exists.
4. If an algorithm is sound, whenever it returns an answer the answer is true.
5. If a robot is smart, it either finds a problem solution or, otherwise, asks the operator for help.

---

## B. Satisfiability

Decide whether the following formulas are valid, unsatisfiable, or neither. Please also provide a justification for your answer, e.g., in the form of derivations, interpretations, or truth tables.

- \( \text{smoke} \implies \text{smoke} \)
- \( \text{smoke} \implies \text{fire} \)
- \( (\text{smoke} \implies \text{fire}) \implies (\neg \text{fire} \implies \neg \text{smoke}) \)
- \( (\text{smoke} \implies \text{fire}) \implies ((\text{smoke} \land \text{heat}) \implies \text{fire}) \)
- \( (\text{smoke} \implies \text{fire}) \implies (\neg \text{fire} \land \text{smoke}) \)

---

## C. CNF Transformation

Transform the formula:
\[
((C \land \neg B) \iff A) \land (\neg C \implies A)
\]
into an equivalent set of clauses \( K \).  
Please write down the individual transformation steps.

---

## D. Resolution

Finally, use the resolution method to demonstrate that:
\[
K \models (\neg B \implies (A \land C))
\]
holds.
