# CV Explorer

Welcome to the CV Explorer repository! This project is designed to help professionals showcase their Curriculum Vitae (CV) in an interactive and dynamic manner. By leveraging the power of Neo4j, GraphQL, and React, users can explore a visual map that beautifully represents the various elements of their CV.

## Features

- **Neo4j Database**: Store and manage CV data efficiently and flexibly with the leading graph database.
- **GraphQL API**: Facilitate client-server communication with GraphQL, ensuring that the client receives exactly the data it needs.
- **Interactive Map**: Utilize a React-based user interface to interactively explore the various elements of your CV.

## Getting Started

### Prerequisites

- Docker and Docker Compose: Make sure you have Docker and Docker Compose installed on your system. See the official [Docker docs](https://docs.docker.com/get-docker/) for installation instructions.

### Installation

1. Clone the repository:

```sh
git clone https://github.com/technoplato/CV.git
cd CV
```

2. Build the Docker containers:

```sh
docker-compose up --build
```

3. The API server and the Neo4j database should now be running. You can access the Neo4j database at http://localhost:7474 and the API at http://localhost:4000.


## Contact

Michael Lustig - lustig@knophy.com

## To-Do

The following is a list of features and improvements that are planned for future development:

- **Build React App**: Develop the front-end using React to create an interactive user interface for CV exploration.

- **Data Importer**:
  - Develop a feature that allows users to easily import data from a resume or a blob of text.
  - Consider implementing a pipeline for text extraction, followed by natural language processing (e.g., using GPT-3.5-turbo) to parse and organize the data.
  - Automatically insert the processed data into the Neo4j database according to the schema.
