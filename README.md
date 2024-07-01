# Space Exploration Persistence Service

This service facilitates GraphQL communication between the database and various Space Exploration services.

## Overview

The Space Exploration Persistence Service acts as an intermediary, enabling efficient data queries and mutations via GraphQL. It integrates seamlessly with the Space Exploration service and the frontend user interface.

## Running Locally

To run the Space Exploration Persistence Service locally, you'll need to set it up alongside the Space Exploration Service and the Space Exploration UI.

### Prerequisites

- Ensure Docker is installed and running on your machine.

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

## Project Links

- **Data Service**: [Space Exploration Service](https://github.com/stevegreghatch/Space-Exploration)
- **Frontend UI**: [Space Exploration UI](https://github.com/stevegreghatch/space-exploration-ui)
