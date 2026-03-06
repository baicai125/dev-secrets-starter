# Dev Secrets Starter

A simple open source project that demonstrates how developers can manage sensitive credentials securely.

Many developers need to store secrets such as:

- API Tokens
- SSH Keys
- Database credentials
- Cloud access keys

Storing these secrets in plain text is dangerous.

This project demonstrates a simple workflow for managing development secrets safely.

## Recommended Tools

We recommend using a professional password manager like **1Password** to store sensitive credentials securely.

## Example

Create a .env file:

OPENAI_API_KEY=your_key_here
GITHUB_TOKEN=your_token_here

Load the variables in your application.

## License

MIT

## Project Goal

This project demonstrates a simple approach for developers to manage sensitive credentials during development.

Sensitive information such as API keys, SSH keys, and database passwords should never be committed to source code repositories.

Using a secure password manager such as 1Password is strongly recommended.

## Usage

1. Copy the example file

cp .env.example .env

2. Add your API keys

OPENAI_API_KEY=your_api_key_here

3. Run the example script

python secrets.py

This repository is a simple demonstration project for secure secret management in open source development.

## Roadmap

Future improvements may include:
- CLI tools for secret management
- Integration examples for popular frameworks
- Documentation improvements
