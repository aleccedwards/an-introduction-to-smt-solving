# An Introduction to SMT Solving

![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)
![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)

Hands-on teaching materials for an introductory session on **Satisfiability
Modulo Theories (SMT)**. The session walks through using SMT solvers — chiefly
[Z3](https://github.com/Z3Prover/z3) and
[CVC5](https://cvc5.github.io/) — to solve problems and to *certify* their
correctness, ending with a toy counterexample-guided inductive synthesis (CEGIS)
implementation for Lyapunov-function synthesis.

## Who this is for

This material is aimed at **first year AIMS (Autonomous Intelligent Machines and
Systems CDT) students**. It assumes familiarity with Python, but no prior
background in logic, SAT/SMT, or formal verification is required.

## Contents

The notebook is a guided, exercise-driven session. It covers:

1. **SAT and SMT basics** — propositional satisfiability and solving with Z3.
2. **Satisfiability over the reals** — roots of polynomials with quantifier-free
   nonlinear real arithmetic.
3. **A Sudoku solver** — quantifier-free linear integer arithmetic.
4. **Certifying specifications** — proving a property holds over a domain and
   extracting counterexamples when it does not.
5. **Bit-vector reasoning** — proving classic "bit tricks" correct.
6. **Counterexample-guided inductive synthesis (CEGIS)** — synthesising
   Lyapunov functions with a learned candidate and an SMT verifier.
7. **Quantifier alternation** — using `ForAll` to synthesise certificates
   directly.

## Getting started

This project uses Python. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

Install the requirements:

```bash
python -m pip install -r requirements.txt
```

Register the environment as a Jupyter kernel (optional, if you use a virtual
environment):

```bash
python -m ipykernel install --user --name='.venv'
```

Launch the notebook:

```bash
jupyter notebook
```

## Repository layout

| Path | Description |
| --- | --- |
| `An Introduction to SMT-solving.ipynb` | The student copy — exercises left for the reader. |
| `Completed_An Introduction to SMT-solving.ipynb` | The instructor copy, with solutions and outputs. |
| `res/` | Figures used in the notebook. |
| `requirements.txt` | Python dependencies. |

Instructors should teach from the student notebook and keep the completed
notebook as a reference/answer key.

## Further reading

The session builds directly on ideas from the following work:

- **Fossil 2.0** — A. Edwards, A. Peruffo, A. Abate. *Fossil 2.0: Formal
  Certificate Synthesis for the Verification and Control of Dynamical Models.*
  HSCC '24, ACM, 2024. [doi:10.1145/3641513.3651398](https://doi.org/10.1145/3641513.3651398)
  · [github.com/oxford-oxcav/fossil](https://github.com/oxford-oxcav/fossil)
- **Neural Abstractions** — A. Abate, A. Edwards, M. Giacobbe. *Neural
  Abstractions.* NeurIPS 2022.
- **SAT/SMT by Example** — D. Yurichev. A wide-ranging, example-driven SAT/SMT
  resource: <https://smt.st/> (CC BY-SA 4.0).

Background and further resources referenced throughout:

- D. Kroening, O. Strichman. *Decision Procedures: An Algorithmic Point of View.*
  <https://www.decision-procedures.org/>
- The [SMT-LIB](https://smtlib.cs.uiowa.edu/) standard.
- L. de Moura, N. Bjørner. *Z3: An Efficient SMT Solver.* TACAS 2008.
  <https://link.springer.com/chapter/10.1007/978-3-540-78800-3_24>
- [CVC5](https://cvc5.github.io/).
- P. A. Parrilo. *Semidefinite programming relaxations for semialgebraic
  problems.* (Sum-of-Squares optimisation, an alternative to SMT-based
  stability certification.) <https://ieeexplore.ieee.org/document/1184414>
- Neural-network verification tools: [Marabou](https://github.com/NeuralNetworkVerification/Marabou),
  [PLANET](https://github.com/progirep/planet),
  [JAXVerify](https://github.com/deepmind/jax_verify),
  [DNNV](https://github.com/dlshriver/DNNV).

## Citation

If you use or adapt these materials, please cite this repository. A
[`CITATION.cff`](CITATION.cff) file is provided; GitHub will show a "Cite this
repository" button.

## License

This repository is **dual-licensed** by content type:

- **Code** (Python snippets and scripts) — [MIT](LICENSE).
- **Written teaching content** (notebook prose and figures, documentation) —
  [Creative Commons Attribution 4.0 International](LICENSE-CC-BY-4.0).

## Author

Alec Edwards · [@aleccedwards](https://github.com/aleccedwards)
