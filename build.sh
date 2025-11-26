#!/bin/bash

# Fetch all tags and ensure they are up to date
git fetch --tags

# Echo current directory and list files for debugging
echo "Current directory: $(pwd)"
ls -la

# Get the latest tag
VERSION=$(git tag --sort=-creatordate | head -n 1)

echo "Latest tag: $VERSION"

# Update the version in pyproject.toml using sed
sed -i '' "s/^version = .*/version = \"$VERSION\"/" pyproject.toml

# Now run uv build with verbose output
uv build -v
