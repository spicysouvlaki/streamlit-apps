"""
goal: explore relationships between comitters and files in a git repository
"""
import pydriller
import streamlit
from collections import defaultdict

repo = pydriller.RepositoryMining("/Users/williamschmitt/go/src/github.com/streamlit/streamlit")

def createAuthorsToChanges(n=2000):
    authors = defaultdict(list)

    for commit in repo.traverse_commits(): # this is an incredibly slow operation even on a beefy computer
        if len(commit.modifications) == 0:
            continue
        authors[commit.author.name].append((commit.committer_date, commit.modifications))

    return authors

def newModTupleForFile(commit, mod):
    return (commit.author, mod.added, mod.removed)

def createFilesToAuthors(n=2000):
    files = defaultdict(list)
    filenames = defaultdict(list)
    # this is an incredibly slow operation even on a beefy computer
    for commit in repo.traverse_commits():
        if n <= 0: break
        else: n -= 1
        if len(commit.modifications) == 0:
            continue

        for mod in commit.modifications:
            files[mod.new_path].append(newModTupleForFile(commit, mod))


    return authors
