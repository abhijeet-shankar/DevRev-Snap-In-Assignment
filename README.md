
# Snap-in Development




## DevRev API Work Item Creation

This repo demonstrates how to create a work item using the DevRev API. The work_item.py shows how to make an HTTP POST request to the DevRev API endpoint to create,delete,get details of a (new) work item.

## Prerequisites

Before running the code, ensure you have the following:

- Python installed on your system
- `requests` library installed (`pip install requests`)
- DevRev API credentials (API key)
- Required details for payload for creating work items.

## Setup

- Clone this repository to your local machine.
- Install the required Python libraries using pip:


## Usage

- Install the required dependencies by running pip install requests in your terminal.
- Run the work_create.py in your system.
- Enter the APIs key where needed.
```
py -m work_create.py
```


## Snap In Installation Guide

- Install Devrev Cli
    - Download and Extract the Devrev Cli
    - Add path of Devrev to environment path

- Install jq
```bash
  choco install jq
```

- Install Devrev SDK @typescript
```bash
    npm init 
    npm i @devrev/typescript-sdk
```

- Authenticate Devrev profile
```bash 
    devrev profiles authenticate -o <own-slug> -u <usr_mail>
```

- Initialisation of snap in
```
devrev snap_in_version init
```

Configure manifest.yaml and write a function hello_world.py for hello world code.