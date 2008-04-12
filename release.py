"""Automate release process. 

This is "dodo" file (suposed to be run with DoIt).
"""

def task_revision():
    return "bzr version-info > revision.txt"

def task_manifest():
    return "bzr ls --versioned > MANIFEST"

def task_sdist():
    return "python setup.py sdist"
