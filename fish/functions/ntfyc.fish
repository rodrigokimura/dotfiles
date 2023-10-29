function ntfyc --description "Send notification"
    set -lx PIPENV_PIPFILE $HOME/dev/ntfy_client/Pipfile
    pipenv run python $HOME/dev/ntfy_client/src/app.py $argv
end
