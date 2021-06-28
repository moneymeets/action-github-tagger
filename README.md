# action-github-tagger

GitHub action for tagging a commit.

**Note:** this action is deprecated, because instead of using GitHub API to create tags (which is also possible inline with `curl` or https://github.com/actions/github-script), it can be re-implemented with two lines of code using `git` commands in the workflow itself:

```yml
- name: Tag
  if: github.event.deployment.environment == 'live'
  run: |
    git config user.name 'Sir Mergealot'
    git config user.email 'mergealot@moneymeets.com'

    git tag ${{ format('{0}/v{1}', github.event.deployment.environment, steps.heroku_deployment.outputs.release_version) }}
    git push --tags
```
