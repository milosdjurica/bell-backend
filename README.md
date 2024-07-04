# INSTALLATION

1. Clone the Repository

```bash
git clone https://github.com/milosdjurica/bell-backend
cd bell-backend
```

2. Set up virtual environment

```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. Install dependencies

```bash
pip install flask web3
```

# Interact with smart contracts and start backend in development mode

1. Deploy smart contract on Ganache following instructions here -> https://github.com/milosdjurica/bell-solidity#readme

1. Create .env

```
RPC_PROVIDER_URL=http://127.0.0.1:7545
CONTRACT_ADDR=0xYourContractAddress
CHAIN_ID=1337
USER_ADDR=0xAddressOfGanacheAccount
PRIVATE_KEY=PrivateKeyOfGanacheAccount
```

2. Start development server

```bash
python app.py
```

3. Application should run on port http://127.0.0.1:5000. You can interact with it using Postman or some other tool.
