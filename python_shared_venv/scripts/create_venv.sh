DIR="/opt/manager/resources/deployments/default_tenant/$(ctx deployment id)/$(ctx instance id)"
ctx logger info "Directory: $DIR"
python3 -m venv $DIR
cat > $DIR/requirements.txt << EOF
$REQUIREMENTS
EOF
$DIR/bin/pip3 install --upgrade pip
$DIR/bin/pip3 install -r $DIR/requirements.txt
ctx instance runtime-properties python_path "$DIR/bin/python3"
ctx instance runtime-properties venv_path "$DIR"