#!/usr/bin/env python

import os
import json
import subprocess as sp

def run_cmd(cmd, cwd=None):
    print(f"+ {cmd}")
    process = sp.run(cmd, shell=True, cwd=cwd)
    if process.returncode != 0:
        print("Command failed.")
        exit(1)

def download_lfortran_file(commit, filename):
    base_url = "https://lfortran.github.io/wasm_builds"
    run_cmd(f'curl "{base_url}/{commit["build_type"]}/{commit["id"]}/{filename}" -o public/{filename}')

commit = json.load(open("utils/commit.json"))

download_lfortran_file(commit, "lfortran.js")
download_lfortran_file(commit, "lfortran.wasm")
download_lfortran_file(commit, "lfortran.data")

os.environ["MY_ENV"] = "production" if os.getenv("GITHUB_REF") == "refs/heads/main" else "development"
run_cmd("npm run build")
