# This is the core package

```bash
git clone https://github.com/rmorey/codex_core.git
cd codex_core
poetry install
poetry run python main.py
``` 


This is the core package. It is public, and should have everything one needs to run Codex, using the instructions above. Dependencies are defined in pyproject.toml. It could be built and published to pypi if desired. It is imported by [`codex_production`](https://github.com/rmorey/codex_production). Users can clone this repo to run it, fork it if desired, and open a pull request to submit changes back to the project.