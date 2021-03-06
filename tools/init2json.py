#!/usr/bin/env python3

import argparse
import configparser
import json
import os


def parse_channel_from_config(config, id):
    channel = {
        'id': id,
        'include_node_ids': [],
        'exclude_node_ids': [],
    }

    section = f'kolibri-{id}'
    if section not in config.sections():
        return channel

    channel_section = config[section]
    include_node_ids = channel_section.get('include_node_ids', '').split()
    exclude_node_ids = channel_section.get('exclude_node_ids', '').split()

    channel['include_node_ids'] = include_node_ids
    channel['exclude_node_ids'] = exclude_node_ids

    return channel


def ini2json(f, output='collections'):
    config = configparser.ConfigParser()
    config.read(f)

    out = {'channels': []}

    channel_ids = config['kolibri']['install_channels']
    for id in channel_ids.split():
        channel = parse_channel_from_config(config, id)
        out['channels'].append(channel)

    filename, _ext = os.path.splitext(os.path.basename(f))
    output_path = os.path.join(output, f'{filename}.json')
    with open(output_path, 'w') as output_file:
        json.dump(out, output_file, indent=2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert collection .ini files to manifest.json')
    parser.add_argument('files', metavar='INI_FILE', type=str, nargs='+',
                        help='A .ini file to convert to manifest.json')
    parser.add_argument('-o', '--output', type=str, default='collections',
                        help='The output directory, collections by default')

    args = parser.parse_args()
    for f in args.files:
        ini2json(f, args.output)
