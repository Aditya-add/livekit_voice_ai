import os
from flask import Flask, request, jsonify
from livekit import api
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/getToken')
def get_token():
    room_name = request.args.get('roomName')
    participant_name = request.args.get('participantName')

    if not room_name or not participant_name:
        return jsonify({'error': 'Missing roomName or participantName'}), 400

    token = api.AccessToken(
        os.getenv('LIVEKIT_API_KEY'),
        os.getenv('LIVEKIT_API_SECRET')
    ).with_identity(participant_name) \
    .with_name(participant_name) \
    .with_grants(api.VideoGrants(
        room_join=True,
        room=room_name,
    ))

    jwt_token = token.to_jwt()
    return jsonify({'token': jwt_token})

if __name__ == '__main__':
    app.run(debug=True, port=3001)
