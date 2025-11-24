"""
Helper to initialize Airflow with an absolute SQLite path on any OS.

Airflow's default SQLite URL may be considered a relative path on Windows
when backslashes are present (e.g. `sqlite:///C:\\Users\\name/airflow/airflow.db`).
This script derives an absolute Airflow home directory, forces a POSIX-style
path in the SQLAlchemy URL, and runs ``airflow db init`` with the corrected
configuration so the initialization succeeds on Windows, macOS, and Linux.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path


def _resolve_airflow_home() -> Path:
    """Return an absolute Airflow home directory.

    If ``AIRFLOW_HOME`` is already defined it is respected, otherwise a
    directory named ``airflow_home`` inside the repository root is used.
    """
    env_home = os.environ.get("AIRFLOW_HOME")
    if env_home:
        return Path(env_home).expanduser().resolve()

    repo_root = Path(__file__).resolve().parent.parent
    return repo_root.joinpath("airflow_home").resolve()


def main() -> None:
    airflow_home = _resolve_airflow_home()
    airflow_home.mkdir(parents=True, exist_ok=True)

    # Build a POSIX-style path so SQLite treats it as absolute on Windows.
    database_path = airflow_home.joinpath("airflow.db").as_posix()

    os.environ["AIRFLOW_HOME"] = str(airflow_home)
    os.environ["AIRFLOW__DATABASE__SQL_ALCHEMY_CONN"] = f"sqlite:///{database_path}"

    print(f"AIRFLOW_HOME set to {airflow_home}")
    print(f"Initializing database at sqlite:///{database_path}")
    subprocess.run(["airflow", "db", "init"], check=True)


if __name__ == "__main__":
    main()
