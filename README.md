# Space Exploration Persistence Service

This service facilitates GraphQL communication between the database and various Space Exploration services.

## Overview

The Space Exploration Persistence Service acts as an intermediary, enabling efficient data queries and mutations via GraphQL. It integrates seamlessly with the Space Exploration data service and the frontend user interface.

## Running Locally

To run the Space Exploration Persistence Service locally, you'll need to set it up alongside the Space Exploration Data Service and the Space Exploration UI.

### Prerequisites

- Ensure Docker is installed and running on your machine.
- Clone the necessary repositories:

  ```sh
  git clone https://github.com/stevegreghatch/Space-Exploration.git
  git clone https://github.com/stevegreghatch/space-exploration-ui.git
  ```

### Setup and Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/stevegreghatch/space-exploration-persistence-service.git
   cd space-exploration-persistence-service
   ```

2. **Build the Docker Image**:

   ```sh
   docker build -t persistence-service:latest .
   ```

3. **Run the Docker Container**:

   ```sh
   docker run -d --network my-network -p 8000:8000 --name persistence-service persistence-service:latest
   ```

4. **Run the Data Service**:

   Follow the instructions in the [Space Exploration Data Service repository](https://github.com/stevegreghatch/Space-Exploration) to set up and run the data service.

5. **Run the Frontend**:

   Follow the instructions in the [Space Exploration UI repository](https://github.com/stevegreghatch/space-exploration-ui) to set up and run the frontend.

## Project Links

- **Data Service**: [Space Exploration Data Service](https://github.com/stevegreghatch/Space-Exploration)
- **Frontend UI**: [Space Exploration UI](https://github.com/stevegreghatch/space-exploration-ui)
