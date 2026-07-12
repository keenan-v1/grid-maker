#!/usr/bin/env sh
#
# install.sh - Install the `gridmaker` CLI using uv.
#
# This bootstraps uv if it is missing, then installs gridmaker as a uv-managed
# tool. uv prefers prebuilt wheels and manages its own Python, so this avoids
# the "needs Python dev headers" source builds (e.g. compiling Pillow).
#
# Usage:
#   ./install.sh                          # install from this checkout
#   curl -LsSf https://raw.githubusercontent.com/keenan-v1/grid-maker/main/install.sh | sh
#
set -eu

REPO_URL="https://github.com/keenan-v1/grid-maker"

info() { printf '\033[1;34m==>\033[0m %s\n' "$1"; }
err() { printf '\033[1;31merror:\033[0m %s\n' "$1" >&2; }

# 1. Ensure uv is available.
if ! command -v uv >/dev/null 2>&1; then
    info "uv not found; installing it..."
    if command -v curl >/dev/null 2>&1; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
    elif command -v wget >/dev/null 2>&1; then
        wget -qO- https://astral.sh/uv/install.sh | sh
    else
        err "Need either curl or wget to install uv. Install one and retry."
        exit 1
    fi
    # Make uv available in the current shell for the rest of this script.
    for dir in "$HOME/.local/bin" "$HOME/.cargo/bin"; do
        if [ -x "$dir/uv" ]; then
            PATH="$dir:$PATH"
            export PATH
        fi
    done
fi

if ! command -v uv >/dev/null 2>&1; then
    err "uv installation did not add uv to PATH. Open a new shell and re-run."
    exit 1
fi

info "Using uv: $(uv --version)"

# 2. Install gridmaker as a uv tool.
#    If run from inside a checkout (pyproject.toml present) install from here;
#    otherwise install straight from GitHub.
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ -f "$SCRIPT_DIR/pyproject.toml" ]; then
    info "Installing gridmaker from local checkout: $SCRIPT_DIR"
    uv tool install --force "$SCRIPT_DIR"
else
    info "Installing gridmaker from $REPO_URL"
    uv tool install --force "git+$REPO_URL"
fi

info "Done. Run 'gridmaker -h' to get started."
info "If 'gridmaker' isn't found, run 'uv tool update-shell' and open a new shell."
