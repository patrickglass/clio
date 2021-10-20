
import json
import secrets
import requests

from klein import run, route
from klein import Klein


class Authorization(object):
    app = Klein()

    def __init__(self, domain, client_id, scope=['openid']):
        self._authorization_code = ''
        self._client_id = client_id
        self._domain = domain
        self._scope = scope
        self._access_token = ''
        self._refresh_token = ''

    def Tokens():
        """Returns the access and refresh tokens after auth has taken place"""
        return self._access_token, self._refresh_token

    def DeviceFlow(self):
        code_challenge = secrets.token_hex(84)
        csrf = secrets.token_hex(42)
        authenticate(code_challenge, csrf, 'http://localhost:4043')
        # Exchange code for access token

    def AuthCodeFlow(self):
        code_challenge = secrets.token_hex(84)
        csrf = secrets.token_hex(42)
        # Start webserver to receive authorization code
        # for port in range()
        self.app.run('localhost', 4043)
        authenticate(code_challenge, csrf, 'http://localhost:4043')
        # Exchange code for access token

    def authenticate(self, code_challenge, state, redirect_uri):
        """https://auth0.com/docs/api/authentication#authorization-code-flow-with-pkce"""
        payload = {
            'response_type': 'code',
            'code_challenge_method':'S256',
            'code_challenge': code_challenge,
            'client_id': self._client_id,
            'redirect_uri': redirect_uri,
            'scope': self._scope,
            # 'audience':<token-audience>,
            'state': state
        }
        requests.get(f"https://{self._domain}/authorize", params=payload)

    @route('/callback', methods = ['POST'])
    def handle_authorization_code(self, request):
        print(request)
        print(request.__dict__)
        print(request.args)
        self._authorization_code = request.content.read()
        if self._authorization_code == '':
            request.setResponseCode(404)
            return 'Invalid auth code response parameters'
        return f"""
            <html>
            <body>
                <h1>LOGIN SUCCEEDED</h1>
                <h3>Fixme: Showing code only for development</h3>
                <p>Code: {self._authorization_code}</p>
                <p>State: {state}</p>
                <p>Error: {error}</p>
                <p>Description: {error_description}</p>
            </body>
            </html>
        """

    def get_access_token(self, code, code_verifier, redirect_uri):
        """https://auth0.com/docs/api/authentication#authorization-code-flow45"""
        body = {
            'grant_type': 'authorization_code',
            'client_id': self._client_id,
            'code': code,
            'code_verifier': code_verifier,
            'redirect_uri': redirect_uri
        }
        request.post(f"https://{self._domain}/oauth/token", data=body)
