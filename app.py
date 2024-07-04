import os
from flask import Flask, request, jsonify
from web3 import Web3, HTTPProvider
import json
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

rpc_provider = os.getenv('RPC_PROVIDER_URL')
contract_address = os.getenv('CONTRACT_ADDR')
chain_id = int(os.getenv('CHAIN_ID'))
user_address = os.getenv('USER_ADDR')

web3 = Web3(HTTPProvider(rpc_provider))

with open('abi/Store.json', 'r') as abi_file:
    abi = json.load(abi_file)['abi']

contract = web3.eth.contract(address=contract_address, abi=abi)

@app.route('/storeNote', methods=['POST'])
def store_note():
    data = request.json
    note = data['note']
    private_key = os.getenv('PRIVATE_KEY')

    try:
        transaction = contract.functions.storeNote(note).build_transaction({
            'chainId': chain_id,
            'gas': 2000000,
            'gasPrice': web3.to_wei('20', 'gwei'),
            'nonce': web3.eth.get_transaction_count(user_address),
        })

        signed_tx = web3.eth.account.sign_transaction(transaction, private_key=private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return jsonify({'transactionHash': tx_hash.hex()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/getNote/<int:id_>', methods=['GET'])
def get_note(id_):
    try:
        note = contract.functions.getNote(id_).call({'from': user_address})
        return jsonify({'note': note}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
