# Tank Controller in Python

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-8-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->


## Project Motivations

Update the `TankController` code from C++ to Python and run on a Raspberry Pico.


## Requirements

To set up and run this project, the system must meet the following requirements:

- **Python**: The project requires Python to run. Python provides the runtime for the scripts and the GUI components.  
- **pip**: Python's package installer is needed to install and manage dependencies.  
- **pipenv**: Used for managing project dependencies and creating isolated virtual environments.  
- **Tkinter**: Required for the GUI components of the application. Tkinter comes with Python (as `python3-tk`) and is used to build and display the UI.

## Windows Developer Instructions

Test Python version:  
- `python -V`  
This command prints the installed Python version.

Upgrade pip:  
- `pip install --upgrade pip`  
- `pip --version`  
The first command upgrades pip to the latest version, and the second verifies the installed version.

Install pipenv (tool for dependencies and virtual environments):  
- `pip install pipenv`
- `pipenv --version` 
- `pipenv install`
This installs or updates all dependencies defined in the Pipfile and updates the Pipfile.lock.

Verify Tkinter installation:  
- `python -m tkinter`  
A small GUI window should appear if Tkinter is installed correctly.

## Run in Local Environment

To run in a local environment with mocked devices (with the UI State Machine integrated)

``` sh
./run_gui.sh
```
## Testing

To perform Pytest tests for the devices and UI states.

``` sh
./test.sh
```


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://www.linkedin.com/in/kadensukachevin/"><img src="https://avatars.githubusercontent.com/u/26241731?v=4?s=100" width="100px;" alt="Kaden Sukachevin"/><br /><sub><b>Kaden Sukachevin</b></sub></a><br /><a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=kadensu" title="Code">💻</a> <a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=kadensu" title="Documentation">📖</a> <a href="https://github.com/Open-Acidification/AlkalinityTitrator/issues?q=author%3Akadensu" title="Bug reports">🐛</a></td>
      <td align="center"><a href="https://github.com/prestoncarman"><img src="https://avatars.githubusercontent.com/u/3517157?v=4?s=100" width="100px;" alt="Preston Carman"/><br /><sub><b>Preston Carman</b></sub></a><br /><a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=prestoncarman" title="Code">💻</a> <a href="https://github.com/Open-Acidification/AlkalinityTitrator/issues?q=author%3Aprestoncarman" title="Bug reports">🐛</a></td>
      <td align="center"><a href="https://github.com/KonradMcClure"><img src="https://avatars.githubusercontent.com/u/66455502?v=4?s=100" width="100px;" alt="Konrad McClure"/><br /><sub><b>Konrad McClure</b></sub></a><br /><a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=KonradMcClure" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/Noah-Griffith"><img src="https://avatars.githubusercontent.com/u/78978886?v=4?s=100" width="100px;" alt="Noah-Griffith"/><br /><sub><b>Noah-Griffith</b></sub></a><br /><a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=Noah-Griffith" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/d-cryptic"><img src="https://avatars.githubusercontent.com/u/52271502?v=4?s=100" width="100px;" alt="Barun Debnath"/><br /><sub><b>Barun Debnath</b></sub></a><br /><a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=d-cryptic" title="Code">💻</a></td>
      <td align="center"><a href="https://kieransukachevin.github.io/first%20portfolio/portfolio.html"><img src="https://avatars.githubusercontent.com/u/54186484?v=4?s=100" width="100px;" alt="Kieran Sukachevin"/><br /><sub><b>Kieran Sukachevin</b></sub></a><br /><a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=kieransukachevin" title="Tests">⚠️</a> <a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=kieransukachevin" title="Code">💻</a></td>
      <td align="center"><a href="https://github.com/jsoref"><img src="https://avatars.githubusercontent.com/u/2119212?v=4?s=100" width="100px;" alt="Josh Soref"/><br /><sub><b>Josh Soref</b></sub></a><br /><a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=jsoref" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/TaylorSmith28"><img src="https://avatars.githubusercontent.com/u/83837157?v=4?s=100" width="100px;" alt="TaylorSmith28"/><br /><sub><b>TaylorSmith28</b></sub></a><br /><a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=TaylorSmith28" title="Tests">⚠️</a> <a href="https://github.com/Open-Acidification/AlkalinityTitrator/commits?author=TaylorSmith28" title="Code">💻</a></td> <!-- gitleaks:allow -->
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
