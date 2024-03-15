
# Get the operating system type
os_type=$(uname)

if [[ "$os_type" == "Darwin" ]]; then
    # If it's macOS
    echo "macOS"
    rm -r python3_enviroment
    python3 -m venv python3_enviroment
    source python3_enviroment/bin/activate
    pip install ipykernel
    python -m ipykernel install --user --name=python3_enviroment --display-name="Python (python3_enviroment)"
    pip install --upgrade pip
    pip install -r requirements.txt

elif [[ "$os_type" == "Linux" ]]; then
    # If it's Linux
    echo "Linux"
    echo "macOS"
    rm -r python3_enviroment
    python3 -m venv python3_enviroment
    source python3_enviroment/bin/activate

elif [[ "$os_type" =~ "CYGWIN"* || "$os_type" =~ "MSYS"* || "$os_type" =~ "MINGW"* ]]; then
    # If it's Windows (Cygwin, MSYS or MinGW)
    echo "Windows"

else
    echo "Unknown operating system"
fi