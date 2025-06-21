#!/bin/zsh
# Usage: ./remove_references.sh input.md

# This script removes reference patterns like [1], [23], [^1_1], [^1_2], etc., from the input file in place.
# It creates a backup of the original file as input.md.bak

if [ -z "$1" ]; then
  echo "Usage: $0 input.md"
  exit 1
fi

cp "$1" "$1.bak"
# Remove [1], [23], [^1_1], [^1_2], etc.
sed -i '' -E 's/\[(\^?[0-9]+(_[0-9]+)?)\]//g' "$1"
