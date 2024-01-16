# Endless Key Collections

This project provides content collections used in the Endless Key app. These
content collections are defined in JSON files, using an extension of the
content manifest JSON format from Kolibri's `importcontent` and
`exportcontent` commands.

## Included content collections

### English

English language content collections are grouped into a set of "starter packs"
with different topics. The names are suffixed by a number, allowing for new
content packs to be added which build on the same topic:

- artist-0001.json
- athlets-0001.json
- curious-0001.json
- explorer-0001.json
- inventor-0001.json
- scientist-0001.json

In the Endless Key app, the user chooses a single starter pack. This affects
what content is installed when the user chooses the starter pack. In addition,
the app installs the metadata for all of the channels listed in each English
language content pack.

In addition, there are two "extras" collections:

- extras-0001.json
- extras-preload-0001.json

These collections, combined with the starter packs, describe what we consider
the complete Endless Key content library.

The `extras-0001.json` collection lists only channel IDs, and no content
nodes. This collection is imported when the user chooses a starter pack to
download in the Endless Key app. Importing it means that the app will retrieve
metadata for any channels listed in the collection, but no actual content.
This makes it easier for the user to choose individual pieces of content in
the future.

The `extras-preload-0001.json` lists both channel IDs *and* a selection of
content nodes inside those channels. This collection is intended for
specialized deployments, such as Endless OS images which come with large
libraries of content pre-installed.

### Spanish

At the moment, we have a single core Spanish language content collection,
instead of using topic-specific starter packs:

- spanish-0001.json

In addition, there is a set of "extras" collections.

- spanish-extras-0001.json
- spanish-extras-preload-0001.json

These collections work identically to their English language counterparts,
where `spanish-extras-0001.json` is a list of channels and no content, while
`spanish-extras-preload-0001.json` includes specific content nodes as well.

## How to install content collections

At the moment, Kolibri has no built in command to import both all channels and
all content from a given content manifest file. In addition, the format used
in this project includes an additional set of external content tags which
should be applied by a separate command in
[kolibri-explore-plugin](https://github.com/endlessm/kolibri-explore-plugin/).
To work around this, we can use [`jq`](https://github.com/jqlang/jq) to parse
the manifest files externally.

To import a content collection completely, try the following set of commands,
replacing "artist-0001.json" with the path to the content collection you wish
to import:

```sh
COLLECTION_FILE=artist-0001.json
# Import all channels from the manifest file:
jq -r '.channels[].id' $COLLECTION_FILE |
  xargs -n 1 kolibri manage importchannel network
# For each channel in the manifest file, import the content that is specified:
jq -r '.channels[].id' $COLLECTION_FILE |
  xargs -n 1 kolibri manage importcontent --manifest=$COLLECTION_FILE network
```

Optionally, if kolibri-explore-plugin is installed, apply the included content
tags:

```sh
# For each node_id / tags group in tagged_node_ids, run applyexternaltags:
jq -r '.metadata.tagged_node_ids[] | "--tags=\((.tags | join(","))) \(.node_id)"' $COLLECTION_FILE |
  xargs -n 2 kolibri manage applyexternaltags
```

## Development

Setup pre-commit:

```sh
pipenv install --dev
pipenv run pre-commit install
```

In case you want to run the checks by hand you can do:

```
pipenv run pre-commit run --all-files
```

### How to edit content collections

To edit the content collections in this repository, use the editor provided by
[https://github.com/endlessm/kolibri-dynamic-collections-plugin](kolibri-dynamic-collections-plugin).
The quickest way to access this editor is by installing the "Dynamic
Collections Plugin" add-on for the
[Kolibri app](https://flathub.org/apps/org.learningequality.Kolibri) on
Flathub.
