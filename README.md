# Clio - OIDC Authorization Code Flow for CLI Programs

This python module demonstrates a simple way for a command line program to
reterive an access token to m ake calls to an API that is protected by JWT using
an Open ID Connect (OIDC) IDP such as Auth0. This authentication flow is best
used on a developers primary machine and it requires the browser to be able to
hit the cli's network socket (webserver). Specifically this module implements
https://auth0.com/docs/authorization/flows/authorization-code-flow

> NOTE: Device Authorization Flow is not yet supported but coming soon.
> This is used in the case where the current device does not have the ability
> to open a browser such as a remote linux virtual machine (VM). For more
> information visit https://auth0.com/docs/authorization/flows/device-authorization-flow

## Usage

To run through this example you will need a tenant at Auth0 and to download
this repo.

```
pip install https://github.com/patrickglass/cliauth
```

Login to your Auth0 tenant at `https://manage.auth0.com`. Create a new Application.

* Create Application:
  * Name: cli interface for my api
  * Application Type: Regular Web Applications (Traditional web app using redirects)


## Further Reading

https://auth0.com/docs/authorization/flows/device-authorization-flow
https://auth0.com/docs/authorization/flows/authorization-code-flow
https://datatracker.ietf.org/doc/html/draft-ietf-oauth-device-flow-15#section-3.5
https://datatracker.ietf.org/doc/html/rfc6749#section-4.1
https://www.altostra.com/blog/cli-authentication-with-auth0
