#!/bin/bash

# Copyright 2023 Endless OS Foundation LLC
# SPDX-License-Identifier: GPL-2.0-or-later

set -e

TOOLSDIR=$(dirname "$(realpath "$0")")
SRCDIR=$(dirname "$TOOLSDIR")
JSONDIR="$SRCDIR/json"
OUTPUT="$SRCDIR/collections.zip"

echo "Creating $OUTPUT"
rm -f "$OUTPUT"
(cd "$JSONDIR" && zip -v "$OUTPUT" -- *.json)
