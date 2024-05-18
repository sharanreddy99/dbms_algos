<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">DBMS_ALGOS</h1>
</p>
<p align="center">
    <em>Exploration of normalization and validation algorithms, such as All Candidate Keys, BCNF Decomposition, Chase Test, and more. Users can input data and receive step-by-step instructions on algorithm execution, covering aspects like Dependency Preservation, Minimal Cover, and 3NF Synthesis.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/commit-activity/m/sharanreddy99/dbms_algos" alt="last-commit">
	<img src="https://img.shields.io/github/created-at/sharanreddy99/dbms_algos" alt="created_at">
   <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/sharanreddy99/dbms_algos">
   <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/sharanreddy99/dbms_algos">
   <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/sharanreddy99/dbms_algos">

</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
</details>
<hr>

##  Overview

The dbms_algos project offers advanced algorithms for efficient database management. It enables calculation of exponential products, 3NF synthesis, BCNF checking, and more. With functionalities like candidate key generation, minimal cover computation, and functional dependency analysis, this project enhances database performance and integrity. By seamlessly integrating frontend and backend components via Flask API and React UI, dbms_algos caters to database administrators and developers seeking robust database algorithm implementations within a unified repository architecture.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project's architecture relies on a combination of React for the frontend, Flask for the backend, and Nginx for routing. It employs Docker for containerization and coordination between services, ensuring a scalable and modular structure. |
| 🔩 | **Code Quality**  | The codebase demonstrates good code quality with clear naming conventions, separation of concerns, and consistent styling. It follows best practices such as modularization, reusable components, and adheres to industry standards for maintainability. |
| 📄 | **Documentation** | The project includes extensive documentation covering setup, configuration, and functionality explanations. It provides detailed insights into backend algorithms, frontend components, and Docker configurations, enhancing understandability for contributors and users. |
| 🔌 | **Integrations**  | Key integrations include React, Flask, Nginx, Material-UI, Axios, and ESLint among others. These external dependencies enhance the project's capabilities in frontend development, backend API communication, styling, and code quality enforcement. |
| 🧩 | **Modularity**    | The codebase exhibits high modularity with distinct frontend and backend components encapsulated in separate directories. Each functional module focuses on specific tasks like database algorithm implementations, UI components, and server configurations, promoting reusability and maintainability. |
| 🧪 | **Testing**       | Testing frameworks and tools for the project are not explicitly mentioned in the repository details. Implementing unit tests, integration tests, or end-to-end testing suites could further enhance the codebase's reliability and robustness. |
| ⚡️  | **Performance**   | The project emphasizes algorithm efficiency, data processing speed, and resource optimization in database management tasks. By implementing advanced algorithms like ExponentialProduct, Minimal Cover, and 3NF Synthesis, it aims to enhance database operations performance and scalability. |
| 🛡️ | **Security**      | Data protection measures within the project involve Flask-Cors integration for secure frontend-backend communication. Access control mechanisms, encryption protocols, and other security practices are crucial considerations for maintaining data integrity and preventing unauthorized access. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include React, Flask, Material-UI, Axios, ESLint, Docker, and Nginx. These libraries facilitate frontend development, backend functionalities, UI design, HTTP requests handling, code linting, containerization, and routing configurations. |
| 🚀 | **Scalability**   | The project demonstrates scalability through Docker orchestration, service coordination, and microservices architecture with React, Flask, and Nginx. The use of containerization, modular components, and backend algorithms enhances the system's ability to handle increased traffic and evolving database requirements. |

---

##  Repository Structure

