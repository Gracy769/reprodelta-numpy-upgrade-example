# NumPy upgrade investigation example

This small, runnable Python repository demonstrates a real dependency change:
`numpy==1.26.4` on `main` to `numpy==2.0.2` in the open upgrade pull request.
The signal-classifier source stays unchanged. NumPy's scalar promotion changed
between those versions, which can change this classifier's intermediate dtype
and its decision for an input near the threshold.

The classifier is a **constructed demonstration**, not an independently
observed production defect. It is the exact supported kernel used by
[ReproDelta](https://reprodelta-web-production.up.railway.app/). ReproDelta's
paired replay runs this trusted kernel in two pinned environments; it does not
execute arbitrary code from this repository.

## Try the pull request in ReproDelta

1. Sign in to ReproDelta with the GitHub account that can access this repository.
2. Open **Review a change** and select this repository's open NumPy upgrade PR,
   or paste the PR URL.
3. Choose **Review change**. Read the file review, then approve the displayed
   paired-run contract and start the investigation.
4. The report should show evidence from both NumPy versions and the input that
   changes the classifier's decision. Inspect the exact versions and limitations
   in the report before drawing a conclusion.

## Run either version yourself

Use Python 3.10 or 3.11. In a fresh virtual environment:

```shell
python -m venv .venv
python -m pip install -r requirements.txt
python run_example.py
```

On Windows, activate `.venv\\Scripts\\activate` before the `pip` and `run_example.py`
commands. Check out `main` for NumPy 1.26.4 or the upgrade PR branch for
NumPy 2.0.2, then reinstall the requirements in a fresh environment.

The source is MIT licensed. Its behavior is explained in
[`fixture/project/pipeline.py`](fixture/project/pipeline.py).
