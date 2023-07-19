# LightningRod

An asynchronous command-line parsing servcie built on the [JC parser](https://github.com/kellyjonbrazil/jc)

Output is in JSON-formatted.

## Install and Run

LightningRod currently supports a local dev version of the service. Begin by cloning this repository.

`python3` prerequisite packages: `Djano`, `httpx`, and `django-ipware`

Run by using `python3 api/manage.py runserver`

The service will be accessible at http://localhost:8000/api/

## Endpoints

### POST /submit

Two required fields in the body of the request are `parser` and `file`.

`parser`: This is a string of the selection of how to interpret the command result. See the JC documentation for a list of supported parsers.

`file`: This is the command result that needs to be parsed.

Save the `ticket_number` number value to request the status.

### GET /submit

This returns the status of a submitted ticket. This takes one query parameter.

`ticket_number`: This is the number value returned from the initial POST request.

The output will be reutrned in JSON format in the field `p_output`.
