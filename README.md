# This is the core package

```bash
git clone https://github.com/rmorey/codex_core.git
cd codex_core
poetry install
poetry run python main.py
``` 


This is the core package. It is public, and should have everything one needs to run Codex, using the instructions above. Dependencies are defined in pyproject.toml. The routes are currently defined in [`init.py`](https://github.com/rmorey/codex_core/blob/main/codex_core/__init__.py). It could be built and published to pypi, or object storage, and subsequently installed that way. It is imported by [`codex_production`](https://github.com/rmorey/codex_production). Users can clone this repo to run it, fork it if desired, and open a pull request to submit changes back to the project. It uses [poetry](https://python-poetry.org) but doesn't necessarily have to.  A user could install and use this pacakge with poetry, pip, conda, or some other tool.