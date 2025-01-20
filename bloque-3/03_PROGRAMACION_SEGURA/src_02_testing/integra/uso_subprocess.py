# uso_subprocess.py
from subprocess import run

result = run(['python3', '-m', 'main_00', "suma", '1', '2' ], capture_output=True, check=True ,text=True)

print("Var result:", result)
print("result.stdout:", result.stdout)