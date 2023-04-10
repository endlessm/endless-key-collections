#!/usr/bin/env python3

import os
import json


def sanitize(filename):
    d = None
    with open(filename, "r") as f:
        d = json.load(f)

    existing = []
    for c in d["channels"]:
        existing.extend(c["include_node_ids"])

    new_tagged = []
    for t in d["metadata"]["tagged_node_ids"]:
        if t["node_id"] not in existing:
            continue
        elif len(t["tags"]) == 0:
            continue
        new_tagged.append(t)

    d["metadata"]["tagged_node_ids"] = new_tagged

    with open(filename, "w") as f:
        json.dump(d, f, indent=2)
        f.write("\n")


if __name__ == "__main__":
    sanitize("json/inventor-0001.json")
    sanitize("json/scientist-0001.json")
    sanitize("json/curious-0001.json")
    sanitize("json/explorer-0001.json")
    sanitize("json/athlete-0001.json")
    sanitize("json/artist-0001.json")
