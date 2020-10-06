# Programming for Life Sciences

[![License][badge-license]][badge-url-license]
[![Build_status][badge-build-status]][badge-url-build-status]
[![Coverage][badge-coverage]][badge-url-coverage]
[![Docs][badge-docs]][badge-url-docs]

Python toy repository for demonstrating:

* Git
* GitHub
* Social coding
* Packaging code
* Managing virtual environments
* Type annotations
* Docstrings & API docs
* Code linting
* Unit testing & test coverage
* Continuous integration

Can be used as a template for starting new repositories that follow several
good practices in terms of writing, testing, documenting and building code.

## Usage

After [installing the package](#installation), in your Python code or
interpreter, simply import `our_package`:

```py
import our_package

# run a function provided by the package
our_package.math.add_integers(3, 4)
```

Alternatively, import only the module that you are interested in:

```py
from our_package import math as our_math

# run a function provided by the package
our_math.add_integers(3, 4)
```

> Note that we have given the module the alias `our_math` during import,
> rather than just referring to it as `math` in our subsequent code; this is
> because we want to avoid namespace collisions with Python's built-in `math`
> library, which, if imported with `import math`, would _also_ be imported
> as `math`.

Finally, you can also just import the function you want to use:

```py
from our_package.math import add_integers

# run imported function
add_integers(3, 4)
```

Check the [API docs][badge-url-docs] to see all of what's in this package!

## Installation

> Note that the steps listed here generally need to be done only once, with two
> exceptions:
>  
> * When starting a new shell or after calling `conda deactivate`, the
>   Conda environment containing `our_package` (as set up according to the
>   instructions below) will always need to be activated with:
>  
>   ```bash
>   conda activate programming-for-life-sciences
>   ```
>  
> * If additional dependencies are added to the project along the way, they
>   should be added to the environment so that their installation will be
>   persistent. See the [dedicated section](#updating-the-conda-environment)
>   for details on how that can be done.

### Quick installation

While detailed, step-by-step instructions are outlined below, these summarized
installation instructions may be helpful to get you started quickly!

> If you haven't already installed Conda on your system, we recommend
> [installing Miniconda][miniconda-install]. Alternatively, you can also
> [install Anaconda][anaconda-install] which comes packed with a boatload of
> useful tools for bioinformatics.

```bash
git clone git@github.com:zavolanlab/programming-for-life-sciences.git
cd programming-for-life-sciences
conda deactivate
conda update -y conda
conda env create -f environment.yml
conda env update --name programming-for-life-sciences --file environment-dev.yml
conda activate programming-for-life-sciences
```

### Cloning the repository

Before you can install the package, you need to first obtain the repository
contents. Traverse to a directory of your choice, and then clone the
repository with:

```bash
git clone git@github.com:zavolanlab/programming-for-life-sciences.git
```

This will create a directory `programming-for-life-sciences` in your current
working directory. If you would prefer a different name (it's quite a
mouthful!), you can call that last command with an additional parameter
indicating the desired name, like so:

```bash
git clone git@github.com:zavolanlab/programming-for-life-sciences.git toy-repo
```

Enter the new directory cloned from GitHub:

```bash
cd programming-for-life-sciences
```

> Obviously you will need to change this call accordingly, if you gave the
> directory a different name in the previous step.

### Setting up a dedicated Conda environment

Now that we have all the code and related files residing on our local machine
and are located in the root directory of the repository, we are ready to
install our package `our_package` so that it can be imported and used in your
Python code.

However, in order to contain all software dependencies of a project in an
isolated environment, it is highly recommended to set up a _virtual
environment_ first. There are several options to do so, such as the
Python-specific [`virtualenv`][virtualenv] package. However, here we will use
[Conda]-based virtual environments, as they are somewhat more convenient to
manage across projects, and, perhaps more importantly, allow adding non-Python
dependencies.

Verify your Conda installation by running:

```bash
conda info
```

> If it turns out that you do not have Conda installed, check the node in the
> [quick installation](#quick-installation) section that provides links to
> Conda installation instructions.

To ensure you start from a clean slate, deactivate any existing environment:

```bash
conda deactivate
```

You may also want to ensure that you are using the latest Conda version:

```bash
conda update -y conda
```

Now it's time to set up your environment and install the package. You can
do so either manually or by making use of [Conda environment
files][conda-env-files].

#### Manual installation

To manually set up a Conda environment and install the package, start with the
following command, which instructs Conda to install a barebones environment
called `programming-for-life-sciences` based on a recent Python version:

```bash
conda create --name programming-for-life-sciences python=3.8.5
```

Now we still need to activate the environment:

```bash
conda activate programming-for-life-sciences
```

Finally, we are ready to install the package. This can be done using either
of the following ways:

```bash
# Install the package in an editable manner; better for development
# Will create files/directories in your current working directory
pip install -e .

# Regular installation; better when simply using a package
# Will create files/directories in your standard Python library path
pip install .
```

> [Pip][pip] is Python's default package manager, i.e., similar to an app
> store it knows about software/package repositories and allows you to
> conveniently install them, taking care of resolving and - if possible -
> installing dependencies. It's very similar to Conda in that sense, but while
> Conda has the advantage of supporting software written in any kind of
> language, not all Python packages are available via Conda, and, importantly,
> Conda cannot directly be used to install local packages such as
> `our_package`. However, within an active Conda environment, Conda will make
> sure that any packages installed via `pip` will be private to this
> environment, ensuring, like in this case, that `our_package` will not be
> installed globally.

#### Installation via a Conda environment file

A Conda environment can be created also with a configuration file. This allows
setting up the environment and installing the package (and/or any dependencies)
conveniently in one go:

```bash
conda env create -f environment.yml
```

We will still need to activate the environment:

```bash
conda activate programming-for-life-sciences
```

### Updating the Conda environment

Currently, they are no additional dependencies required for _using_
`our_package` (but note that there are additional [requirements for
testing/development](#installing-development-dependencies)). However, as time
goes by, additional dependencies are typically added to a project. Here we
will describe some ways on how you can update your Conda environment to persist
such added dependencies.

#### Adding dependencies via Conda

You can use Conda to add any available Conda package to your environment. If
your environment is already activated, you can simply do:

```bash
conda install YOUR_PACKAGE

# Example
conda install requests=2.23.0
```

If your environment is _not_ activated, you can either activate it first and
the call the above command, or you can specify the name of the enviroment like
so:

```bash
conda install --name programming-for-life-sciences YOUR_PACKAGE

# Example
conda install --name programming-for-life-sciences requests=2.23.0
```

If your package is only available via a non-default channel, you can add a
channel to your call:

```bash
conda install --channel CHANNEL YOUR_PACKAGE

# Example
conda install --channel bioconda samtools=1.11
```

##### Version control dependencies via an environment file

While the above process will ensure that the package will be available in
_your_ environment, others won't know that the package is required. Therefore
you should also add any new dependecies to a version-controlled Conda
environment file, typically `environment.yml`. If you do so first, this gives
you another possibility to update your environment:

```bash
conda env update --name programming-for-life-sciences --file environment.yml
```

This will update your environment with any new dependencies, while already
available ones are ignored.

> Note that if a package listed in the environment file is already installed
> in your environment, but the versions do not match, this call will replace
> the available version with the one listed in the environment file.

#### Adding Python dependencies via Pip

Using Conda to add software dependencies to your environment is generally the
preferred way, even when installing Python packages. But in cases where Conda
binaries are not available for a given package or because it may be more
convenient/fitting to use Pip instead, you can add a package to your
environment in the following way:

First, ensure that your Conda environment is activated:

```bash
conda activate programming-for-life-sciences
```

Then simply install your package via `pip`:

```bash
pip install YOUR_PACKAGE

# Example
pip install requests==2.23.0
```

##### Version control dependencies via a requirements file

Similar to Conda's environment files, Pip is also able to install dependencies
from a file, which, by convention, is typically called `requirements.txt`. If
you are maintaining a pure Python project and do not use Conda (or if you only
use it to manage your Python/Pip virtual environment), you can dispense with
the complexities of maintaining a Conda environment file and add your
dependencies to that file, then install/update your _active_ Conda environment
with:

```bash
pip install -r requirements.txt
```

> The same behavior regarding version conflicts applies as for Conda
> environment files: package versions listed in `requirements.txt` will replace
> available packages of the same name if versions do not match.

### Installing development dependencies

If you do not only want to _use_ the package, but run tests and/or contribute
to its development, several Python packages are required for code linting and
testing.

It is good practice to keep these dependencies in version-controlled
environment/requirement files, but separate from essential dependencies.
Therefore this package provides the files `environment-dev.yml` (Conda) and
`requirements-dev.txt` (Pip) to store package information on any non-essential
dependencies.

> Note that projects wouldn't normally include _both_ a Conda environment and
> a Pip requirements file, as it is confusing and requires both files to be
> kept in sync. We have simply chosen to do so to make you familiar with both
> styles, as they are both very common. In this regard, it is also worth
> pointing out that while Conda is particularly great for many bioninformatics
> projects where dependencies are often written in different languages,
> building projects with Conda is typically not as well supported by automated
> build systems that are used, e.g., in Continuous Integration or documentation
> building systems. For example, in the configurations for both the Travis CI
> and the Sphinx documentation building engine provided in this repository, Pip
> is used rather than Conda for simplicitie's sake.

#### Installing development dependencies with Conda

To install development/testing dependencies with Conda, run:

```bash
conda env update --name programming-for-life-sciences --file environment-dev.yml
```

#### Installing development dependencies with Pip

To install development/testing dependencies with Pip, first ensure that the
Conda environment is activate:

```bash
conda activate programming-for-life-sciences
```

Then run:

```bash
pip install -r requests-dev.txt
```

## Contributing

This project is a community effort and lives off your contributions, be it in
the form of bug reports, feature requests, discussions, fixes, or other code
changes. Please refer to our organization's [contributing
guidelines][contributing] if you are interested to contribute. Please respect
the [Code of Conduct][code-of-conduct] for all interactions with the community.

## Versioning

The project adopts the [semantic versioning][semver] scheme for versioning.
Currently the service is in beta stage, so the API may change without further
notice.

## License

This project is covered by the [Apache License 2.0][badge-url-license] also
[shipped with this repository][license].

## Contact

Feel free to [reach out to us][contact] with any questions, suggestions or
complaints you may have.

[anaconda-install]: <https://docs.anaconda.com/anaconda/install/>
[badge-build-status]:<https://travis-ci.com/zavolanlab/programming-for-life-sciences.svg?branch=main>
[badge-coverage]:<https://img.shields.io/coveralls/github/zavolanlab/programming-for-life-sciences>
[badge-license]:<https://img.shields.io/badge/license-Apache%202.0-blue.svg>
[badge-url-build-status]:<https://travis-ci.com/zavolanlab/programming-for-life-sciences>
[badge-url-coverage]:<https://coveralls.io/github/zavolanlab/programming-for-life-sciences>
[badge-url-license]:<http://www.apache.org/licenses/LICENSE-2.0>
[badge-docs]: <https://readthedocs.org/projects/programming-for-life-sciences/badge/?version=latest>
[badge-url-docs]: <https://programming-for-life-sciences.readthedocs.io/en/latest/?badge=latest>
[contact]: <zavolab-biozentrum@unibas.ch>
[code-of-conduct]: CODE_OF_CONDUCT.md
[contributing]: CONTRIBUTING.md
[license]: LICENSE
[miniconda-install]: <https://docs.conda.io/projects/conda/en/latest/user-guide/install/>
[pip]: <https://pip.pypa.io/en/stable/>
[semver]: <https://semver.org/>
[virtualenv]: <https://virtualenv.pypa.io/en/latest/>
