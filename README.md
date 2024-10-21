# Label Studio with PostgreSQL - Docker Setup

![image](https://github.com/user-attachments/assets/ed05c29f-35b4-4ed3-9251-7d91a3558d2d)
![image](https://github.com/user-attachments/assets/afdc0769-4d7d-4182-be50-f1a08ce9f456)


This Docker Compose configuration sets up Label Studio with PostgreSQL as the backend database. Label Studio is an open-source data labeling tool that supports various data types. PostgreSQL is used as the database to store project and annotation data.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

## Services

This setup consists of two main services:
1. **PostgreSQL** (version 14.5) as the database.
2. **Label Studio** as the front-end labeling interface.

## Docker Compose Configuration

- **PostgreSQL**
  - Exposed on port `5437`.
  - Stores data in a Docker volume `postgres_data` to persist the database across container restarts.
  - Healthcheck ensures the database is ready before Label Studio starts.

- **Label Studio**
  - Exposed on port `8090`.
  - Data for Label Studio is stored in a Docker volume `labelstudio_data` to persist user data.
  - It automatically migrates the database on startup.
  - Optionally, you can set a secure access token for Label Studio by uncommenting the `LABEL_STUDIO_ACCESS_TOKEN` environment variable.

## Usage

1. Clone the repository or copy the `docker-compose.yml` file to your project.
2. Ensure Docker and Docker Compose are installed and running.
3. Run the following command to start the services:

    ```bash
    docker compose up -d
    ```

4. After all services are up, access Label Studio in your browser at: `http://localhost:8090`.

## Environment Variables

You can adjust the environment variables for both services in the `docker-compose.yml` file:

- **PostgreSQL**
  - `POSTGRES_DB`: The database name (default: `labelstudio`).
  - `POSTGRES_USER`: The database user (default: `labelstudio`).
  - `POSTGRES_PASSWORD`: The password for the database user (default: `labelstudio_password`).

- **Label Studio**
  - `POSTGRE_HOST`: The hostname for PostgreSQL (default: `postgres`).
  - `POSTGRE_PORT`: The PostgreSQL port (default: `5432`).
  - `POSTGRE_NAME`: The PostgreSQL database name (default: `labelstudio`).
  - `POSTGRE_USER`: The PostgreSQL user (default: `labelstudio`).
  - `POSTGRE_PASSWORD`: The PostgreSQL user password (default: `labelstudio_password`).
  - Uncomment the `LABEL_STUDIO_ACCESS_TOKEN` line to secure access with a token.

## Volumes

This setup uses Docker volumes to persist data:

- `postgres_data`: Stores PostgreSQL data.
- `labelstudio_data`: Stores Label Studio project and annotation data.

## Stopping and Removing the Containers

To stop the running services, run:

```bash
docker compose down
