# Money Transfer App - Backend

Welcome to the Money Transfer App backend! We're delighted to have you contribute to this project. Before you begin, please take a moment to familiarize yourself with the information below.

## Project Overview

The Money Transfer App backend complements the frontend, addressing challenges in the financial transaction industry. It aims to enhance the usability, affordability, and security of money transfer apps.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/damoxify/money-transfer-app-backend.git
   ```

2. **Switch to the `testing` branch:**
   ```bash
   git checkout testing
   ```

3. **Install dependencies:**
   ```bash
   pipenv install
   ```

4. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```

5. **Apply database migrations:**
   ```bash
   flask db upgrade
   ```

6. **Run the development server:**
   ```bash
   python run.py
   ```

The backend server should now be running at `http://localhost:5000/`.

## Running Tests

To run tests, use the following command:

```bash
pytest
```

This will execute all tests in the `/tests` directory.

## Contributing

We encourage contributions to improve the project. Follow these steps:

1. Fork the repository.
2. Create a new branch based on the `testing` branch.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Create a pull request from your branch to the `testing` branch of the main repository.

Refer to the [Contribution Guidelines](CONTRIBUTING.md) for detailed information on our contribution process.

## Code of Conduct

Review and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a positive and inclusive community.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
