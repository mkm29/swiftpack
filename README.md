<div id="readme-top"/>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mkm29/swiftpack">
    <img src="media/logo.png" alt="Logo" width="380" height="380">
  </a>

<h3 align="center">SwiftPack</h3>

  <p align="center">
    Asynchronous Python, DevEx Style
    <br />
    <a href="https://github.com/mkm29/swiftpack"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mkm29/swiftpack">View Demo</a>
    ·
    <a href="https://github.com/mkm29/swiftpack/issues">Report Bug</a>
    ·
    <a href="https://github.com/mkm29/swiftpack/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#usage-init">Initialization</a></li>
        <li><a href="#usage-basic">Basic</a></li>
    </li>
    <li><a href="#features">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project contains a simple Python® project that demonstrates how to work with [SQLAlchemy](https://www.sqlalchemy.org/) asynchronously with [SQLModel](https://sqlmodel.tiangolo.com/) and [FastAPI](https://fastapi.tiangolo.com/). We also include some setup/build tooling using [Make](https://www.gnu.org/software/make/) and [Poetry](https://python-poetry.org/), with data validation being handled via [Pydantic](https://docs.pydantic.dev/latest/) and [SQLModel](https://sqlmodel.tiangolo.com/). [Pre-commit](https://pre-commit.com/) hooks are utilized for a variety of purposes, including:

- Code formatting
- Linting
- Checking commit messages
- Dependency checks
- Secret detection

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
<a name="getting-started"></a>

## Getting Started

> [!TIP]
> **Quickstart:** With [Homebrew](https://brew.sh) installed and `brew` available (`which brew`):
> ```bash
> # if you use the gh CLI tool
> gh repo clone mkm29/swiftpack
> # or just git
> git clone https://github.com/mkm29/swiftpack.git
> # then set it up, run deps twice in separate invocations
> make deps
> make deps check test build

<!-- PREREQUISITES -->
<div id="prerequisites"/>

### Prequisites

The following are required:

- A `-nix` system
  - Adding Windows support is invited, please create a PR :)
- [Poetry](https://python-poetry.org/)
- [Python](https://www.python.org/)
- [Make](https://www.gnu.org/software/make/)
- [Homebrew](https://brew.sh)
- [Docker](https://www.docker.com/)
    - docker-compose

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
<div id="usage"/>

## Usage

<div id="usage-init"/>

### Initializaton

You can simply start the stack locally via `docker compose up --build -d`. Currently you may see an error starting the webserver initially, if you run into this you need to perform the migrations:

```bash
docker compose exec web alembic init -t async migrations
docker compose exec web alembic upgrade head|<REVISION_ID>
```

or you can create the `song` table via the following `SQL`:

```
docker compose exec db psql -U postgres -d swiftpack -w -c "CREATE TABLE song (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, artist VARCHAR(255) NOT NULL, year INT);"
```

<div id="usage-basic"/>

### Basic

As this is simply a very basic FastAPI + async Postgres app, you will be to view a few endpoints such as:

- `/health`: Currently only return a `{"status": "ok"}` JSON response
- `/info`: Basic application settings
- `/metrics`: Prometheus metrics
- `/api/v1/songs/`
  - `GET` to list all `songs` in database
  - `POST` use `curl` to create a song: `curl -d '{"name":"Wagon Wheel", "artist":"O.C.M.S", "year":"2004"}' -H "Content-Type: application/json" -X POST http://localhost:8004/api/v1/songs`


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FEATURES -->
<div id="roadmap"/>

## Features

- API
  - Songs
    - [x] List
    - [x] Create
    - [ ] Search
  - Artists
    - [ ] List
    - [ ] Create
    - [ ] Search
  - Shows
    - [ ] List
    - [ ] Create
    - [ ] Search
  - Authentication
    - [ ] Basic
    - [ ] JWT/OIDC with Keycloak
- Database
  - Models
    - [x] Song
    - [ ] Artist
    - [ ] Show
- Migrations
  - [x] Implement basic Alembic logic
- Keycloak
  - [ ] Create service (`docker-compose`)

See the [open issues](https://github.com/mkm29/swiftpack/issues) for a full list of proposed features (and known issues/bugs).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
<div id="contributing"/>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
<div id="license"/>

## License

Distributed under the MIT License. See [LICENSE](./LICENSE.md) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
<div id="acknowledgments"/>

## Acknowledgments

* Lead Developer - Mitchell Murphy

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
