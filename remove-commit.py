from git_filter_repo import (
    FilterRepo,
    Commit,
    Filter,
)

def remove_commit(commit: Commit) -> bool:
    # Replace 'commit_hash_to_remove' with the hash of the commit you want to remove
    commit_hash_to_remove = "3018b2c"
    return commit.original_id == 3018b2c

filter_repo = FilterRepo(
    filter_function=remove_commit
)
filter_repo.run()

