# conda-tool


Simple utility for conda management

## Prerequites

Have Anaconda or Miniconda in your PATH

## Installation

```
git clone https://github.com/StudioEtrange/conda-tool
```

set PATH variable under windows or linux to your conda-tool install folder

## USAGE

Remove build number version of exported conda specification
with `conda env export -n env_name > environment.yml`

So it will maximize portability between OS.

Usefull until this bug is resolved : https://github.com/conda/conda/issues/4844

```
conda env clean-file [-f env.yml]
```