#!/bin/sh

python -c "import project.db.initial_setup as sdi; sdi.create_from_empty()"