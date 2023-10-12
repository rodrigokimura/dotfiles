if test -f "$DISPLAY"
  if test "x$XDG_VTNR" == "x1"
    exec startx
  end
end

if status is-interactive
  # Commands to run in interactive sessions can go here
end

alias ..="cd .."
alias ls="exa"
alias x="exit"
alias mkdir="mkdir -p"

alias vi="nvim"
alias vim="nvim"
alias config="cd $HOME/.config && nvim"

export EDITOR="nvim"

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)" # This only sets up the path stuff.
eval "$(pyenv init -)" # This makes pyenv work in the shell.
eval "$(pyenv virtualenv-init -)" # Enabling virtualenv so it works natively.

source ~/.config/fish/kanagawa.fish

[ -s "/home/rodrigokimura/.jabba/jabba.fish" ]; and source "/home/rodrigokimura/.jabba/jabba.fish"
