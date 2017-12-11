#!/bin/bash

source /home/alu5906/.virtualenvs/vm/bin/activate
uwsgi --ini /home/alu5906/vm/vmweb/uwsgi.ini