```sh
└── dbms_algos/
    ├── README.md
    ├── backend
    │   ├── AllCandidateKeys.py
    │   ├── BCNFDecomposition.py
    │   ├── ChaseTest.py
    │   ├── Check3NF.py
    │   ├── CheckBCNF.py
    │   ├── DependencyPreserving.py
    │   ├── Dockerfile
    │   ├── ExponentialProduct.py
    │   ├── FDRestriction.py
    │   ├── MinimalCover.py
    │   ├── NonAdditiveTestBinDecomposition.py
    │   ├── ThreeNFSynthesis.py
    │   ├── Utils.py
    │   ├── app.py
    │   └── requirements.txt
    ├── docker-compose.yml
    ├── frontend
    │   ├── .eslintrc.cjs
    │   ├── Dockerfile
    │   ├── README.md
    │   ├── index.html
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── public
    │   ├── src
    │   └── vite.config.js
    └── nginx
        ├── Dockerfile
        └── default.conf
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                                 | Summary                                                                                                                                                                                                                                                                       |
| ---                                                                                                  | ---                                                                                                                                                                                                                                                                           |
| [docker-compose.yml](https://github.com/sharanreddy99/dbms_algos.git/blob/master/docker-compose.yml) | Coordinates Docker services for front-end, back-end, and nginx in the repository. Defines builds and volumes, connects front-end to back-end via environment variable, and ensures nginx dependencies. Maintains ports for accessing front-end, back-end, and nginx services. |

</details>

<details closed><summary>frontend</summary>

| File                                                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                         | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [package-lock.json](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/package-lock.json) | ExponentialProduct.py**The `ExponentialProduct.py` file in the `dbms_algos` repository plays a crucial role in calculating and generating the exponential product of relations within a database management system. This essential functionality enables the system to efficiently process complex queries, analyze relationships between tables, and optimize data retrieval operations. By implementing this feature, the code enhances the overall performance and scalability of the database system, aligning with the repositorys architectural focus on advanced algorithms for database management. |
| [vite.config.js](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/vite.config.js)       | Configures Vite settings for the frontend, enabling React plugin and defining server options like the port and watch mode.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Dockerfile](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/Dockerfile)               | Facilitates frontend setup with Node.js in Docker. Establishes a working directory, installs dependencies, copies files, and initiates the application. Enables seamless frontend development within the DBMS algorithms repository architecture.                                                                                                                                                                                                                                                                                                                                                           |
| [package.json](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/package.json)           | Manages scripts and dependencies for Walmart frontend build pipeline using Vite and ESLint, enhancing development with React and Material-UI.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [index.html](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/index.html)               | Defines the main HTML structure and root element for the DBMS Codes frontend, loading scripts for application functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [.eslintrc.cjs](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/.eslintrc.cjs)         | Configures ESLint with rules for React development, ensuring browser and ES2020 compatibility. Ignores specified patterns and enforces guidelines for React components, unused variables, and component exports.                                                                                                                                                                                                                                                                                                                                                                                            |

</details>

<details closed><summary>frontend.src</summary>

| File                                                                                            | Summary                                                                                                                                                                                                                                                                                |
| ---                                                                                             | ---                                                                                                                                                                                                                                                                                    |
| [App.css](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/src/App.css)     | Improve styling consistency across the frontend of the repository by defining CSS rules for the components. This file enhances the visual appeal and user experience by ensuring a cohesive design language is applied uniformly.                                                      |
| [index.css](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/src/index.css) | Prevent text selection on web pages by disabling user-select CSS property in the frontend/src/index.css file. This feature enhances user experience by restricting accidental text highlighting.                                                                                       |
| [utils.js](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/src/utils.js)   | Implements a utility function for sorting objects in an array by a specified key.                                                                                                                                                                                                      |
| [main.jsx](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/src/main.jsx)   | Renders React application root element using ReactDOM.createRoot, encapsulating App component for frontend UI in the dbms_algos repository.                                                                                                                                            |
| [App.jsx](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/src/App.jsx)     | Manages user interface interactions, fetches backend data, and displays results. Persists user password, executes algorithms, and updates UI components dynamically based on user input. Facilitates a seamless frontend experience for running database management system algorithms. |

</details>

<details closed><summary>frontend.src.components.SelectDropdown</summary>

| File                                                                                                                                        | Summary                                                                                                                                                                                                                                                     |
| ---                                                                                                                                         | ---                                                                                                                                                                                                                                                         |
| [SelectDropdown.jsx](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/src/components/SelectDropdown/SelectDropdown.jsx) | Enables selection of algorithm types with a dropdown menu for interactive user experience. Integrates readily into frontend to facilitate seamless navigation and interaction with various backend algorithms in the database management system repository. |

</details>

<details closed><summary>frontend.src.components.Parameters</summary>

| File                                                                                                                            | Summary                                                                                                                                                                                             |
| ---                                                                                                                             | ---                                                                                                                                                                                                 |
| [Parameters.jsx](https://github.com/sharanreddy99/dbms_algos.git/blob/master/frontend/src/components/Parameters/Parameters.jsx) | Generates interactive form to input parameters for computing minimal cover types in database management system algorithms. Supports dynamic updating of data fields for efficient user interaction. |

</details>

<details closed><summary>nginx</summary>

| File                                                                                           | Summary                                                                                                                                                                          |
| ---                                                                                            | ---                                                                                                                                                                              |
| [Dockerfile](https://github.com/sharanreddy99/dbms_algos.git/blob/master/nginx/Dockerfile)     | Configures Nginx server by copying custom configuration.                                                                                                                         |
| [default.conf](https://github.com/sharanreddy99/dbms_algos.git/blob/master/nginx/default.conf) | Enables reverse proxying to Flask and React servers for API and frontend requests.Defines upstream servers and routes HTTP requests to corresponding services based on URI path. |

</details>

<details closed><summary>backend</summary>

| File                                                                                                                                         | Summary                                                                                                                                                                                                                                                       |
| ---                                                                                                                                          | ---                                                                                                                                                                                                                                                           |
| [NonAdditiveTestBinDecomposition.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/NonAdditiveTestBinDecomposition.py) | Implements a function to test non-additive join-binarization decomposition in database management system algorithms. It checks if subsets of attributes preserve functional dependencies based on given sets of attributes and functional dependencies.       |
| [DependencyPreserving.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/DependencyPreserving.py)                       | Analyzes functional dependencies to determine if they are preserved in a given relation decomposition, aiding in maintaining data integrity.                                                                                                                  |
| [FDRestriction.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/FDRestriction.py)                                     | Calculates Functional Dependency Restrictions based on the provided functional dependencies and attributes. Determines proper subsets and restrictions for each subset. Displays results, including the minimal cover if desired.                             |
| [requirements.txt](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/requirements.txt)                                     | Implements Flask and Flask-Cors dependencies for backend API functionality. Facilitates seamless communication between the frontend and backend components within the repositorys architectural scope.                                                        |
| [Check3NF.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/Check3NF.py)                                               | Checks for 3rd Normal Form (3NF) compliance in a database schema by verifying key dependencies. Ensure all attributes not part of any candidate key are functionally determined by only the key attributes.                                                   |
| [AllCandidateKeys.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/AllCandidateKeys.py)                               | Generates candidate keys by analyzing functional dependencies and attribute sets. Identifies primary keys based on closure computations, considering all possible attribute combinations in a given relation.                                                 |
| [CheckBCNF.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/CheckBCNF.py)                                             | Implements BCNF (Boyce-Codd Normal Form) checking for a given set of functional dependencies and relation schema. Analyzes if any dependency violates BCNF and returns the first one found, otherwise confirms BCNF compliance.                               |
| [Dockerfile](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/Dockerfile)                                                 | Installs Python dependencies for the backend server, sets up the project environment, and runs a Flask server in the Docker container for the database management system algorithms repository.                                                               |
| [ExponentialProduct.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/ExponentialProduct.py)                           | Implements algorithm for finding functional dependencies in relation schema. Automatically derives all dependencies using reflexivity, augmentation, and transitivity rules. Displays rounds of modification and final count of dependencies.                 |
| [ThreeNFSynthesis.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/ThreeNFSynthesis.py)                               | Analyzes functional dependencies and synthesizes 3NF decompositions for the provided relation schemas. Verifies candidate keys, generates minimal covers, and tests containment relationships to yield decompositions. Organizes results with custom mapping. |
| [MinimalCover.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/MinimalCover.py)                                       | Implements the Minimal Cover algorithm for functional dependencies in a database system. Manages left and right reductions, eliminating empty right-hand sides, and applies standard or non-standard form rules based on a specified characteristic.          |
| [Utils.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/Utils.py)                                                     | Computes closures and power sets, handles functional dependencies, and aids in relational database algorithms by extracting LHS and RHS. BaseController for managing data transformations and prints step-by-step progress.                                   |
| [app.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/app.py)                                                         | Implements backend algorithms in a Flask app. Routes handle various database management tasks like finding candidate keys, BCNF decomposition, and 3NF synthesis. The app executes algorithms based on user input and returns outputs accordingly.            |
| [ChaseTest.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/ChaseTest.py)                                             | Validates lossless relations using Chase test and functional dependencies, ensuring data consistency for database schemas in the repository.                                                                                                                  |
| [BCNFDecomposition.py](https://github.com/sharanreddy99/dbms_algos.git/blob/master/backend/BCNFDecomposition.py)                             | Implements BCNF decomposition algorithm within the database management systems backend. Performs decomposition and prints the resulting map.                                                                                                                  |

</details>

---

##  Getting Started

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the dbms_algos repository:
>
> ```console
> $ git clone https://github.com/sharanreddy99/dbms_algos.git
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd dbms_algos
> ```
>
> 3. Run the project using docker compose
> ```console
> $ docker compose up
> ```

###  Usage


> Access the application in the browser at http://localhost

---


##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/sharanreddy99/dbms_algos.git/issues)**: Submit bugs found or log feature requests for the `dbms_algos` project.
- **[Submit Pull Requests](https://github.com/sharanreddy99/dbms_algos.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/sharanreddy99/dbms_algos.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/sharanreddy99/dbms_algos.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com/sharanreddy99/dbms_algos.git/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=sharanreddy99/dbms_algos">
   </a>
</p>
</details>

---
