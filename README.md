# Simple Blockchain Simulation

## Overview
This project is a simple blockchain simulation implemented in Python. It demonstrates core blockchain concepts, including block creation, hashing, proof-of-work, validation, and tamper detection. The project also includes a Flask API for interacting with the blockchain and is fully containerized using Docker.

## Features
- **Block Structure**: Each block contains an index, timestamp, transactions, previous block hash, and current block hash.
- **Proof of Work**: Implements a simple mining mechanism to add computational effort to block creation.
- **Blockchain Validation**: Ensures the chain's integrity by verifying hashes.
- **Tampering Detection**: Modifying a block invalidates the entire chain.
- **Flask API**: Provides endpoints for interacting with the blockchain.
- **Dockerized**: Easily deployable using Docker.

## Prerequisites
- Python 3.9+
- Flask (`pip install flask`)
- Docker (if running in a container)

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/ANJALINITA/quadB-_Tech_Assigment_Anjali.git
cd quadbtech_blockchain
```

### 2. Run the Blockchain Manually
#### a. Install Dependencies
```bash
pip install flask
```
#### b. Start the Server
```bash
python server.py
```

### 3. Docker Setup (Optional but Recommended)
#### a. Build the Docker Image
```bash
docker build -t simple-blockchain .
```
#### b. Run the Container
```bash
docker run -p 5000:5000 simple-blockchain
```

## API Endpoints
### 1. **Mine a Block**
- **Endpoint:** `POST /mine`
- **Request:**
  ```json
  {
    "transactions": "Alice -> Bob: 10 BTC"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Block added!",
    "index": 1
  }
  ```

### 2. **Retrieve Blockchain**
- **Endpoint:** `GET /chain`
- **Response:**
  ```json
  [
    {
      "index": 0,
      "transactions": "Genesis Block",
      "hash": "..."
    },
    {
      "index": 1,
      "transactions": "Alice -> Bob: 10 BTC",
      "hash": "..."
    }
  ]
  ```

### 3. **Tamper with Blockchain**
- **Endpoint:** `POST /tamper`
- **Request:**
  ```json
  {
    "index": 1,
    "new_data": "Tampered Transaction"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Block tampered!"
  }
  ```

### 4. **Validate Blockchain**
- **Endpoint:** `GET /validate`
- **Response:**
  ```json
  {
    "valid": false
  }
  ```

## How to Detect Tampering
1. Add some blocks.
2. Modify a block using the tamper API.
3. Validate the blockchain (it should return `false`).

## Project Structure
```
/
├── blockchain.py    # Blockchain logic
├── server.py        # Flask API server
├── Dockerfile       # Docker configuration
├── README.md        # Project documentation
```

## Future Enhancements
- Implementing a peer-to-peer network.
- Adding digital signatures for transactions.
- Integrating a frontend UI.

## License
This project is licensed under the MIT License.

## Author
[ANJALI](https://github.com/ANJALINITA)

