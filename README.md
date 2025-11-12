# Kill3r
## 🔐 Key Manager with Fernet Encryption

This project provides a simple Python class for managing encryption keys using the `cryptography` library's Fernet symmetric encryption. It includes functionality to generate, save, and validate keys, with destructive fallback behavior if an invalid key is provided.

### 📁 Project Structure

. ├── key_manager.py # Contains the Key class ├── fs.py # Custom FileSystem class (must implement delete_key()) └── key.key # Auto-generated key file (if not present)

Code

### 🚀 Features

- Generates a new Fernet key on initialization
- Saves the key to `key.key` if it doesn't already exist
- Deletes files via `FileSystem.delete_key()` if an invalid key is provided
- Warns users before destructive actions

### 🧩 Requirements

- Python 3.6+
- `cryptography` library
- Custom `fs.FileSystem` class with a `delete_key()` method

### Install dependencies:

```bash
pip install cryptography
```

### ⚠️ Warning
If the provided key does not match the internally stored key, the system will trigger FileSystem.delete_key() and print:

Code
Might as well say goodbye to your files and directories now!
Use this behavior responsibly.

🛠️ Notes
The key is written in text mode ("w"), which may cause issues since Fernet keys are bytes. Consider using binary mode ("wb") for robustness.

The delete_key() method assumes destructive behavior—ensure your FileSystem class handles this safely.

📄 License
This project is open-source and available under the MIT License.

Happy encrypting! 🔐

Code

Let me know if you’d like to include GitHub badges, contribution guidelines, or a sample `FileSystem` implementation.
